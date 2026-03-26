import requests

url = "https://jsonplaceholder.typicode.com/users//hhh"

try:
    response = requests.get(url)
    # Raise an error if the request failed (e.g., 404 or 500 error)
    response.raise_for_status() 
    
    data = response.json()

    for rec in data:
        # Using .get() is safer in case a record is missing an "id"
        print(f"User ID: {rec.get('id')}")

except requests.exceptions.RequestException as e:
    print(f"Connection Error: {e}")