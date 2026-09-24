from Contract_NDA_Agreement_OOP import Contract, NDA, LeaseAgreement

contract1 = Contract(
    "CON-001",
    "Microsoft India",
    "01-01-2026",
    "Active"
)
contract2 = NDA(
    "NDA-002",
    "Tata Consultancy Services",
    "15-02-2026",
    "Active",
    "5 years"
)
contract3 = LeaseAgreement(
    "LEASE-003",
    "Amazon India",
    "01-04-2026",
    "Active",
    "Bangalore, Karnataka"
)
contracts = [contract1, contract2, contract3]
for contract in contracts:
    contract.display_contract()
    print("\n" + "-" * 40 + "\n")