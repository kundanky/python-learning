#class attendance checker
#lists #loops()
names = ["kundan","sakshi","rohit","om","ritesh","ayush","nishant"]
att_percent = [82, 85,64,89,95,34,100]
eligible = []
non_eligible=[]
pass_count = 0
fail_count = 0
for i in range(len(att_percent)):
	if att_percent [i] >= 75:
		pass_count = pass_count + 1 
		print (names[i],att_percent [i],"%")
		eligible.append(names[i])
		
	else :
		fail_count=fail_count +1
		print (names[i],att_percent [i],"%")
		non_eligible.append(names[i]) 
		

print("Total eligible students:",pass_count,eligible)
print("Non-Eligible students:",fail_count,non_eligible)