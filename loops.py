# i = 1
# numList = []
# while i < 6:
#     numList.append(int(input("Enter a number: ")))
#     i = i + 1
# print(numList)

# for loop
fruiet = ["banana","apple","oreange"]

string = "Apple"
for x in fruiet:
    if x == "apple":
        continue
    print(x)
    
for i in range(5):
    print(i)
    
##Print the table of 3 using 
#while and for loops

i = 1
while i<11:
    print("3 x",i,"=",i*3)
    i += 1
print("")
for i in range(1,11):
    print("3 x",i,"=",i*3)