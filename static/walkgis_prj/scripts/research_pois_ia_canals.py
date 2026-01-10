
import requests
import json
import time
import os

# Configuration
GOOGLE_API_KEY = 'AIzaSyDrrfcQvb-E1Kogk34QfAq2VFyGBeejNT4'
OUTPUT_FILE = '/Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/static/walkgis_prj/data/20260111_ia_central_canals_pois.json'

# Center of Search (Central Taiwan) 
CENTER_LAT = 23.9
CENTER_LON = 120.6
RADIUS = 60000 

POI_LIST = [
    {"category": "水利設施-彰化管理處", "name": "八堡一圳員林市區段", "query": "八堡一圳 員林市"},
    {"category": "水利設施-彰化管理處", "name": "八堡圳 (用水管制中心)", "query": "彰化用水管制中心"},
    {"category": "水利設施-彰化管理處", "name": "同源圳舊進水口", "query": "同源圳舊進水口"},
    {"category": "水利設施-彰化管理處", "name": "東西三圳", "query": "東西三圳 員林 河濱路"},
    {"category": "水利設施-彰化管理處", "name": "義和制水閘", "query": "義和制水閘"},
    
    {"category": "水利設施-雲林管理處", "name": "斗六大圳進水口", "query": "斗六大圳進水口"},
    {"category": "水利設施-雲林管理處", "name": "水圳綠道", "query": "水圳綠道"},
    {"category": "水利設施-雲林管理處", "name": "林內2號進水口", "query": "林內2號進水口"},
    {"category": "水利設施-雲林管理處", "name": "林內分水工 (八卦池)", "query": "林內分水工 八卦池"},
    {"category": "水利設施-雲林管理處", "name": "後庄子埤", "query": "後庄子埤"},
    {"category": "水利設施-雲林管理處", "name": "新頂埤頭", "query": "新頂埤頭"},
    {"category": "水利設施-雲林管理處", "name": "濁幹線調蓄池", "query": "濁幹線調蓄池"},

    {"category": "水利設施-南投管理處", "name": "北圳步道", "query": "北圳步道"},
    {"category": "水利設施-南投管理處", "name": "阿罩霧一圳 (水車)", "query": "阿罩霧一圳 水車"},
    {"category": "水利設施-南投管理處", "name": "埔里南烘圳鳳雛公園", "query": "埔里南烘圳鳳雛公園"},
    {"category": "水利設施-南投管理處", "name": "農田水利教育園區 (土城工作站)", "query": "農田水利署南投管理處土城工作站"},
    {"category": "水利設施-南投管理處", "name": "頭社水庫", "query": "頭社水庫"},
    {"category": "水利設施-南投管理處", "name": "頭社水庫山龍坑吊橋", "query": "頭社水庫 山龍坑吊橋"}
]

def search_google_places(query):
    endpoint = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': query,
        'location': f"{CENTER_LAT},{CENTER_LON}",
        'radius': RADIUS,
        'key': GOOGLE_API_KEY,
        'language': 'zh-TW'
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'results' in data and len(data['results']) > 0:
            item = data['results'][0]
            return {
                'found': True,
                'name': item['name'],
                'lat': item['geometry']['location']['lat'],
                'lon': item['geometry']['location']['lng'],
                'address': item.get('formatted_address', ''),
                'rating': item.get('rating', 0),
                'place_id': item['place_id']
            }
        else:
            return {'found': False}
            
    except Exception as e:
        print(f"Error searching for {query}: {e}")
        return {'found': False, 'error': str(e)}

def main():
    results = []
    print(f"Start searching for {len(POI_LIST)} locations...")
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    for poi in POI_LIST:
        q = poi.get('query', poi['name'])
        print(f"Searching: {q}...", end='', flush=True)
        data = search_google_places(q)
        
        if data['found']:
            print(f" Found: {data['name']}")
            poi_data = poi.copy()
            poi_data.update(data)
            results.append(poi_data)
        else:
            print(" Not Found.")
            poi_data = poi.copy()
            poi_data['found'] = False
            results.append(poi_data)
        
        time.sleep(1.0) 

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"Done. Saved {len(results)} items to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
