import re

def classify_department(abc_text):
    abc = abc_text.lower()

    if any(x in abc for x in ["payment", "refund", "billing", "charge", "invoice", "subscription"]):
        return "Billing"

    if any(x in abc for x in ["crash", "error", "bug", "failed", "locked", "not working"]):
        return "Technical"

    if any(x in abc for x in ["pricing", "cost", "enterprise", "quote", "plan"]):
        return "Sales"

    if any(x in abc for x in ["feature request", "add feature", "can you add"]):
        return "Product"

    return "General"


def analyze_sentiment(abc_text):
    abc = abc_text.lower()

    if any(x in abc for x in ["third time", "angry", "frustrated", "urgent", "!!!", "nobody"]):
        return "Frustrated"

    if any(x in abc for x in ["thank", "great", "appreciate"]):
        return "Satisfied"

    return "Neutral"


def assess_priority(abc_text, abc_sentiment):
    abc = abc_text.lower()

    if "urgent" in abc:
        return "Critical"

    if abc_sentiment == "Frustrated":
        return "High"

    if any(x in abc for x in ["failed", "locked", "error"]):
        return "High"

    if any(x in abc for x in ["pricing", "cost", "quote"]):
        return "Medium"

    return "Low"


def extract_entities(abc_text):
    abc_entities = {}

    abc_error = re.search(r'[A-Z]{2,5}-\d{3,5}', abc_text)
    if abc_error:
        abc_entities["error_code"] = abc_error.group()

    abc_version = re.search(r'v\d+\.\d+(\.\d+)?', abc_text)
    if abc_version:
        abc_entities["version"] = abc_version.group()

    abc_size = re.search(r'\d+MB|\d+GB', abc_text)
    if abc_size:
        abc_entities["file_size"] = abc_size.group()

    if "payment" in abc_text.lower():
        abc_entities["issue_type"] = "Payment Failure"

    if "crash" in abc_text.lower():
        abc_entities["issue_type"] = "Technical Bug"

    if "cancel" in abc_text.lower() and "refund" in abc_text.lower():
        abc_entities["multi_issue"] = True

    return abc_entities


def search_faq(abc_text):
    abc = abc_text.lower()

    abc_data = {
        "payment": "Please verify your card details and try again.",
        "refund": "Refunds are processed within 5-7 business days.",
        "crash": "Please update to the latest version and clear cache.",
        "locked": "Use the forgot password option to regain access.",
        "pricing": "Our sales team will share detailed pricing options."
    }

    for abc_key in abc_data:
        if abc_key in abc:
            return abc_data[abc_key]

    return "Our team will review your issue and get back shortly."


def generate_response(abc_ticket, abc_dept, abc_priority, abc_sentiment, abc_solution):
    abc_name = abc_ticket.get("Customer Name", "Customer")

    if abc_sentiment == "Frustrated":
        abc_line = "We sincerely apologize for the inconvenience caused."
    else:
        abc_line = ""

    abc_reply = f"""
Dear {abc_name},

{abc_line}
Thank you for contacting us.

Your issue has been routed to our {abc_dept} department with {abc_priority} priority.

Suggested Help:
{abc_solution}

Please let us know if you need further assistance.

Best Regards,
Support Team
"""

    return abc_reply.strip()


def log_decision(abc_text, abc_dept, abc_priority):
    return f"Routed to {abc_dept} due to keyword detection. Priority set to {abc_priority} based on urgency and sentiment."