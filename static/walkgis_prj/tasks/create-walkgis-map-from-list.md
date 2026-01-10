---
description: 從景點清單自動建立 WalkGIS 地圖的全流程 (搜尋 -> MD -> DB -> NotebookLM -> KML) - v2 (20260111 Updated)
---

# Create WalkGIS Map from List

This task automates the creation of a full WalkGIS map package from a simple list of location names.

## 0. Prerequisites
- **Python Environment**: Ensure you are using the correct Conda environment (e.g., `m2504`).
  - Command: `/Users/wuulong/opt/anaconda3/envs/m2504/bin/python` or `conda run -n m2504 python`.
- **Google Maps API**: Ensure `GOOGLE_MAPS_API_KEY` is available for `search_google_places` scripts.

## 1. Input Collection & Strategy
- **Ask the user** for the **"Map Name"**.
- **Ask the user** for the **"List of Locations"**.
- **Categorization Strategy (The 5 Dimensions)**:
  - Encourage classifying POIs into these categories for better GIS layering:
    1. **自然 (Nature)**: 山岳、地質、瀑布、濕地。
    2. **水利 (Water Infrastructure)**: 水庫、壩堰、圳路、電廠。
    3. **人文 (Culture/History)**: 聚落、古蹟、廟宇、歷史事件。
    4. **交通 (Transport)**: 橋樑、車站、古道。
    5. **災害 (Disaster/Env)**: 斷層、地層下陷、易淹水區。
- **Define IDs**:
  - **Map ID**: MUST use `YYYYMMDD_map_name_english` (e.g., `20260111_zhuoshui_river`).
  - **Feature ID**: MUST use `YYYYMMDD_map_name_XX_poi_name` (e.g., `20260111_zhuoshui_river_01_hehuanshan`).

## 2. Research & Enrichment
- **Tool**: Use `search_web` or a Google Places API script.
- **Goal**: Get **GPS Coordinates**, **Address**, **Rating**, and **Place ID**.
- **Output**: A JSON file (e.g., `data/YYYY_map_pois.json`) containing the enriched list.

## 3. Map & Feature Generation (Python Script)
- Create/Update a Python script (e.g., `scripts/create_{map_id}.py`).
- **CRITICAL: Database Interaction**:
  - Do NOT just generate a SQL file blindly.
  - **Connect to SQLite** (`walkgis.db`) directly in the script.
  - **Layer Management**:
    - Check if the required Layer (Category) exists in the `layers` table.
    - If not, INSERT it and get the new `layer_id`.
  - **Schema Compliance**:
    - Table `walking_maps`: `map_id`, `name`, `description`, `region`.
    - Table `walking_map_features`: `feature_id`, `name`, `geometry_wkt` (POINT(lon lat)), `layer_id`.
    - Table `walking_map_relations`: Link maps and features.
- **Markdown Generation**:
  - Generate standard Frontmatter Markdown files in `features/`.
  - Generate the Map Markdown in `maps/` with a Mermaid graph.

## 4. Execution & Validation
- Run the generation script using the correct Python path.
- **Verify**:
  - Check `walkgis.db` for new records.
  - Check `features/*.md` files exist.

## 5. Artifact Generation
- **NotebookLM Context**:
  - Run `scripts/gen_notebooklm_context.sh {map_id}`.
- **KML & Navigation**:
  - Run an export script (e.g., `scripts/export_{map_id}.py`) to generate KML and Google Maps Links.
  - **Note**: Google Maps URL has a length limit; for >20 points, consider splitting or just showing the KML.

## 6. Final Report
- Summarize:
  - Map ID & Name.
  - Number of Features created.
  - Path to NotebookLM Context (for RAG).
  - Path to KML (for visual).
  - Sample Navigation Link.
