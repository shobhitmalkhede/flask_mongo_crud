1. Flask MongoDB CRUD Application

This is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a `User` resource using a REST API. It includes Docker support and is designed to be scalable, structured, and easy to use. The application provides API endpoints for managing users and can be tested using Postman.

## Project Structure

flask_mongo_crud/ ├── app/ │ ├── init.py # Initializes the app, database, and routes │ ├── config.py # Configuration settings for the app and MongoDB │ ├── routes.py # Routes and API endpoints for CRUD operations │ ├── models.py # MongoDB models (user schema) ├── tests/ # Folder containing test cases │ └── test_routes.py # Unit tests for the routes ├── Dockerfile # Dockerfile for building the app's Docker image ├── requirements.txt # List of Python dependencies ├── .env # Environment variables (MongoDB URI, etc.) ├── README.md # Project overview, setup instructions, and usage ├── run.py # Entry point to run the Flask app ├── docker-compose.yml # Docker Compose file to manage app and MongoDB container └── .gitignore # Specifies files and directories to ignore in Git


## Prerequisites

- Docker and Docker Compose
- Python 3.10 or higher (if not using Docker)
- MongoDB running (handled by Docker Compose in this setup)

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/flask_mongo_crud.git
cd flask_mongo_crud

2. Set Up Environment Variables

Create a .env file in the root directory and add the following configuration (you can replace with your MongoDB URI if not using Docker):

MONGODB_URI=mongodb://mongo:27017/flask_mongo_crud
FLASK_APP=run.py
FLASK_ENV=development

3. Install Dependencies
Option 1: Using Docker (Recommended)

If you're using Docker, you don't need to worry about installing dependencies manually. Docker Compose will handle this for you.

    Build and run the application using Docker Compose:

docker-compose up --build

This will build the Docker image, create the containers, and start the Flask app along with the MongoDB service.
Option 2: Without Docker

If you're not using Docker, you need to manually install the dependencies:

    Create a virtual environment (recommended):

python3 -m venv venv

    Activate the virtual environment:
        For Linux/macOS:

source venv/bin/activate

    For Windows:

    .\venv\Scripts\activate

    Install the required Python dependencies:

pip install -r requirements.txt

4. Run the Application
Option 1: Using Docker

Once the containers are up, you can access the app at http://localhost:5000. Docker will manage everything for you.
Option 2: Without Docker

To run the app without Docker:

python run.py

This will start the Flask server, and you can access the API at http://localhost:5000.
5. Test the API Endpoints

You can test the CRUD operations using Postman.

The following API endpoints are available:

    GET /users - Retrieve all users
    GET /users/<id> - Retrieve a specific user by ID
    POST /users - Create a new user
    PUT /users/<id> - Update an existing user by ID
    DELETE /users/<id> - Delete a user by ID

Example Requests:

    Create User (POST):
        URL: http://localhost:5000/users
        Body (JSON):

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}

Get All Users (GET):

    URL: http://localhost:5000/users

Get User by ID (GET):

    URL: http://localhost:5000/users/<id>

Update User (PUT):

    URL: http://localhost:5000/users/<id>
    Body (JSON):

    {
      "name": "John Updated",
      "email": "johnupdated@example.com",
      "password": "newpassword123"
    }

    Delete User (DELETE):
        URL: http://localhost:5000/users/<id>

6. Run Tests

You can run unit tests to ensure everything works as expected.

    Install pytest if it's not already installed:

pip install pytest

    Run tests:

pytest tests/test_routes.py

This will run the unit tests defined in test_routes.py.
Docker Compose Configuration

The docker-compose.yml file defines two services:

    flask_mongo_crud: The Flask application running on port 5000.
    mongo: The MongoDB database, running on the default MongoDB port (27017).

Both services are connected via the MONGODB_URI defined in the .env file.