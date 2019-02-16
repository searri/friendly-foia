import requests

headers = {
    'X-API-Key': 'zAI65kxpNF2gJQfEpd6vP1ughBhwFu2UCZNVHwht',
}

response = requests.get('https://api.foia.gov/api/agency_components/[[ID]]/request_form', headers=headers)