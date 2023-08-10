import requests
import xmltodict
import json

# URL of the XML data
url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-diyogyakarta.xml"

# Make a GET request to the URL
response = requests.get(url)

# Parse the XML data into a dictionary
data_dict = xmltodict.parse(response.content)

# Convert the dictionary to JSON
json_data = json.dumps(data_dict)

# Print the JSON data
print(json_data)
