import requests, json, config
from datetime import datetime   
import pytz

def convert_date(datestring): #2022-04-28 23:30:00
    datelist = datestring.split(" ")
    returnstring = f'{datelist[0]}T{datelist[1]}+05:30'
    datetimeobject = datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
    print(datetimeobject)
    return returnstring
# convert_date("2022-04-28 23:30:00")


def get_availability(mentorEmail, fromDate, toDate, duration):  #YYYY-MM-DD Format String
    timezone = config.timezone
    apiURL = f"https://api.vyte.in/v2/slots?duration={duration}&emails={mentorEmail}&from={fromDate}&to={toDate}&timezone={timezone}"
    response = requests.get(apiURL, headers=config.headers)
    print(response.status_code)
    print(type(json.loads(response.text)))
    # jsonResponse = json.loads(response.text)
    # for slot in jsonResponse['slots']:
        # print(slot)
get_availability("19ucc014@lnmiit.ac.in", "2022-04-28", "2022-04-28", "30")
    

def create_meeting(mentorName, startDate, endDate, mentorEmail, menteeEmail, allDay=False): #UTC ISO-8601 Format
    json_data = {
        'title': f'Meeting with {mentorName}',
        'created_by': {
            'email': config.organizationEmail,
        },
        'dates': [
            {
                'all_day': allDay,
                'date': convert_date(startDate),                 
                'end_date': convert_date(endDate),
            },
        ],
        'places': [{"name": "Google Meet", "source": "Google Meet"}],
        'invitees': [{"email": mentorEmail}, {"email": menteeEmail}],
        'timezone': config.timezone,
        'confirmed': {
            'flag': True
        }
    }
    response = requests.post('https://api.vyte.in/v2/events', headers=config.headers, json=json_data)
    jsonResponse = json.loads(response.text)
    print(f"Meeting ID: {jsonResponse['_id']} \nPlace ID: {jsonResponse['places'][0]['_id']} \nDate ID: {jsonResponse['dates'][0]['_id']}")
    print(f"Meeting Link: {jsonResponse['places'][0]['address']}")
create_meeting("Rajat Soni", "2022-04-28 23:30:00", "2022-04-29 00:30:00", "rajatsonibkn2002@gmail.com", "fotugrafers@gmail.com")



def cancel_meeting(meetingID):
    response = requests.post(f'https://api.vyte.in/v2/events/{meetingID}/cancel', headers=config.headers)
# cancel_meeting("6261ac542d9bf27530118103")


def rescheduleMeeting(meetingID, startDate, endDate, allDay=False):
    headers = config.headers
    headers['Content-Type'] = 'application/json'
    data = {
        'dates': [
            {
                'all_day': allDay,
                'date': convert_date(startDate),                 
                'end_date': convert_date(endDate),
            },
        ]
    }
    response = requests.put(f'https://api.vyte.in/v2/events/{meetingID}', headers=headers, json=data)
    print(response.text)
# rescheduleMeeting("62625a828ffea36b3ab47f73", "2020-04-22 17:00:00", "2020-04-22 18:00:00")

def confirm_meeting(meetingID, placeID):
    data = {'p': placeID}
    response = requests.post(f'https://api.vyte.in/v2/events/{meetingID}/confirm', headers=config.headers, data=data)
    print(response.text)

# confirm_meeting("626295d682c1d4bd96a563f1", "626295d682c1d46eb5a563f3")