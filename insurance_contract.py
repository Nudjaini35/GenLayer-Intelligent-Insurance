# High-level primitive logic structure for GenLayer execution
from genlayer import IntelligentContract, consensus, WebData

class FlightInsurance(IntelligentContract):
    def __init__(self):
        self.insurance_pool = {}
        self.premium_cost = 0.05 * 10**18  # in ETH testnet
        self.payout_amount = 0.5 * 10**18

    @consensus
    def verify_and_payout(self, flight_number: str, departure_date: str) -> bool:
        # Call GenLayer validators to scrape multiple real-time web sources
        evidence_1 = WebData.get(f"https://flightradar24.com{flight_number}")
        evidence_2 = WebData.get(f"https://google.com{flight_number}+delay+news")

        # LLM Prompt executed during consensus phase
        prompt = f"Analyze the following data logs for Flight {flight_number} on {departure_date}. Determine if it was delayed by more than 4 hours due to force majeure. Evidence 1: {evidence_1}, Evidence 2: {evidence_2}. Respond strictly in JSON: {{'delayed': true/false, 'reason': 'text'}}"

        result = self.call_llm_consensus(prompt)

        if result['delayed'] == True:
            self.execute_payout()
            return True
        return False
