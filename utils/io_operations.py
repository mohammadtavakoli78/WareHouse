import json

"""
The ReadInputFiles Class reads input files
"""


class ReadInputFiles:
    def __init__(self):
        pass

    """
    This function reads input files and get json object
    @:returns json object
    """
    @staticmethod
    def read_file(path: str = ""):
        input_file = open(path)
        input_object = json.load(input_file)
        return input_object
