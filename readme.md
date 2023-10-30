# simplePointService Docker Compose

This Docker Compose project sets up a development environment for the `simplePointService` using Flask as the application framework and PostgreSQL as the database. It provides a simple way to run the application and its dependencies in a containerized environment.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Prerequisites

Before you can use this Docker Compose environment, ensure that you have the following software installed on your local machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Usage

Follow these steps to set up and run the `simplePointService` with Docker Compose:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/LeonTWYO/simplePointService.git
cd simplePointService
docker-compose up
```
Access the Flask app
Once the environment is up and running, you can access the Flask API via http://localhost:8080. The app should be available on port 8080 of your local machine.

## API Endpoints
The simplePointService provides the following API endpoints for managing user points:

1. Create User and Give Initial Balance:

- Endpoint: /user/create_user
- HTTP Method: POST
- Description: Create a new user and provide an initial points balance.
- Request Body:
```json
{
  "username": "username",
  "initial_balance": 100
}
```
- Response: A JSON object containing the serial_user_id.

2. Get Balance by User ID:
- Endpoint: /user/get_balance/<user_id>
- HTTP Method: GET
- Description: Retrieve the points balance of a specific user by their user ID.
- Response: A JSON object containing the user's balance.

3. Give Points:

- Endpoint: /user/give_points
- HTTP Method: POST
- Description: Give points to a specific user.
- Request Body:
```json
{
  "user_id": "serial_user_id",
  "points": 50
}
```
- Response: A JSON object confirming the transaction.

4. Use Points:

- Endpoint: /user/use_points
- HTTP Method: POST
- Description: Allow a user to use their points.
- Request Body:
```json
{
  "user_id": "serial_user_id",
  "points": 30
}
```
- Response: A JSON object confirming the transaction.

5. Get Latest Transactions:

- Endpoint: /user/get_latest_transactions/<user_id>
- HTTP Method: GET
- Description: Retrieve the latest transaction records of a specific user by their user ID.
- Request Body:
- Response: A JSON object containing the user's the latest 10 transaction records.