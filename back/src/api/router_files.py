from fastapi import APIRouter, Body, Depends, HTTPException, BackgroundTasks
import os
from src.settings import settings
import fileinput
import json

router = APIRouter()

@router.get("/log_tree")
async def get_log_tree():
    return  get_files_and_dirs(settings.LOG_PATH)

def get_files_and_dirs(path):
    result = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            result.append({
                "name": item,
                "type": "dir",
                "children": get_files_and_dirs(full_path)  # Рекурсивный вызов для подкаталогов
            })
        else:
            result.append({
                "name": item,
                "type": "file"
            })
    return result

@router.get("/log_file")
async def get_log_file(path:str):
    return  get_file_array_json(settings.LOG_PATH+path)

def get_file_array_json(path):
    res = {
        "log": []
    }
    with open(path, 'r',encoding='utf-8') as source, open(path, 'r') as filtered:
        for line in source:
            res["log"].append(json.loads(line)) 

    return res
