#Example
A = int(input("A:"))
G = input("M/f:")
if((A==1 or A==2)and G=="M"):
    print("100")
elif(A==3 or A==4 or G=="F"):
    print("200")
elif(A==5 and G=="M"):
    print("200")
else:
    print("No fee")
    
#Eg2
food = input()
eat = "yes" if food == "cake" else "no"
print(eat)
#Eg3
food = input()
eat1 = "yes" if food == "cake" or food == "jalabi" else "no"
print(eat1)

#Calculate Simple Interest
p=float(input("Principal Ammount:"))
r=float(input("Rate"))
t=float(input("Time in Years:"))
SI= (p*r*t)/100
print(SI)