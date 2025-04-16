import folium
import geopandas as gpd
import pandas as pd
import os

# Find the most recent data files
OUTPUT_DIR = "transit_data"
stops_files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith("transit_stops_") and f.endswith(".geojson")]
routes_files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith("transit_routes_") and f.endswith(".csv")]

if not stops_files:
    print("No stops data found. Run the ETL script first.")
    exit(1)

# Get the most recent files
most_recent_stops = max(stops_files)
most_recent_routes = max(routes_files) if routes_files else None

# Load the data
stops_gdf = gpd.read_file(os.path.join(OUTPUT_DIR, most_recent_stops))
routes_df = pd.read_csv(os.path.join(OUTPUT_DIR, most_recent_routes)) if most_recent_routes else None

# Create map
center = [stops_gdf.geometry.y.mean(), stops_gdf.geometry.x.mean()]
m = folium.Map(location=center, zoom_start=10)

# Add stops to the map
for _, row in stops_gdf.iterrows():
    # Define color based on wheelchair accessibility
    color = 'green' if row.wheelchair_accessible else 'red'
    
    # Create popup content
    popup_content = f"""
    <b>{row.stop_name}</b><br>
    ID: {row.stop_id}<br>
    {row.region or ''}, {row.country or ''}
    """
    
    # Add marker
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=5,
        color='black',
        weight=1,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=folium.Popup(popup_content, max_width=300)
    ).add_to(m)

# Save map
output_file = os.path.join(OUTPUT_DIR, "transit_map.html")
m.save(output_file)
print(f"Map saved to {output_file}")