#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
		roll=input("press r to roll the dice")
		if roll=="r":
			r=random.randint(1,6)
			count=count+r
			print("your random num is",r)

			if count==8:
				count=37
				print("wow u climbed to ladder",count)
			elif count==13:
				count=34
				print("wow u climed the ladder",count)
			elif count==40:
				count=68
				print("wow u climed the ladder",count)
			elif count==52:
				count=81
				print("wow u climed the ladder",count)
			elif count==76:
				count=97
				print ("wow u climbed ladder",count)
			elif count==11:
				count=2
				print("oops u r bitten by snake",count)
			elif count==25:
		   	    count=4
				print("oops u r bitten by snake",count)
        	elif count==38:
            	count=9
            	print("oops u r bitten by snake",count)
       	    elif count==65:
            	count=46
            	print("oops u got bitten by snake"count)
       	    elif count==89:
            	count=70
            	print("oops u got bitten by snake",count)
    	    elif count==97:
            	count=76
            	print ("oops u got bitten by snake",count)
            else:
				print("you are on count",count)

