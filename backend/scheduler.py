import random
import structures

import json
import array

def get_week_array(json_string):
    #json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    #parsed_json = (json.loads(json_data))
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))
    team_array = []
    days_array = []
    temp_days = []
    #count = 0
    with open(json_string, 'r') as f:
        distros_dict = json.load(f)
    for distro in distros_dict:
        team_array = (distro['Team'])
        days_array = (distro['Days'])
        temp_days = (distro['Days'])
        print(team_array)
        print(days_array)
    count = len(team_array)
    a = []
    for x in range(0, count):
        a.append(x)
    random.shuffle(a)
    print(a)
    for x in range(0, count):
        temp_days[x] = team_array[a[x]]
    print(temp_days)


#week_
def schedule(week_array, TeamList):
    #make split into sections

'''
def schedule(availableTimeSlots, Teams, numOfSections):
    #make split into sections
    numOfTimeSlots = availableTimeSlots.count
    sizeOfSection = round(numOfTimeSlots/numOfSections)
    sectionHolder = []
    for i in numOfSections:
        section = []
        for j in range(i,((i+1)*sizeOfSection)):
            section.append(availableTimeSlots[j])
        sectionHolder.append(section)
    
    for week in week_array:
        #schedule the teams
        scheduleOneWeek(week,TeamList)


#days_left is a D array to fill
def scheduleOneWeek(days_left,Teams):
    random_Team_set = [i for i in range(0,len(Teams))]

    random.shuffle(random_Team_set)
    
    days_scheduled = 0
    random_index = 0
    while days_scheduled <= len(days_left) and random_index <= len(random_Team_set):
        rand = random_Team_set[random_index]
        e = structures.Event("practice")
        days_left[days_scheduled] = e.addTeam(Teams[random_index]._id)
        random_index += 1
        days_scheduled += 1



    """
    availableTimeSlots = []
    for day in days_left:
        for time_slot in day:
            availableTimeSlots.append(time_slot)
    

    teamsLeft = []
    count =0
    for t in Teams:
        teamsLeft.append(count)
        count = count +1
    random.shuffle(teamsLeft)
    indexOfTeams = 0
    indexOfTimeSlots = 0
    while(len(teamsLeft) != indexOfTeams and len(availableTimeSlots) != indexOfTimeSlots):

        availableTimeSlots[indexOfTimeSlots] = structures.Event("practice").addTeam(Teams[teamsLeft[indexOfTeams]])
        indexOfTeams += 1
        indexOfTimeSlots += 1
    """
    




Testing_weeks = [[[structures.TimeSlot(str("hi"),k*j*i) for k in range(0,1)] for j in range(0,5)] for i in range(0,5)]
Testing_timeslots = []
for t in range(1,60):
    Testing_timeslots.append(structures.TimeSlot(t -1, t))


Testing_teams = [structures.Team(str(i),i) for i in range(0,5)]
for t in range(1,5):
    Testing_teams.append(structures.Team(str(t),t))

schedule(Testing_weeks,Testing_teams)

for t in range(0,59):
    print("working??")'''
