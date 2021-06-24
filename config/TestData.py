import datetime


class TestData:
    BASE_URL = 'https://www.orbitz.com/'
    LOCATION_FROM = 'San Francisco'
    LOCATION_TO = 'New York'
    DEPARTING_DATE_STRING = '{dt:%b} {dt.day}'.format(dt=(datetime.datetime.now() + datetime.timedelta(days=14)))
    RETURNING_DATE_STRING = '{dt:%b} {dt.day}'.format(dt=(datetime.datetime.now() + datetime.timedelta(days=21)))
