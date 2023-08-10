def extract_data(json_data):
    data = json.loads(json_data)
    issue = data['data']['forecast']['issue']
    area = data['data']['forecast']['area']

    timestamp = issue['timestamp']
    year = issue['year']
    month = issue['month']
    day = issue['day']
    hour = issue['hour']
    minute = issue['minute']
    second = issue['second']

    area_info = []
    for a in area:
        area_id = a['@id']
        description = a['@description']
        latitude = a['@latitude']
        longitude = a['@longitude']
        coordinate = a['@coordinate']
        area_type = a['@type']
        region = a['@region']
        level = a['@level']
        domain = a['@domain']
        tags = a['@tags']

        names = {}
        for name in a['name']:
            lang = name['@xml:lang']
            text = name['#text']
            if lang == 'id_ID':
                names[lang] = text

        parameters = []
        for parameter in a.get('parameter', []):
            parameter_id = parameter['@id']
            parameter_description = parameter['@description']
            parameter_type = parameter['@type']

            timeranges = []
            #print('base timeranges', timeranges)
            for timerange in parameter.get('timerange', []):
                if isinstance(timerange, dict):
                    timerange_type = timerange['@type']
                    timerange_day = timerange.get('@day')  # Use .get() to handle missing key
                    timerange_h = timerange.get('@h')  # Use .get() to handle missing key
                    timerange_datetime = timerange['@datetime']
                    
                    values = []
                    for value in timerange.get('value', []):
                        if isinstance(value, dict):
                            value_unit = value.get('@unit')
                            value_text = value.get('#text')
                            values.append({
                                'unit': value_unit,
                                'text': value_text
                            })
                        #print('base values', values)

                    timeranges.append({
                        'type': timerange_type,
                        'day': timerange_day,
                        'h': timerange_h,
                        'datetime': timerange_datetime,
                        'values': values
                    })

            parameters.append({
                'id': parameter_id,
                'description': parameter_description,
                'type': parameter_type,
                'timeranges': timeranges
            })

        area_info.append({
            'id': area_id,
            'description': description,
            'latitude': latitude,
            'longitude': longitude,
            'coordinate': coordinate,
            'type': area_type,
            'region': region,
            'level': level,
            'domain': domain,
            'tags': tags,
            'names': names,
            'parameters': parameters
        })

    return {
        'issue': {
            'timestamp': timestamp,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'minute': minute,
            'second': second
        },
        'area': area_info
    }