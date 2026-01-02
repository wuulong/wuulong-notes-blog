import os
import zipfile
import uuid
import ast
import glob

# Configuration
BASE_DIR = "/Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/static/walkgis_prj"
FEATURES_DIR = os.path.join(BASE_DIR, "features")
OUTPUT_DIR = os.path.join(BASE_DIR, "atak_packages")
PACKAGE_NAME = "daan_dajia_pipeline_mission_package"
KML_FILENAME = "daan_dajia_pipeline.kml"

def parse_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_raw = parts[1]
            body = parts[2]
            
            metadata = {}
            for line in frontmatter_raw.strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    # Handle basic arrays and strings usually found in fontmatter
                    if value.startswith('[') and value.endswith(']'):
                         try:
                             # Try to evaluate as a list
                             # This handles tags: [a, b] etc.
                             # But for coordinates [Lat, Lon], we might want to keep it simple or parse carefully
                             # Because yaml allows [a, b], python list is similar but strings need quotes.
                             # Our files seem to use [24.x, 120.x] which is valid python
                             # The path coordinates [(lat, lon), ...] might trigger syntax error if not standard list
                             # Let's try ast.literal_eval but be careful
                             if '(' in value: # It's a list of tuples likely
                                  metadata[key] = ast.literal_eval(value) 
                             else:
                                  # might be tags like [tag1, tag2] which aren't quoted strings in yaml often
                                  # Quick hack for tags
                                  clean_val = value[1:-1]
                                  metadata[key] = [x.strip() for x in clean_val.split(',')]
                         except:
                             metadata[key] = value
                    else:
                        # string or number
                        metadata[key] = value.strip('"').strip("'")
            return metadata, body
    return None, None

def generate_kml(features):
    kml_header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>大安大甲溪聯通管工程計畫</name>
    <description>大安大甲溪聯通管工程計畫 ATAK Data Package</description>
    <Style id="redLine">
      <LineStyle>
        <color>ff0000ff</color>
        <width>4</width>
      </LineStyle>
    </Style>
    <Style id="pointStyle">
        <IconStyle>
            <scale>1.1</scale>
        </IconStyle>
    </Style>
"""
    kml_footer = """  </Document>
</kml>
"""
    kml_body = ""

    for feature in features:
        name = feature.get('title', 'Unknown')
        
        # Determine geometry
        if 'coordinate' in feature:
            # Point
            # Expecting string like "[24.2797, 120.7691]" or list
            coords = feature['coordinate']
            if isinstance(coords, str):
                 # simplify cleanup [ ]
                 coords = coords.replace('[', '').replace(']', '').split(',')
            
            # KML expects "lon,lat"
            lat = float(coords[0])
            lon = float(coords[1])
            
            kml_body += f"""    <Placemark>
      <name>{name}</name>
      <styleUrl>#pointStyle</styleUrl>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>
"""
        elif 'coordinates' in feature:
            # LineString (Path)
            # Expecting string like "[(24.2797, 120.7691), (24.282, 120.76), ...]" or list of tuples
            raw_coords = feature['coordinates']
            # Convert to KML coordinate string "lon,lat,0 lon,lat,0 ..."
            
            coord_str_list = []
            if isinstance(raw_coords, list):
                for p in raw_coords:
                     if isinstance(p, tuple) or isinstance(p, list):
                         coord_str_list.append(f"{p[1]},{p[0]},0")
            
            kml_coord_str = " ".join(coord_str_list)

            kml_body += f"""    <Placemark>
      <name>{name}</name>
      <styleUrl>#redLine</styleUrl>
      <LineString>
        <tessellate>1</tessellate>
        <coordinates>
          {kml_coord_str}
        </coordinates>
      </LineString>
    </Placemark>
"""

    return kml_header + kml_body + kml_footer

def generate_manifest(uid, name, kml_file_path):
    # kml_file_path is relative to the zip root
    return f"""<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<MissionPackageManifest version="2">
  <Configuration>
    <Parameter name="name" value="{name}" />
    <Parameter name="uid" value="{uid}" />
    <Parameter name="version" value="1" />
    <Parameter name="onReceiveAction" value="import" />
  </Configuration>
  <Contents>
    <Content ignore="false" zipEntry="{kml_file_path}" />
  </Contents>
</MissionPackageManifest>
"""

def main():
    # 1. Collect Data
    pattern = os.path.join(FEATURES_DIR, "20260101_daan_dajia_pipeline_*.md")
    files = glob.glob(pattern)
    print(f"Found {len(files)} files.")
    
    features = []
    for fpath in files:
        meta, _ = parse_frontmatter(fpath)
        if meta:
            features.append(meta)
    
    # 2. Generate KML
    kml_content = generate_kml(features)
    kml_path = os.path.join(OUTPUT_DIR, KML_FILENAME)
    
    with open(kml_path, 'w', encoding='utf-8') as f:
        f.write(kml_content)
    print(f"Generated KML at {kml_path}")
    
    # 3. Generate Manifest
    pkg_uid = str(uuid.uuid4())
    manifest_content = generate_manifest(pkg_uid, "大安大甲溪聯通管工程", KML_FILENAME)
    
    # 4. Create Zip
    zip_path = os.path.join(OUTPUT_DIR, f"{PACKAGE_NAME}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zf:
        # Add KML
        zf.write(kml_path, arcname=KML_FILENAME)
        # Add Manifest
        zf.writestr('MANIFEST/manifest.xml', manifest_content)
        
    print(f"Created ATAK Data Package at {zip_path}")

if __name__ == "__main__":
    main()
