template = "Hello <<UserName>>, How are you?"

username = input("Enter your name: ")
if len(username) > 3:
    message = template.replace("<<UserName>>", username)
    print(message)
