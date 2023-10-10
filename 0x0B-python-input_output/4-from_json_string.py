#!/usr/bin/python3
"""
Contains "from_json_string" function
"""

import json


def from_json_string(my_str):
    """returns object represented by the JSON string"""
    return json.loads(my_str)
