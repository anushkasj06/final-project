#r= int(input())
#area=3.14*r*r
#print(area)

#str1 = "anushka"
#str2 = "jadhav"
#print(str1+str2)
#h=int(input())
#if(h>10):
#	print( " the number is greater than 10")
#elif(h<10):
#	print("the number is less than 10")
#else:
#	print("equal")

import random 
 r = random.randint(1,20)

 while(True):
 	inp=int(input())
 	if(inp<r):
 		print("wrong guess, try a greater number")
 	elif(inp>r):
 		print("wrong guess , try a smaller number")
 	else:
 		print("congrats ")
 		break;
