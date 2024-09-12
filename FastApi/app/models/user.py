"""user model module.

This module defines the User model using Pydantic for data validation.
"""

from pydantic import BaseModel


class User(BaseModel):
    """User model

    This model defines the structure and attributes of a user entity.

    Attributes:
        id (int): A unique identifier for the user. Typically, this would be assigned by the database.
        username (str): The username chosen by the user. This should be unique within the system.
        email (str): The user's email address. Email validation can be added later if necessary.
        password (str): The user's password. In practice, this should be stored as a hash rather than plain text.
    """

    id: int
    username: str
    email: str
    password: str
