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

    url = "http://localhost:8080/user/create_user"  # Replace with your server URL

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())
    return response.json()['user_id']

def get_balance(user_id):
    # Make a GET request to the API endpoint
    response = requests.get(f"http://localhost:8080/user/get_balance/{user_id}")
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
def use_points(user_id,points):
    # Replace with your actual data
    data = {
        "user_id": user_id,
        "points": points  # or any desired initial balance
    }

    url = "http://localhost:8080/user/use_points"  # Replace with your server URL

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())
def give_points(user_id,points):
    # Replace with your actual data
    data = {
        "user_id": user_id,
        "points": points  # or any desired initial balance
    }

    url = "http://localhost:8080/user/give_points"  # Replace with your server URL

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())
def get_latest_transactions(user_id):
    url = f"http://localhost:8080/user/get_latest_transactions/{user_id}"  # Replace with your server URL

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.json())
if __name__=="__main__":
    user_id=create_user()
    get_balance(user_id)
    use_points(user_id,200)
    get_balance(user_id)
    give_points(user_id,150)
    get_balance(user_id)
    use_points(user_id,200)
    get_balance(user_id)
    get_latest_transactions(user_id)
