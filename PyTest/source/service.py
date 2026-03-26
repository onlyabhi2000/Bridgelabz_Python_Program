import requests

database ={
    1 : "Abhishek",
    2 : "sachin",
    3 : "Sashikant"
}


def get_user_id(user_id):
    return database.get(user_id)



def get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError
