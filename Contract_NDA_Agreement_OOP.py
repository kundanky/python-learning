# Legal OOP for contracts, NDA, Agreements
# Legal Case Management System

class Contract:
    def __init__(self, contract_id, party, start_date, status):
        self.contract_id = contract_id
        self.party = party
        self.start_date = start_date
        self.status = status

    def display_contract(self):
        print(f"Contract: {self.contract_id}")
        print(f"Party: {self.party}")
        print(f"Start Date: {self.start_date}")
        print(f"Status: {self.status}")


class NDA(Contract):
    def __init__(self, contract_id, party, start_date, status, confidentiality_period):
        super().__init__(contract_id, party, start_date, status)
        self.confidentiality_period = confidentiality_period

    def display_contract(self):
        print(f"Contract: {self.contract_id}")
        print(f"Party: {self.party}")
        print(f"Start Date: {self.start_date}")
        print(f"Status: {self.status}")
        print(f"Confidentiality Period: {self.confidentiality_period}")


class LeaseAgreement(Contract):
    def __init__(self, contract_id, party, start_date, status, property_address):
        super().__init__(contract_id, party, start_date, status)
        self.property_address = property_address

    def display_contract(self):
        print(f"Contract: {self.contract_id}")
        print(f"Party: {self.party}")
        print(f"Start Date: {self.start_date}")
        print(f"Status: {self.status}")
        print(f"Property Address: {self.property_address}")