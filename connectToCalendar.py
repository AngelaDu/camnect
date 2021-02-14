# get Calendars
def readCalendar(service):
    result = service.calendarList().list().execute()
    return result


# return Events
def readEvents(service):
    calendar = readCalendar(service)
    result = service.events().list(calendarId=calendar["items"][0]["id"]).execute()
    for event in result["items"]:
        print(event["summary"])

