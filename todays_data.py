import requests

today_url = 'https://covid19.th-stat.com/api/open/today'
response = requests.get(today_url)
response_json = response.json()

def f_number(n):
    return str(f'{n:,}')

def get_variable(key):
    return response_json[key]

def print_stuff(stuff, data):
    print(f'{stuff}: {str(f_number(data))}')

confirmed = get_variable('Confirmed')
recovered = get_variable('Recovered')
hospitalized = get_variable('Hospitalized')
deaths = get_variable('Deaths')
newConfirmed = get_variable('NewConfirmed')
newRecovered = get_variable('NewRecovered')
newHospitalized = get_variable('NewHospitalized')
newDeaths = get_variable('NewDeaths')
updateDate = get_variable('UpdateDate')
updateDate = updateDate[0:10]
fatality_rate = round(deaths/confirmed*100, 2)


print(f'\nCountry: Bangkok\nDate: {updateDate}\n')
print('Summary:')
print_stuff('Confirmed cases', confirmed)
print_stuff('Recovered patients', recovered)
print_stuff('Hospitalized patients', hospitalized)
print_stuff('Deaths', deaths)
print(f'Fatality Rate: ' + str(fatality_rate) + '%\n')
print('Today\'s update: ''')
print_stuff('New cases confirmed today', newConfirmed)
print_stuff('New patients hospitalized today', newHospitalized)
print_stuff('Patients recovered today', newRecovered)
print_stuff('Fatilities today', newDeaths)





