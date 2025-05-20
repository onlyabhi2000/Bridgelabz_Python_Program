# f = open("demo.text" ,"w")

# data = f.write("This will overwrite all the text in the file")

f = open("demo.text" ,"a")
data = f.write("\nappend will add the text at the end of the file , without overwriting ")
f.close()