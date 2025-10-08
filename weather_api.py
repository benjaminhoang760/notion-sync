import requests, json, argparse, certifi

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url, timeout=10, verify=certifi.where())
    response.raise_for_status()
    return response.json()["current_weather"]

def main():
    parser = argparse.ArgumentParser(description="Fetch real weather data")
    parser.add_argument("--lat", type=float, default=10.7769, help="Latitude (default: Ho Chi Minh City)")
    parser.add_argument("--lon", type=float, default=106.7009, help="Longitude (default: Ho Chi Minh City)")
    args = parser.parse_args()

    data = get_weather(args.lat, args.lon)
    print(json.dumps(data, indent=2))
    print(f"\nTemperature: {data['temperature']}°C | Windspeed: {data['windspeed']} km/h")

if __name__ == "__main__":
    main()
