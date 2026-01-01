from pytrends.request import TrendReq
import pandas as pd

# Connect to Google Trends
pytrends = TrendReq(hl='en-US', tz=330)

# Keywords used in the project
keywords = ["football", "cricket", "basketball"]

# Time period (older range)
timeframe = "2008-01-01 2024-12-31"

# Search types available in Google Trends
search_types = {
    "web": "",
    "youtube": "youtube",
    "image": "images",
    "news": "news",
    "shopping": "froogle"
}

all_data = []

for search_name, gprop in search_types.items():
    pytrends.build_payload(
        kw_list=keywords,
        timeframe=timeframe,
        geo="",       # empty = worldwide
        gprop=gprop   # search type
    )
    
    data = pytrends.interest_over_time()
    
    if not data.empty:
        data = data.drop(columns=["isPartial"])
        data["search_type"] = search_name
        all_data.append(data)

# Combine all search types into one DataFrame
final_df = pd.concat(all_data)

# Save to CSV
final_df.to_csv("google_trends_sports_data.csv")

print("Data extraction completed successfully!")



from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=330)

keywords = ["football", "cricket", "basketball"]
timeframe = "2008-01-01 2024-12-31"

# Countries to analyze
countries = {
    "India": "IN",
    "United States": "US",
    "United Kingdom": "GB",
    "Australia": "AU"
}

search_types = {
    "web": "",
    "youtube": "youtube",
    "image": "images",
    "news": "news",
    "shopping": "froogle"
}

all_data = []

for country_name, geo_code in countries.items():
    for search_name, gprop in search_types.items():
        
        pytrends.build_payload(
            kw_list=keywords,
            timeframe=timeframe,
            geo=geo_code,
            gprop=gprop
        )
        
        data = pytrends.interest_over_time()
        
        if not data.empty:
            data = data.drop(columns=["isPartial"])
            data["country"] = country_name
            data["search_type"] = search_name
            all_data.append(data)

final_df = pd.concat(all_data)
final_df.to_csv("google_trends_countrywise_sports.csv")

print("Country-wise data extraction completed!")

