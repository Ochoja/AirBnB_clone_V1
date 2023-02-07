#!/usr/bin/python3
import uuid, datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, id, created_at, updated_at):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at
