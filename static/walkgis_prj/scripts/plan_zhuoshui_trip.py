
import sqlite3
import re
import os

DB_PATH = "events/notes/wuulong-notes-blog/static/walkgis_prj/walkgis.db"
MAP_ID = "20260111_zhuoshui_facilities"

def parse_lon(wkt):
    # POINT (120.xxxxx 23.xxxxx)
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+", wkt)
    if match:
        return float(match.group(1))
    return None

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = """
        SELECT f.name, f.geometry_wkt, l.description
        FROM walking_map_features f
        JOIN walking_map_relations r ON f.feature_id = r.feature_id
        LEFT JOIN layers l ON f.layer_id = l.layer_id
        WHERE r.map_id = ?
        ORDER BY f.feature_id -- Fetch all first, sort by lon in python
    """
    
    cursor.execute(query, (MAP_ID,))
    all_features = []
    
    for row in cursor.fetchall():
        name, wkt, category = row
        lon = parse_lon(wkt)
        if lon:
            all_features.append({
                "name": name,
                "lon": lon,
                "category": category
            })
            
    # Sort from West (Sea) to East (Mountain)
    all_features.sort(key=lambda x: x["lon"])
    
    total = len(all_features)
    print(f"Total features found: {total}")
    
    # Divide into 4 logical sections based on longitude clustering or just quadrants
    # Map is roughly 120.2 (Mailiao) to 121.2 (Hehuan)
    # Day 1: Estuary (Mailiao/Dacheng) -> ~120.4 (Xiluo?)
    # Day 2: Plains (Xiluo/Ershui) -> ~120.6 (Linnei/Zhushan)
    # Day 3: Hills (Jiji/Shuili) -> ~120.8 (Sun Moon Lake/Xinyi)
    # Day 4: Mountains (Xinyi/Hehuan) -> >121.0
    
    day1 = [f for f in all_features if f['lon'] < 120.40] # West of Xiluo Bridge approx
    day2 = [f for f in all_features if 120.40 <= f['lon'] < 120.65] # Xiluo to Linnei/Ershui
    day3 = [f for f in all_features if 120.65 <= f['lon'] < 120.85] # Jiji/Shuili
    day4 = [f for f in all_features if f['lon'] >= 120.85] # Deep mountains
    
    days = [day1, day2, day3, day4]
    
    for i, day_features in enumerate(days, 1):
        print(f"\n=== Day {i} ({len(day_features)} spots) ===")
        # Pick top 5 diverse spots (simple heuristic: just pick some distributed ones)
        # Actually just list first, middle, last to give an idea
        if not day_features:
            print("No features found in this range.")
            continue
            
        print(f"Range: {day_features[0]['lon']:.2f} - {day_features[-1]['lon']:.2f} E")
        
        # Select significant spots (User mentioned specific categories in previous turns, e.g. Dikes, Water gates, Sightseeing)
        # Let's show a mix.
        unique_names = []
        for f in day_features:
            if f['name'] not in unique_names:
                unique_names.append(f['name'])
                
        # Print a sample
        step = max(1, len(unique_names) // 10)
        for name in unique_names[::step]:
            print(f"- {name}")

if __name__ == "__main__":
    main()
