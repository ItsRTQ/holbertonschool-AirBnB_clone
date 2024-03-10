#!/usr/bin/python3
"""This is module runs as soon as the instance is created"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
