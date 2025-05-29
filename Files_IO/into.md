# Synatx 1-->  open , read and close the file

f = open("file_name" , "mode")
data = f.read()
f.close()


## Syntax 2--> 

with open("file_name", "mode") as f:
    data = f.read()
    ## note --> no need to close the file , with will handle 