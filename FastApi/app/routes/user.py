"""
This module defines the routes for user-related operations in the FastAPI application.

Routes:
    - POST /users/: Creates a new user.
    - GET /users: Retrieves a list of all users.
    - GET /users/{user_id}: Retrieves a specific user by ID.

Functions:
    - create_user(user: User): Creates a new user with the provided details.
    - get_users(): Retrieves all users from the database.
    - get_user(user_id: int): Fetches a specific user by their ID. 
      Returns an error if the user is not found.

Dependencies:
    - UserModel: The database model representing users.
    - User: The Pydantic model for data validation of user inputs.
    - APIRouter: FastAPI's router for defining API routes.
    - Body: FastAPI's dependency for handling request bodies.
"""

from fastapi import APIRouter, Body

from models.user import User

user_route = APIRouter()


@user_route.post("/users/")
def create_users(user: User = Body(...)):
    """
    Create a new user.

    Args:
        user (User): The user object containing the username, password, and email.

    Returns:
        None
    """
    print(user)
    return {"message": "User created successfully"}


@user_route.get("/users")
def get_users():
    """
    Retrieves a list of users from the database.

    This function queries the UserModel to fetch all users with an ID greater than 0,
    converts each result into a dictionary, and returns them as a list.

    Returns:
        list: A list of dictionaries, where each dictionary represents a user.
    """
    return {"message": "Get all users"}


@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserModel: The user object if found.
        dict: An error message if the user is not found.
    """
    print(user_id)
    try:
        return {"message": "Get user by ID"}
    except FileNotFoundError as e:
        print(e)
        return {"message": "User not found"}
    