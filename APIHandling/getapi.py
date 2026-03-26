import requests

def get_api_details():
    urls = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(urls)
    data = response.json() ### need to convert into python json format so python can understand
    print(data)
    if data["success"]:
        user_data = data["data"]
        print(user_data)
        username =user_data["login"]["username"]
        country = user_data["location"]["country"]
        print(f"Username: {username}")
        print(f"Country: {country}")
        return username, country

    else :
        raise Exception("API requedst was not successful")
get_api_details()