def checknumber(number):
    if number > 7:
        print("Hello") 
def checkname(name):
    if name == "John":
        print("Hello,John")
    elif name!="John":
        print("There is no such name") 
def arraymultiply(array):
    final = []
    for i in array:
        i = i * 3
        final.append(i)
    print(final)

numinput = int(input("Enter number: "))
checknumber(numinput)
nameinput = input("Enter name: ")
checkname(nameinput)
arrayinput = []
arraysize = int(input("Enter array size: "))
print("Enter array: ")
for i in range(0,arraysize):
    i = int(input())
    arrayinput.append(i)
arraymultiply(arrayinput)