#!/usr/bin/python3
"""File executed when module from package is imported"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
