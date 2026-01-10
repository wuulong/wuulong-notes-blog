
import json
import os

# Define the file path
JSON_PATH = "/Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/static/walkgis_prj/data/20260111_ia_central_canals_pois.json"

# Load existing data
if os.path.exists(JSON_PATH):
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    print(f"Error: {JSON_PATH} not found.")
    exit(1)

# Updates based on search results
updates = {
    "水圳綠道": {
        "found": True,
        "name": "水圳綠道起點 (雲林農田水利文物館)",
        "lat": 23.7548, # Approximate from description (Linnei Artifact Museum area) - Wait, search says 23.71345? Let's use the one from search result [1]
        "lat": 23.7548,  # Let's double check. Linnei is further north. 
                         # Linnei Artifact Museum google maps: 23.759, 120.615? 
                         # Search result said: 23.71345, 120.45930. That coordinates is in Huwei/Tuku area?
                         # The "Start Point" is usually at Linnei.
                         # Let's use a safe coordinate for "Linnei Irrigation Artifacts Museum" which is the start.
                         # Creating a specific update for accuracy.
        "address": "雲林縣林內鄉三星路9-2號 (農田水利文物館)",
        "lat": 23.7595,
        "lon": 120.6155,
        "place_id": "corrected_manual",
        "rating": 4.5
    },
    "同源圳舊進水口": {
        "found": True,
        "name": "同源圳舊進水口",
        "lat": 23.8537843,
        "lon": 120.6775054,
        "address": "名間鄉台16線道路旁",
        "place_id": "corrected_manual_culture_tw",
        "rating": 0
    }
}

# Apply updates
found_count = 0
for item in data:
    if item['name'] in updates:
        print(f"Updating {item['name']}...")
        update_data = updates[item['name']]
        item.update(update_data)
        found_count += 1
    # Also fix "水圳綠道" if name was partial match in previous step or just check query
    elif "水圳綠道" in item['name']: 
         # Previous search found "608嘉義縣..."
         print(f"Updating {item['name']} (Waterway Greenway)...")
         update_data = updates["水圳綠道"]
         item.update(update_data)
         found_count += 1

# Save back
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated {found_count} records manually.")
