from legal_OOP import LegalCase , CriminalCase, CorporateCase 
client1 = LegalCase( 101, "Kundan", "Bombay High Court","Divorce")
client1.display_case()
client2 = CriminalCase(102, "Ydv", "Delhi High Court","Online_Case","Pirate")
client2.display_case()
client3 = CorporateCase(103, "K"," Supreme Court","Fraud","SpaceX")
client3.show_company_details()
print(client3.company_name)