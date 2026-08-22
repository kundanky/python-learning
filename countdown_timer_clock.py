import time
my_time= int(input("Enter your time in seconds:")) 
for x in range(my_time, 0,-1) :
	seconds = x  % 60
	minutes = int(x / 60) % 60
	hours = int(x/3600) %3600
	days = int(x/86400)
	print(f"{days:01}d:{hours :02}:{minutes :02}:{seconds :02}")
	time.sleep(1)
print("times up")