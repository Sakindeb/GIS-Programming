import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os
import time
from datetime import datetime

# Configuration
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://transit.land/api/v2/rest"
OUTPUT_DIR = "transit_data"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_all_pages(endpoint, params=None):
    """Fetch all pages of data from a paginated API endpoint"""
    if params is None:
        params = {}
    
    params["apikey"] = API_KEY
    all_data = []
    next_url = f"{BASE_URL}/{endpoint}"
    
    print(f"Fetching data from {endpoint}...")
    page = 1
    
    while next_url:
        print(f"  Fetching page {page}...")
        response = requests.get(next_url, params=params if "?" not in next_url else None)
        
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            print(response.text)
            break
        
        data = response.json()
        
        # Get the items based on endpoint
        if endpoint == "stops":
            all_data.extend(data["stops"])
        elif endpoint == "routes":
            all_data.extend(data["routes"])
        
        # Check if there's a next page
        if "meta" in data and "next" in data["meta"]:
            next_url = data["meta"]["next"]
            params = {}  # Clear params as they're included in the next URL
        else:
            next_url = None
        
        page += 1
        time.sleep(0.5)  # Be nice to the API
    
    print(f"Fetched {len(all_data)} records from {endpoint}")
    return all_data

def process_stops(stops_data):
    """Process stops data into a GeoDataFrame"""
    stops_list = []
    
    for stop in stops_data:
        try:
            # Extract geometry
            coords = stop.get("geometry", {}).get("coordinates", [None, None])
            if None in coords or len(coords) < 2:
                continue
                
            # Extract place data
            place_data = stop.get("place", {})
            
            stops_list.append({
                "stop_id": stop.get("stop_id"),
                "onestop_id": stop.get("onestop_id"),
                "stop_name": stop.get("stop_name"),
                "longitude": coords[0],
                "latitude": coords[1],
                "country": place_data.get("adm0_name"),
                "region": place_data.get("adm1_name"),
                "wheelchair_accessible": stop.get("wheelchair_boarding") == 1,
                "feed_version_id": stop.get("feed_version", {}).get("id"),
                "feed_onestop_id": stop.get("feed_version", {}).get("feed", {}).get("onestop_id")
            })
        except Exception as e:
            print(f"Error processing stop: {e}")
    
    # Create DataFrame
    stops_df = pd.DataFrame(stops_list)
    
    # Convert to GeoDataFrame
    stops_gdf = gpd.GeoDataFrame(
        stops_df, 
        geometry=[Point(xy) for xy in zip(stops_df.longitude, stops_df.latitude)],
        crs="EPSG:4326"
    )
    
    return stops_gdf

def process_routes(routes_data):
    """Process routes data into a DataFrame"""
    routes_list = []
    
    for route in routes_data:
        try:
            # Get agency info
            agency = route.get("agency", {})
            
            routes_list.append({
                "route_id": route.get("route_id"),
                "onestop_id": route.get("onestop_id"),
                "route_short_name": route.get("route_short_name"),
                "route_long_name": route.get("route_long_name"),
                "route_type": route.get("route_type"),
                "route_color": route.get("route_color"),
                "agency_name": agency.get("agency_name"),
                "agency_onestop_id": agency.get("onestop_id"),
                "feed_version_id": route.get("feed_version", {}).get("id"),
                "feed_onestop_id": route.get("feed_version", {}).get("feed", {}).get("onestop_id")
            })
        except Exception as e:
            print(f"Error processing route: {e}")
    
    # Create DataFrame
    routes_df = pd.DataFrame(routes_list)
    
    return routes_df

def join_data(stops_gdf, routes_df):
    """Join stops and routes data through their feed versions"""
    # This is a simplified join based on feed IDs
    # A more complete join would use the `operated_by` and `served_by` endpoints
    # or fetch the stop_times data to connect routes to stops
    
    # For this simple example, we'll just add feed information to help with later joining
    return stops_gdf, routes_df

def save_data(stops_gdf, routes_df):
    """Save processed data to files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save to GeoJSON and CSV
    stops_file = f"{OUTPUT_DIR}/transit_stops_{timestamp}.geojson"
    routes_file = f"{OUTPUT_DIR}/transit_routes_{timestamp}.csv"
    
    stops_gdf.to_file(stops_file, driver="GeoJSON")
    routes_df.to_csv(routes_file, index=False)
    
    print(f"Saved stops data to {stops_file}")
    print(f"Saved routes data to {routes_file}")
    
    return stops_file, routes_file

def main():
    """Main ETL process"""
    print("Starting TransitLand ETL process...")
    
    # Extract data
    stops_data = fetch_all_pages("stops", {"limit": 100})
    routes_data = fetch_all_pages("routes", {"limit": 100})
    
    # Transform data
    stops_gdf = process_stops(stops_data)
    routes_df = process_routes(routes_data)
    
    # Optional: Join data
    stops_gdf, routes_df = join_data(stops_gdf, routes_df)
    
    # Load (save) data
    stops_file, routes_file = save_data(stops_gdf, routes_df)
    
    print("\nETL process completed successfully!")
    print(f"Processed {len(stops_gdf)} stops and {len(routes_df)} routes")

if __name__ == "__main__":
    main()