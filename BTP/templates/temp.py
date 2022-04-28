import requests
import json
from datetime import datetime
import pytz

headers = {
    'Authorization': 'occvlk7x6r7o0ndol75wlbae8odkdn38yfbu15wkm4z7imowp3'
}


def convert_date(datestring):
    local = pytz.timezone("Asia/Kolkata")
    naive = datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(naive, is_dst=None)
    return local_dt.astimezone(pytz.utc).isoformat()


def get_availability(mentorEmail, fromDate, toDate, duration):  # YYYY-MM-DD Format String
    timezone = "Asia/Kolkata"
    apiURL = f"https://api.vyte.in/v2/slots?duration={duration}&emails={mentorEmail}&from={fromDate}&to={toDate}&timezone={timezone}"
    response = requests.get(apiURL, headers=headers)
    jsonResponse = json.loads(response.text)
    for slot in jsonResponse['slots']:
        print(slot)


def create_meeting(mentorName, startDate, endDate, mentorEmail, menteeEmail, message, allDay=False):  # 2020-04-22 10:00:00
    json_data = {
        'title': f'Meeting with {mentorName}',
        'created_by': {
            'email': 'docitmed@gmail.com',
        },
        'dates': [
            {
                'all_day': allDay,
                'date': startDate,
                'end_date': endDate,
            },
        ],
        'places': [{"name": "Google Meet", "source": "Google Meet"}],
        'invitees': [{"email": mentorEmail}, {"email": menteeEmail}],
        'timezone': "Asia/Kolkata",
        'messages': {
            'body': message
        },
        'confirmed': {
            'flag': True
        }
    }
    response = requests.post(
        'https://api.vyte.in/v2/events', headers=headers, json=json_data)
    jsonResponse = json.loads(response.text)
    # print(jsonResponse)
    print(
        f"Meeting ID: {jsonResponse['_id']} \nPlace ID: {jsonResponse['places'][0]['_id']} \nDate ID: {jsonResponse['dates'][0]['_id']}")
    print(f"Meeting Link: {jsonResponse['places'][0]['address']}")


create_meeting("Rajat Soni", "2022-04-27T10:34:11Z", "2022-04-27T11:34:11Z",
               "rajatsonibkn2002@gmail.com", "singhalneeraj933@gmail.com", "Hello!")


def cancel_meeting(meetingID):
    response = requests.post(
        f'https://api.vyte.in/v2/events/{meetingID}/cancel', headers=headers)
# cancel_meeting("6261ac542d9bf27530118103")


def rescheduleMeeting(meetingID, startDate, endDate, allDay=False):
    headers = headers
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
    response = requests.put(
        f'https://api.vyte.in/v2/events/{meetingID}', headers=headers, json=data)
    print(response.text)
# rescheduleMeeting("62625a828ffea36b3ab47f73", "2020-04-22 17:00:00", "2020-04-22 18:00:00")


def confirm_meeting(meetingID, placeID):
    data = {'p': placeID}
    response = requests.post(
        f'https://api.vyte.in/v2/events/{meetingID}/confirm', headers=headers, data=data)
    print(response.text)

# confirm_meeting("626295d682c1d4bd96a563f1", "626295d682c1d46eb5a563f3")
