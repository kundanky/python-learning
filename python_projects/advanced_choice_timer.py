# let user select for countdown or count up
import time
def count_up(start=1,end =10):
	for i in range(start, end+1):
		print(i)
		time.sleep(1)
	print("Done!")
def count_down(start,end =1):
	for i in range(start,end-1,-1):
		print(i)
		time.sleep(1)
	print("Done!")
while True:
	choice = input("Enter 'u' for timer or 'd' to countdown(q to quit):").lower()
	if choice == "q":
		break
	elif choice =="u":
		end = int(input("Enter stop time in seconds:"))
		count_up(end=end)
	elif choice =="d":
		start = int(input("Enter start time in seconds:"))
		count_down(start=start)