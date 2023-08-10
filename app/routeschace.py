from app import app
from flask import render_template, request
import requests, datetime, xmltodict
import xml.etree.ElementTree as ET

@app.route("/")
def index():
    #return 'Hello ridwaanhall'
    return render_template('main-base.html')

@app.route("/gempa-terbaru")
def gempa_terbaru():
    url = 'https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml'

    # Use the requests library to get the XML data from the URL
    response = requests.get(url)

    # Parse the XML data using the xmltodict library
    data = xmltodict.parse(response.text)

    # Extract the information you need
    gempa     = data['Infogempa']['gempa']
    
    tanggal   = gempa['Tanggal']
    jam       = gempa['Jam']
    datetime  = gempa['DateTime']
    point     = gempa['point']['coordinates']
    lintang   = gempa['Lintang']
    bujur     = gempa['Bujur']
    magnitude = gempa['Magnitude']
    kedalaman = gempa['Kedalaman']
    wilayah   = gempa['Wilayah']
    potensi   = gempa['Potensi']
    dirasakan = gempa['Dirasakan']
    shakemap  = gempa['Shakemap']

    # Render the template with the extracted data
    #print(data)
    return render_template('main-terbaru.html',
                           tanggal     = tanggal,
                           jam         = jam,
                           datetime    = datetime,
                           coordinates = point,
                           lintang     = lintang,
                           bujur       = bujur,
                           magnitude   = magnitude,
                           kedalaman   = kedalaman,
                           wilayah     = wilayah,
                           potensi     = potensi,
                           dirasakan   = dirasakan,
                           shakemap    = shakemap)

@app.route("/gempa-besar")
def gempa_besar():
    url = 'https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.xml'

    # Use the requests library to get the XML data from the URL
    response = requests.get(url)

    # Parse the XML data using the xmltodict library
    data = xmltodict.parse(response.text)

    # Extract the information you need
    gempa_list = data['Infogempa']['gempa']
    
    rows = []
    if isinstance(gempa_list, list):
        for gempa in gempa_list:
            tanggal   = gempa['Tanggal']
            jam       = gempa['Jam']
            datetime  = gempa['DateTime']
            point     = gempa['point']['coordinates']
            lintang   = gempa['Lintang']
            bujur     = gempa['Bujur']
            magnitude = gempa['Magnitude']
            kedalaman = gempa['Kedalaman']
            wilayah   = gempa['Wilayah']
            potensi   = gempa['Potensi']

            rows.append({
                "tanggal"     : tanggal,
                "jam"         : jam,
                "datetime"    : datetime,
                "coordinates" : point,
                "lintang"     : lintang,
                "bujur"       : bujur,
                "magnitude"   : magnitude,
                "kedalaman"   : kedalaman,
                "wilayah"     : wilayah,
                "potensi"     : potensi
            })
    elif isinstance(gempa_list, dict):
        # If there is only one gempa, convert it to a list for consistent handling
        gempa = gempa_list
        tanggal   = gempa['Tanggal']
        jam       = gempa['Jam']
        datetime  = gempa['DateTime']
        point     = gempa['point']['coordinates']
        lintang   = gempa['Lintang']
        bujur     = gempa['Bujur']
        magnitude = gempa['Magnitude']
        kedalaman = gempa['Kedalaman']
        wilayah   = gempa['Wilayah']
        potensi   = gempa['Potensi']

        rows.append({
            "tanggal"     : tanggal,
            "jam"         : jam,
            "datetime"    : datetime,
            "coordinates" : point,
            "lintang"     : lintang,
            "bujur"       : bujur,
            "magnitude"   : magnitude,
            "kedalaman"   : kedalaman,
            "wilayah"     : wilayah,
            "potensi"     : potensi
        })

    # Render the template with the extracted data
    #print(rows)
    return render_template('main-besar.html', data=rows)

@app.route("/gempa-dirasakan")
def gempa_dirasakan():
    url = 'https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.xml'

    # Use the requests library to get the XML data from the URL
    response = requests.get(url)

    # Parse the XML data using the xmltodict library
    data = xmltodict.parse(response.text)

    # Extract the information you need
    gempa_list = data['Infogempa']['gempa']
    
    rows = []
    if isinstance(gempa_list, list):
        for gempa in gempa_list:
            tanggal   = gempa['Tanggal']
            jam       = gempa['Jam']
            datetime  = gempa['DateTime']
            point     = gempa['point']['coordinates']
            lintang   = gempa['Lintang']
            bujur     = gempa['Bujur']
            magnitude = gempa['Magnitude']
            kedalaman = gempa['Kedalaman']
            wilayah   = gempa['Wilayah']
            dirasakan = gempa['Dirasakan']

            rows.append({
                "tanggal"     : tanggal,
                "jam"         : jam,
                "datetime"    : datetime,
                "coordinates" : point,
                "lintang"     : lintang,
                "bujur"       : bujur,
                "magnitude"   : magnitude,
                "kedalaman"   : kedalaman,
                "wilayah"     : wilayah,
                "dirasakan"   : dirasakan
            })
    elif isinstance(gempa_list, dict):
        # If there is only one gempa, convert it to a list for consistent handling
        gempa = gempa_list
        tanggal   = gempa['Tanggal']
        jam       = gempa['Jam']
        datetime  = gempa['DateTime']
        point     = gempa['point']['coordinates']
        lintang   = gempa['Lintang']
        bujur     = gempa['Bujur']
        magnitude = gempa['Magnitude']
        kedalaman = gempa['Kedalaman']
        wilayah   = gempa['Wilayah']
        dirasakan = gempa['Dirasakan']

        rows.append({
            "tanggal"     : tanggal,
            "jam"         : jam,
            "datetime"    : datetime,
            "coordinates" : point,
            "lintang"     : lintang,
            "bujur"       : bujur,
            "magnitude"   : magnitude,
            "kedalaman"   : kedalaman,
            "wilayah"     : wilayah,
            "dirasakan"   : dirasakan
        })

    # Render the template with the extracted data
    #print(rows)
    return render_template('main-dirasakan.html', data=rows)


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
            tags = area['@tags']

            areas.append({
                "id": area_id,
                "description": description,
                "latitude": latitude,
                "longitude": longitude,
                "coordinate": coordinate,
                "type": area_type,
                "level": level,
                "domain": domain,
                "tags": tags
            })

    else:
        area = forecast_areas
        area_id = area['@id']
        description = area['@description']
        latitude = area['@latitude']
        longitude = area['@longitude']
        coordinate = area['@coordinate']
        area_type = area['@type']
        level = area['@level']
        domain = area['@domain']
        tags = area['@tags']

        areas.append({
            "id": area_id,
            "description": description,
            "latitude": latitude,
            "longitude": longitude,
            "coordinate": coordinate,
            "type": area_type,
            "level": level,
            "domain": domain,
            "tags": tags
        })

    # Render the template with the extracted data and timestamp
    return render_template(
        'main-diyogyakarta.html',
        areas=areas,
        timestamp=timestamp,
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
        second=second
    )


def parse_weather_data():
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
    for area in forecast_areas:
        area_id = area['@id']
        description = area['@description']
        domain = area['@domain']

        parameters = []
        area_parameters = area['parameter']
        if isinstance(area_parameters, list):
            for parameter in area_parameters:
                parameter_id = parameter['@id']
                parameter_description = parameter['@description']
                parameter_type = parameter['@type']

                parameters.append({
                    "id": parameter_id,
                    "description": parameter_description,
                    "type": parameter_type
                })

        else:
            parameter = area_parameters
            parameter_id = parameter['@id']
            parameter_description = parameter['@description']
            parameter_type = parameter['@type']

            parameters.append({
                "id": parameter_id,
                "description": parameter_description,
                "type": parameter_type
            })

        areas.append({
            "id": area_id,
            "description": description,
            "domain": domain,
            "parameters": parameters
        })

    return areas, timestamp, year, month, day, hour, minute, second

areas, timestamp, year, month, day, hour, minute, second = parse_weather_data()

@app.route("/cuaca-diyogyakarta/<area_id>")
def cuaca_diyogyakarta_area(area_id):
    # Find the area with the given ID
    selected_area = None
    for area in areas:
        if area['id'] == area_id:
            selected_area = area
            break
    #print(timestamp)
    #print(area)
    if selected_area:
        template_name = f"main-area_id.html"
        return render_template(template_name, area=selected_area, timestamp=timestamp, year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    else:
        return "Area not found"

@app.route("/cuaca-diyogyakarta/<area_id>/<parameter_id>")
def cuaca_diyogyakarta_area_id_parameter_id(area_id, parameter_id):
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DIYogyakarta.xml'

    # Use the requests library to get the XML data from the URL
    response = requests.get(url)

    # Parse the XML data using the xmltodict library
    data = xmltodict.parse(response.text)

    # Extract the timestamp
    timestamp = data['data']['forecast']['issue']['timestamp']
    year = data['data']['forecast']['issue']['year']
    month = data['data']['forecast']['issue']['month']
    day = data['data']['forecast']['issue']['day']
    hour = data['data']['forecast']['issue']['hour']
    minute = data['data']['forecast']['issue']['minute']
    second = data['data']['forecast']['issue']['second']

    # Extract the information you need
    forecast_areas = data['data']['forecast']['area']

    selected_area = None
    selected_parameter = None

    for area in forecast_areas:
        if area['@id'] == area_id:
            selected_area = area
            parameters = area['parameter']
            if isinstance(parameters, list):
                for parameter in parameters:
                    if parameter['@id'] == parameter_id:
                        selected_parameter = parameter
                        break
            else:
                if parameters['@id'] == parameter_id:
                    selected_parameter = parameters
                    break
        #print("selected", selected_area)
    if selected_area and selected_parameter:
        template_name = "main-area_id-parameter_id.html"
        timeranges = selected_parameter['timerange']
        for timerange in timeranges:
            values = timerange['value']
            if not isinstance(values, list):
                values = [values]  # Convert single value to a list for consistent processing
                #print(values)
            for value in values:
                unit = value['@unit']
                text = value['#text']
                value['unit'] = unit  # Add 'unit' key to value dictionary
                value['text'] = text  # Add 'text' key to value dictionary
                print(value['unit'])
                print(value['text'])
            #print(values)

        return render_template(
            template_name,
            timestamp=timestamp,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            area_id=area_id,
            area_description=selected_area['@description'],
            area_domain=selected_area['@domain'],
            parameter_id=parameter_id,
            parameter_description=selected_parameter['@description'],
            timeranges=timeranges
        )
    # Return an error if the area or parameter is not found
    return "Area or parameter not found"
