#Uppgift 1
print("Uppgift 1a")
nice_name = "Kim"
print(nice_name)


print("Uppgift 1b")
long_name = ""
for i in range(33):
    long_name += "Kim"

print(long_name)

#Uppgift 2
print("Uppgift 2")
input_name = input("Vad heter du?")

for i in range(39):
    print(input_name)


#Uppgift 3
print("Uppgift 3")
input_name = input("Vad heter du?")

while input_name != "Shouron":
    print("Hej " + input_name)
    input_name = input("Vad heter du?")
else: 
    print("Hej då")


#Uppgift 4
print("Uppgift 4")
print (1 == 0.99)
print (1 == 0.99999999999)
print (1 == 0.99999999999999999999)

#Uppgift 5
print("Uppgift 5")
import math
def summa(n):
    result = sum (1/ (k**2) for k in range (1,n))
    return result

print ("När n går mot oändligheten så närmar sig summan värdet π**2/6 ≈ 1.64493406685")
print (summa(10))
print (summa(100))
print (summa(1000))








