import os
import sys
import json
import sqlite3

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

import mock_llm


def get_order(order_id):
    conn = sqlite3.connect("data/instamart.db")
    conn.row_factory = sqlite3.Row

    order = conn.execute(
        """
        SELECT order_id, status, order_amount, delivery_minutes
        FROM orders
        WHERE order_id = ?
        """,
        (order_id,)
    ).fetchone()

    conn.close()

    if order is None:
        return {"error": "Order not found"}

    return {
        "order_id": order["order_id"],
        "status": order["status"],
        "order_amount": float(order["order_amount"]),
        "delivery_minutes": order["delivery_minutes"]
    }


def search_policy(query):
    return {
        "policy": "Only completed orders are eligible. Orders delivered after 45 minutes qualify for a full refund. Refunds above INR 1000 need human approval."
    }


def calculate_refund(order_amount, delivery_minutes):
    if delivery_minutes is None or delivery_minutes <= 45:
        refund = 0
    else:
        refund = order_amount

    return {"refund_inr": refund}


def issue_refund(order_id, refund_inr):
    return {
        "order_id": order_id,
        "refund_inr": refund_inr,
        "status": "approved"
    }


def escalate_to_human(order_id, refund_inr):
    return {
        "order_id": order_id,
        "refund_inr": refund_inr,
        "status": "sent to human support lead"
    }


TOOLS = {
    "get_order": get_order,
    "search_policy": search_policy,
    "calculate_refund": calculate_refund,
    "issue_refund": issue_refund,
    "escalate_to_human": escalate_to_human
}


def run_refund_agent(order_id):
    mock_llm.reset()

    messages = [
        {
            "role": "system",
            "content": "You are an AGENT. Follow refund policy and use tools."
        },
        {
            "role": "user",
            "content": f"Please check refund eligibility for order {order_id}."
        }
    ]

    for step in range(6):
        response = mock_llm.chat(messages, tools=[])
        message = response.choices[0].message

        if message.content:
            print("\nAgent:", message.content)
            return message.content

        if message.tool_calls:
            for tool_call in message.tool_calls:
                name = tool_call.name
                arguments = tool_call.arguments

                if isinstance(arguments, str):
                    arguments = json.loads(arguments)

                result = TOOLS[name](**arguments)

                print("Tool used:", name)
                print("Result:", result)

                messages.append({
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [{
                        "id": tool_call.id,
                        "type": "function",
                        "function": {
                            "name": name,
                            "arguments": json.dumps(arguments)
                        }
                    }]
                })

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": json.dumps(result)
                })

    print("Human handoff: maximum 6 steps reached.")


if __name__ == "__main__":
    print("REFUND AGENT TEST")
    run_refund_agent("ORD-102006")