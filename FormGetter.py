import requests

def doForm(id):
	headers = {
		'X-API-Key': 'zAI65kxpNF2gJQfEpd6vP1ughBhwFu2UCZNVHwht',
	}

	response = requests.get('https://api.foia.gov/api/agency_components/8216158f-8089-431d-b866-dc334e8d4758/request_form' + id + '/request_form', headers=headers)