#!/usr/bin/python3
"""serializes instances to a JSON file and
    deserializes JSON file to instances
    """
import json as j
from models.base_model import BaseModel as BM


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dic = FileStorage.__objects
        all_obj = {obj: obj_dic[obj].to_dict() for obj in obj_dic.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            j.dump(all_obj, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = j.load(f)
        except FileNotFoundError:
            pass
