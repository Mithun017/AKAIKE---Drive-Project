from tools import classify_department
from tools import analyze_sentiment
from tools import assess_priority
from tools import extract_entities
from tools import search_faq
from tools import generate_response
from tools import log_decision


class SupportAgent:

    def process_ticket(self, ticket):

        text = ticket.get("Ticket Description", "")

        sentiment = analyze_sentiment(text)

        entities = extract_entities(text)

        department = classify_department(text)

        priority = assess_priority(text, sentiment)

        solution = search_faq(text)

        escalation = False

        if sentiment == "Frustrated" and priority in ["High", "Critical"]:
            escalation = True

        if "multi_issue" in entities:
            escalation = True

        response = generate_response(
            ticket,
            department,
            priority,
            sentiment,
            solution
        )

        reasoning = log_decision(text, department, priority)

        return {
            "ticket_id": ticket.get("Ticket ID"),
            "department": department,
            "priority": priority,
            "sentiment": sentiment,
            "entities": entities,
            "suggested_response": response,
            "escalation_required": escalation,
            "reasoning": reasoning
        }