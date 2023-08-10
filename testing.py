import requests
import xmltodict

url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DIYogyakarta.xml'

# Use the requests library to get the XML data from the URL
response = requests.get(url)

# Parse the XML data using the xmltodict library
data = xmltodict.parse(response.text)

forecast_areas = data['data']['forecast']['area']

for area in forecast_areas:
    parameters = area['parameter']
    if isinstance(parameters, list):
        for parameter in parameters:
            parameter_id = parameter['@id']
            timeranges = parameter['timerange']
            if isinstance(timeranges, list):
                for timerange in timeranges:
                    values = timerange['value']
                    if isinstance(values, list):
                        for value in values:
                            value_unit = value['@unit']
                            value_text = value['#text']
                            print("Unit:", value_unit)
                            print("Text:", value_text)
                    else:
                        value_unit = values['@unit']
                        value_text = values['#text']
                        print("Unit:", value_unit)
                        print("Text:", value_text)
            else:
                values = timeranges['value']
                if isinstance(values, list):
                    for value in values:
                        value_unit = value['@unit']
                        value_text = value['#text']
                        print("Unit:", value_unit)
                        print("Text:", value_text)
                else:
                    value_unit = values['@unit']
                    value_text = values['#text']
                    print("Unit:", value_unit)
                    print("Text:", value_text)
