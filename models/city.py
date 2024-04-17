#!/usr/bin/python3
"""Defines City class module """

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel
        Args:

        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """

    state_id = ""
    name = ""
