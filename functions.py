#functions
def love(B,G):
	return B + " " + "love"+" " + G 
full =love("I","Sakshi")
print(full)

def calc(x, y):
	z = x + y
	a = z - y
	b = a * z
	c = b / a
	return  c
  #unpacked result
print(calc(50, 40)) 
print()
print()
print()
#diff variant packed result (tuple)
#def calc(x, y):
	#z = x + y
#	a = z - y
	#b = a * z
	#c = b / a
	#return z , a, b, c
#result= calc(50, 40)
#print(result)

#import time
#def count(start, end=0):
#	for i in range(start,end,-1):
#		print(i)
#		time.sleep(1)
#	print("Done!")
#count(10,0)

import time
def count(start=1,end=10):
	for i in range(start,end+1):
		print(i)
		time.sleep(1)
	print("Done!")
#start = int(input("Enter starting time in seconds:"))
end = int(input("Enter stop time in seconds:"))
count(end=end)