class LegalCase:
	def __init__(self, case_num, client_name, court,case_type):
		self.case_num = case_num
		self.client_name = client_name
		self.court = court
		self.case_type = case_type
	def display_case(self):
		print(f"Case No. : {self.case_num}| Client Name :{self.client_name}| Court :{self.court}| for:{self.case_type}!")
class CriminalCase(LegalCase):
	def __init__(self,case_num, client_name, court,case_type,offence):
		super().__init__(case_num, client_name, court,case_type)
		self.offence = offence
	def display_case(self):
		super().display_case()
		print(f"did {self.offence}")
class CorporateCase(LegalCase):
	def __init__(self,case_num, client_name, court,case_type,company_name):
		super().__init__(case_num, client_name, court,case_type)
		self.company_name = company_name
	def show_company_details(self):
		super().display_case()
		print(f"company name {self.company_name}")