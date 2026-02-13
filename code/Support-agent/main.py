from Agent import SupportAgent

abc_agent = SupportAgent()

abc_ticket = {
    "Ticket ID": "T-1001",
    "Customer Name": "John",
    "Ticket Description": "My payment failed 3 times and now my account is locked! This is urgent! Error PAY-403"
}

abc_result = abc_agent.process_ticket(abc_ticket)

print(abc_result)