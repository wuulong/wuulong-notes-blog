
import requests
import json
import time
import os

# Configuration
GOOGLE_API_KEY = 'AIzaSyDrrfcQvb-E1Kogk34QfAq2VFyGBeejNT4'
OUTPUT_FILE = '/Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/static/walkgis_prj/data/2026_zhuoshui_river_pois.json'

# Center of Search (Nantou/Central Taiwan) to bias results
CENTER_LAT = 23.8
CENTER_LON = 120.9
RADIUS = 50000 # 50km radius to cover the basin

POI_LIST = [
    {"category": "自然地景-源頭與山岳", "name": "佐久間鞍部"},
    {"category": "自然地景-源頭與山岳", "name": "合歡山主峰"},
    {"category": "自然地景-源頭與山岳", "name": "合歡山東峰"},
    {"category": "自然地景-源頭與山岳", "name": "集集大山"},
    {"category": "自然地景-水文/濕地", "name": "瑞龍瀑布"},
    {"category": "自然地景-水文/濕地", "name": "日月潭"},
    {"category": "自然地景-水文/濕地", "name": "草嶺潭"},
    {"category": "自然地景-水文/濕地", "name": "濁水溪出海口"},
    {"category": "自然地景-水文/濕地", "name": "雙龍瀑布"},
    {"category": "自然地景-地質", "name": "金門峒斷崖"},
    {"category": "自然地景-地質", "name": "濁水溪沖積扇"},
    {"category": "水利設施-壩堰", "name": "武界壩"},
    {"category": "水利設施-壩堰", "name": "霧社水庫"},
    {"category": "水利設施-壩堰", "name": "集集攔河堰"},
    {"category": "水利設施-圳路", "name": "八堡圳取水口"},
    {"category": "水利設施-圳路", "name": "莿仔埤圳"},
    {"category": "水利設施-圳路", "name": "斗六大圳"},
    {"category": "水利設施-圳路", "name": "觸口引水道"},
    {"category": "水利設施-電廠", "name": "大觀發電廠"},
    {"category": "交通設施-橋樑", "name": "西螺大橋"},
    {"category": "交通設施-橋樑", "name": "溪州大橋"},
    {"category": "交通設施-橋樑", "name": "自強大橋"},
    {"category": "交通設施-橋樑", "name": "中沙大橋"},
    {"category": "交通設施-橋樑", "name": "西濱大橋"},
    {"category": "交通設施-橋樑", "name": "龍神橋"},
    {"category": "交通設施-橋樑", "name": "雙龍七彩吊橋"},
    {"category": "交通設施-橋樑", "name": "名竹大橋"},
    {"category": "交通設施-橋樑", "name": "孫海橋"},
    {"category": "交通設施-橋樑", "name": "糯米橋"},
    {"category": "交通設施-車站", "name": "集集火車站"},
    {"category": "人文史蹟-古蹟/建築", "name": "林先生廟"},
    {"category": "人文史蹟-古蹟/建築", "name": "竹山社寮敬聖亭"},
    {"category": "人文史蹟-古蹟/建築", "name": "西螺振文書院"},
    {"category": "人文史蹟-古蹟/建築", "name": "明新書院"},
    {"category": "人文史蹟-古蹟/建築", "name": "八通關古道"},
    {"category": "人文史蹟-古蹟/建築", "name": "詔安客家文化館"},
    {"category": "人文史蹟-宗教信仰", "name": "西螺福興宮"},
    {"category": "人文史蹟-宗教信仰", "name": "西螺廣福宮"},
    {"category": "人文史蹟-宗教信仰", "name": "麥寮拱範宮"},
    {"category": "人文史蹟-宗教信仰", "name": "紫南宮"},
    {"category": "人文史蹟-聚落(原民)", "name": "武界部落"},
    {"category": "人文史蹟-聚落(原民)", "name": "萬豐部落"},
    {"category": "人文史蹟-聚落(原民)", "name": "過坑部落"},
    {"category": "人文史蹟-聚落(原民)", "name": "雙龍部落"},
    {"category": "人文史蹟-聚落(漢人)", "name": "北斗鎮"},
    {"category": "人文史蹟-聚落(漢人)", "name": "竹山鎮"},
    {"category": "人文史蹟-聚落(漢人)", "name": "水里鄉"},
    {"category": "人文史蹟-聚落(漢人)", "name": "麥寮鄉"},
    {"category": "災害與環境", "name": "車籠埔斷層保存園區"} # Adjusted for better search
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
            # Return the first result
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
        print(f"Searching: {poi['name']}...", end='', flush=True)
        data = search_google_places(poi['name'])
        
        if data['found']:
            print(f" Found: {data['name']}")
            poi_data = poi.copy()
            poi_data.update(data)
            results.append(poi_data)
        else:
            print(" Not Found.")
            # Keep original with empty coords or handle downstream
            poi_data = poi.copy()
            poi_data['found'] = False
            results.append(poi_data)
        
        time.sleep(0.5) # Throttle

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"Done. Saved {len(results)} items to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
