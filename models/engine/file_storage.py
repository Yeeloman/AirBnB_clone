#!/usr/bin/python3
"""serializes instances to a JSON file and
    deserializes JSON file to instances
    """
import json as j
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dic = FileStorage.__objects
        all_obj = {obj: obj_dic[obj].to_dict() for obj in obj_dic.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            j.dump(all_obj, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dic = j.load(f)
                for obj in obj_dic.values():
                    clsName = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(clsName)(**obj))
        except FileNotFoundError:
            return
