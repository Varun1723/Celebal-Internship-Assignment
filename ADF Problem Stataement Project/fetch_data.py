import requests
import os

# 1. List your countries
countries = ["india", "us", "uk", "china", "russia"]

# 2. Ensure output folder exists
output_dir = "rest_data"
os.makedirs(output_dir, exist_ok=True)

# 3. Fetch each endpoint and save to <country>.json
for country in countries:
    url = f"https://restcountries.com/v3.1/name/{country}"
    print(f"Fetching {country}...", end=" ")
    resp = requests.get(url)
    resp.raise_for_status()  # will crash here if something goes wrong
    file_path = os.path.join(output_dir, f"{country}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(resp.text)
    print("done")
