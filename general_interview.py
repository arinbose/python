print ('..........Reverse a Number.........')
n=int(input("Enter number: "))
rev=0
while(n>0):
 dig=n%10
 rev=rev*10+dig
 n=n//10
print("The reverse of the number:",rev)

print ('..........Sum of the Digits of a Number.........')
n=int(input("Enter a number:"))
tot=0
while(n>0):
 dig=n%10
 tot=tot+dig
 n=n//10
print("The total sum of digits is:",tot)