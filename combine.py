import requests
import xmltodict
import json

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

        parameters = []
        area_parameters = area['parameter']
        if isinstance(area_parameters, list):
            for parameter in area_parameters:
                parameter_id = parameter['@id']
                parameter_description = parameter['@description']
                parameter_type = parameter['@type']

                timeranges = []
                parameter_timeranges = parameter['timerange']
                if isinstance(parameter_timeranges, list):
                    for timerange in parameter_timeranges:
                        timerange_type = timerange['@type']
                        timerange_datetime = timerange['@datetime']

                        values = []
                        timerange_values = timerange['value']
                        if isinstance(timerange_values, list):
                            for value in timerange_values:
                                value_unit = value['@unit']
                                value_text = value['#text']

                                values.append({
                                    value_unit: value_text
                                })
                        else:
                            value_unit = timerange_values['@unit']
                            value_text = timerange_values['#text']

                            values.append({
                                value_unit: value_text
                            })

                        timeranges.append({
                            "type": timerange_type,
                            "datetime": timerange_datetime,
                            "values": values
                        })

                else:
                    timerange_type = parameter_timeranges['@type']
                    timerange_datetime = parameter_timeranges['@datetime']

                    values = []
                    timerange_values = parameter_timeranges['value']
                    if isinstance(timerange_values, list):
                        for value in timerange_values:
                            value_unit = value['@unit']
                            value_text = value['#text']

                            values.append({
                                value_unit: value_text
                            })
                    else:
                        value_unit = timerange_values['@unit']
                        value_text = timerange_values['#text']

                        values.append({
                            value_unit: value_text
                        })

                    timeranges.append({
                        "type": timerange_type,
                        "datetime": timerange_datetime,
                        "values": values
                    })

                parameters.append({
                    "id": parameter_id,
                    "description": parameter_description,
                    "type": parameter_type,
                    "timeranges": timeranges
                })

        else:
            parameter = area_parameters
            parameter_id = parameter['@id']
            parameter_description = parameter['@description']
            parameter_type = parameter['@type']

            timeranges = []
            parameter_timeranges = parameter['timerange']
            if isinstance(parameter_timeranges, list):
                for timerange in parameter_timeranges:
                    timerange_type = timerange['@type']
                    timerange_datetime = timerange['@datetime']

                    values = []
                    timerange_values = timerange['value']
                    if isinstance(timerange_values, list):
                        for value in timerange_values:
                            value_unit = value['@unit']
                            value_text = value['#text']

                            values.append({
                                value_unit: value_text
                            })
                    else:
                        value_unit = timerange_values['@unit']
                        value_text = timerange_values['#text']

                        values.append({
                            value_unit: value_text
                        })

                    timeranges.append({
                        "type": timerange_type,
                        "datetime": timerange_datetime,
                        "values": values
                    })

            else:
                timerange_type = parameter_timeranges['@type']
                timerange_datetime = parameter_timeranges['@datetime']

                values = []
                timerange_values = parameter_timeranges['value']
                if isinstance(timerange_values, list):
                    for value in timerange_values:
                        value_unit = value['@unit']
                        value_text = value['#text']

                        values.append({
                            value_unit: value_text
                        })
                else:
                    value_unit = timerange_values['@unit']
                    value_text = timerange_values['#text']

                    values.append({
                        value_unit: value_text
                    })

                timeranges.append({
                    "type": timerange_type,
                    "datetime": timerange_datetime,
                    "values": values
                })

            parameters.append({
                "id": parameter_id,
                "description": parameter_description,
                "type": parameter_type,
                "timeranges": timeranges
            })

        areas.append({
            "id": area_id,
            "description": description,
            "latitude": latitude,
            "longitude": longitude,
            "coordinate": coordinate,
            "type": area_type,
            "level": level,
            "domain": domain,
            "parameters": parameters
        })

# Print the extracted values
print("Timestamp:", timestamp)
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)
print()

# Print additional area information
for area in areas:
    print("Area ID:", area['id'])
    print("Description:", area['description'])
    print("Latitude:", area['latitude'])
    print("Longitude:", area['longitude'])
    print("Coordinate:", area['coordinate'])
    print("Type:", area['type'])
    print("Level:", area['level'])
    print("Domain:", area['domain'])
    print()

    # Print parameter information
    for parameter in area['parameters']:
        print("Parameter ID:", parameter['id'])
        print("Parameter Description:", parameter['description'])
        print("Parameter Type:", parameter['type'])
        print()

        # Print timerange information
        for timerange in parameter['timeranges']:
            print("Timerange Type:", timerange['type'])
            print("Timerange Datetime:", timerange['datetime'])
            print()

            # Print value information
            for value in timerange['values']:
                print(value_unit, value_text)
                print()

            print()

        print()

    print()

# Convert to JSON with indentation
json_data = json.dumps(areas, indent=4)

# Print prettier JSON data
print(json_data)
