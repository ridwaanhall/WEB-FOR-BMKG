from app import app
from flask import render_template, request
import requests, datetime, xmltodict
import xml.etree.ElementTree as ET

@app.route("/")
def index():
    #return 'Hello ridwaanhall'
    return render_template('main-base.html')

@app.route("/cuaca-diyogyakarta")
def cuaca_diyogyakarta():
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DIYogyakarta.xml'

    # Use the requests library to get the XML data from the URL
    response = requests.get(url)

    # Parse the XML data using the xmltodict library
    data = xmltodict.parse(response.text)

    # Extract the timestamp
    timestamp = data['data']['forecast']['issue']['timestamp']

    # Extract the year, month, day, hour, minute, and second
    year = data['data']['forecast']['issue']['year']
    month = data['data']['forecast']['issue']['month']
    day = data['data']['forecast']['issue']['day']
    hour = data['data']['forecast']['issue']['hour']
    minute = data['data']['forecast']['issue']['minute']
    second = data['data']['forecast']['issue']['second']

    # Extract the information you need
    forecast_areas = data['data']['forecast']['area']

    areas = []
    if isinstance(forecast_areas, list):
        for area in forecast_areas:
            area_id = area['@id']
            description = area['@description']
            latitude = area['@latitude']
            longitude = area['@longitude']
            coordinate = area['@coordinate']
            area_type = area['@type']
            level = area['@level']
            domain = area['@domain']

            areas.append({
                "id": area_id,
                "description": description,
                "latitude": latitude,
                "longitude": longitude,
                "coordinate": coordinate,
                "type": area_type,
                "level": level,
                "domain": domain
            })
    elif isinstance(forecast_areas, dict):
        # If there is only one area, convert it to a list for consistent handling
        area = forecast_areas
        area_id = area['@id']
        description = area['@description']
        latitude = area['@latitude']
        longitude = area['@longitude']
        coordinate = area['@coordinate']
        area_type = area['@type']
        level = area['@level']
        domain = area['@domain']

        areas.append({
            "id": area_id,
            "description": description,
            "latitude": latitude,
            "longitude": longitude,
            "coordinate": coordinate,
            "type": area_type,
            "level": level,
            "domain": domain
        })

    # Render the template with the extracted data and timestamp
    print(areas)
    return render_template('main-diyogyakarta.html', data=areas, timestamp=timestamp, year=year, month=month, day=day, hour=hour, minute=minute, second=second)
