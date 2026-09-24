class Contract:
  def __init__(self,contract_id,party,start_date,status):
    self.contract_id = contract_id
    self.party= party
    self.start_date = start_date
    self._status =status
  @property
  def status(self):
  	return self._status
  @status.setter
  def status(self, new_status):
  	allowed_statuses = ["Pending","Active","Expired","Terminated"]
  	if new_status in allowed_statuses:
  		self._status =new_status
  	else:
  		print("Invalid Contract Status!")
  def display_contract(self):
    print(f"Contract: {self.contract_id}")
    print(f"Party: {self.party}")
    print(f"Start Date: {self.start_date}")
    print(f"Status: {self.status}")
  def update_status(self,new_status):
    self.status = new_status
#running part 
contract1 = Contract(
    "CON-001",
    "Microsoft India",
    "01-01-2026",
    "Active"
)

contract1.display_contract()

contract1.update_status("Banana")

contract1.display_contract()