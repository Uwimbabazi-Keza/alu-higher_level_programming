#!/usr/bin/python3
"""Module contains Base class"""

import json


class Base:
    """
    manage id attribute in all your future classes
    and to avoid duplicating the same code
    """

    __nb_objects = 0
    
    def __init__(self, id=None):
        """ Initialize """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON rep of a
        list of objects to a file
        """
        f = cls.__name__ + ".json"
        with open(f, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dictionaries))
     
    @staticmethod
    def from_json_string(json_string):
        """Returns reversed format of JSON string"""
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instances with default attributes
        """
        if cls.__name__ == "Rectangle":
            random_inst = cls(3, 2)
        elif cls.__name__ == "Square":
            random_inst = cls(3)
        random_inst.update(**dictionary)
        return random_inst
    
    @classmethod
    def load_from_file(cls):
        """returns list of instances
        """
        f = str(cls.__name__) + ".json"
        try:
            with open(f, "r") as file:
                list_dictionaries = Base.from_json_string(file.read())
                return [cls.create(**dic) for dic in list_dictionaries]
        except FileNotFoundError:
            return []
