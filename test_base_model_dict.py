#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage

my_model = BaseModel()
storage.new(my_model)
storage.save()
