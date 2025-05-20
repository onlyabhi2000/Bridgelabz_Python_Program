f= open("demo.text","r")
# data = f.read()

#Reading data line  by line -> readline()
line1= f.readline()
line2 = f.readline()

print(line1)
print(line2)
# print(data)
# print(type(data))

f.close()