import requests
import json


def test_hello():
    response = requests.get('http://localhost:8080')
    print(response.status_code)
    print(response.json())
def create_user():
    # Replace with your actual data
    data = {
        "username": "testUser",
        "initial_balance": 100  # or any desired initial balance
    }

    url = "http://localhost:8080/create_user"  # Replace with your server URL

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())
def get_balance():
    # Make a GET request to the API endpoint
    response = requests.get("http://localhost:8080/get_balance/1")
    # Check the response status code
    if response.status_code == 200:
        # Successful response
        data = response.json()
        balance = data["balance"]
        print(f"User's balance: {balance}")
    elif response.status_code == 404:
        # User not found
        error = response.json()["error"]
        print(f"Error: {error}")
    else:
        # Other errors
        error = response.json()["error"]
        print(f"Error: {error}")
def use_points():
    # Replace with your actual data
    data = {
        "user_id": 1,
        "points": 100  # or any desired initial balance
    }

    url = "http://localhost:8080/use_points"  # Replace with your server URL

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())
def give_points():
    # Replace with your actual data
    data = {
        "user_id": 1,
        "points": 150  # or any desired initial balance
    }

    url = "http://localhost:8080/give_points"  # Replace with your server URL

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())
if __name__=="__main__":
    create_user()
    get_balance()
    use_points()
    get_balance()
    give_points()
    get_balance()

