
import zipfile
import os

KMZ_PATH = "/Users/wuulong/github/bmad-pa/events/notes/data/濁水溪景點設施.kmz"

def main():
    with zipfile.ZipFile(KMZ_PATH, 'r') as z:
        kml_filename = [n for n in z.namelist() if n.endswith('.kml')][0]
        with z.open(kml_filename) as f:
            raw_bytes = f.read()
            
            # Print start of file to check encoding declaration
            print("--- Head (200 bytes) ---")
            print(raw_bytes[:200])
            
            # Try to find a known name or the problematic area
            # problematic: "偌"
            # It's hard to find without search. 
            # Let's search for "LineString" and look around it.
            
            try:
                idx = raw_bytes.find(b'LineString')
                if idx != -1:
                    # Look slightly before for <name>
                    start_look = max(0, idx - 200)
                    chunk = raw_bytes[start_look:idx+50]
                    print(f"\n--- Chunk around LineString ({idx}) ---")
                    print(chunk)
                    
                    # Try to decode this chunk as big5
                    try:
                        print("\n--- Decoded as CP950 (Big5) ---")
                        print(chunk.decode('cp950', errors='replace'))
                    except:
                        print("Failed to decode as cp950")
                        
                    # Try to decode as utf-8
                    try:
                        print("\n--- Decoded as UTF-8 ---")
                        print(chunk.decode('utf-8', errors='replace'))
                    except:
                        print("Failed to decode as utf-8")
                        
            except Exception as e:
                print(e)
                
if __name__ == "__main__":
    main()
