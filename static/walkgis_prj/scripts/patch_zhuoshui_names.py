
import json
import os
import re

JSON_PATH = "../data/20260111_zhuoshui_facilities.json"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ABS_JSON_PATH = os.path.join(SCRIPT_DIR, JSON_PATH)

def is_garbage(text):
    # Detects common mojibake/PUA characters seen in this dataset
    # PUA range E000-F8FF
    # Stick to PUA only to avoid false positives like '風'
    
    for char in text:
        cp = ord(char)
        if 0xE000 <= cp <= 0xF8FF:
            return True
            
    return False

def main():
    if not os.path.exists(ABS_JSON_PATH):
        print(f"Not found: {ABS_JSON_PATH}")
        return
        
    with open(ABS_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    count = 0
    dike_counter = 1
    
    new_data = []
    for item in data:
        name = item['name']
        if is_garbage(name):
            # Assume it's a segment of the Centennial Dike
            new_name = f"百年舊堤_路段_{str(dike_counter).zfill(2)}"
            print(f"Renaming garbage '{name}' -> '{new_name}'")
            item['name'] = new_name
            dike_counter += 1
            count += 1
        new_data.append(item)
        
    if count > 0:
        with open(ABS_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
        print(f"Patched {count} items.")
    else:
        print("No garbage found.")

if __name__ == "__main__":
    main()
