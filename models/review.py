#!/usr/bin/python3
"""Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Lodge Review Data"""
    place_id = ""
    user_id = ""
    text = ""
