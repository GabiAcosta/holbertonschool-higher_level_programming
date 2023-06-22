#!/usr/bin/python3
"""Task 7"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
try:
    new_list = load_from_json_file(filename)
except Exception as e:
    new_list = []
if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv[1:]):
        new_list.append(arg)

save_to_json_file(new_list, filename)
