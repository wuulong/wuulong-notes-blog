---
description: 從景點清單自動建立 WalkGIS 地圖的全流程 (搜尋 -> MD enrichment -> DB -> Image Gen -> KML) - v3 (20260111 Updated)
---

# Create WalkGIS Map from List

This task automates the creation of a full WalkGIS map package, now including content enrichment and AI image generation.

## 0. Prerequisites
- **Python Environment**: Ensure you are using the correct Conda environment (e.g., `m2504`).
- **API Keys**: Ensure `GOOGLE_MAPS_API_KEY` (for Places) and Image Generation tools are available.

## 1. Input Collection & Strategy
- **Ask the user** for the **"Map Name"** and **"List of Locations"**.
- **Categorization**: Use the 5 dimensions: Nature, Water Infrastructure, Culture, Transport, Disaster.
- **ID Convention**: `YYYYMMDD_map_name_english` (Map) and `YYYYMMDD_map_name_XX_poi_name` (Feature).

## 2. Research & initial Data
- **Tool**: Use `search_web` or Google Places API script to get GPS coordinates.
- **Output**: A JSON file (e.g., `data/YYYY_map_pois.json`) containing the basic list with coordinates.
- **Validation**: Check for coordinate errors (e.g., wrong county) and patch if necessary.

## 3. Map & Feature Generation (Python Script)
- **Script**: Create/Update `scripts/create_{map_id}.py`.
- **Database Interaction**: Connect to `walkgis.db` directly. Manage Layers (`get_or_create_layer`) and use WKT geometry.
- **Markdown Generation**: Generate initial Feature Markdown files and the Map Markdown (with Mermaid graph).
- **Deep Research Prompt**: Ensure the Map Markdown includes a **complete list** of POIs in the Deep Research Prompt section.

## 4. Content Enrichment (The "Thick" Markdown)
- **Goal**: Transform thin placeholder Markdowns into rich content.
- **Action**:
  - Iterate through each generated Feature Markdown.
  - Perform **Web Search** for each POI to find: 簡介 (Introduction), 歷史 (History), 特色 (Features), 基本資訊 (Basic Info).
  - **Batch Update**: Use a script (e.g., `enrich_features_{map_id}.py`) to inject this rich content into the Markdown files. Do NOT leave them as placeholders.

## 5. Visual Enhancement
- **Cover Image Generation**:
  - Use `generate_image` (Nano Banana) to create a thematic cover image for the map.
  - Prompt should reflect the map's theme (e.g., "Irrigation canals in Taiwan, lush green, mountains in background").
  - Save to `assets/images/{map_id}_cover.png`.
  - Update `walking_maps` table and Map Markdown frontmatter with the new image path.

## 6. Artifact Export
- **NotebookLM Context**: Run `scripts/gen_notebooklm_context.sh {map_id}`.
- **KML & Navigation**: Run `scripts/export_{map_id}.py` to generate KML and Google Maps Links.

## 7. Final Report
- Summarize Map ID, Feature Count, Key Artifact Paths (Context, KML, Cover Image), and Navigation Link.
