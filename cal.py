#!/usr/bin/env python3
from datetime import datetime

a_meetings = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
a_workday = ['09:00', '20:00']

a_meetings = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
a_workday = ['10:00', '18:30']

length = 30

output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


def find_available(workday, meetings):
    free_time = []
    num_of_meetings = len(meetings)

    first_meeting = meetings[0]
    last_meeting = meetings[-1]

    # find time between start of day and first meeting
    if workday.start < first_meeting.start:
        free_time.append([workday.start, first_meeting.start])

    # find time between meetings
    for i, meeting in enumerate(meetings):
        if i < num_of_meetings && meetings[i].end < meetings[i+1].start:
            free_time.append([meetings[i].end, meetings[i+1].start])

    # find time between last meeting and end of day
    if workday.end > last_meeting.end:
        free_time.append([last_meeting.end, workday.end])

    return free_time
