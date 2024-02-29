#!/usr/bin/python3
"""This module defines class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits From BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
