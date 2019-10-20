import random
import structures
import json
import array

def get_week_array():
    #json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    #parsed_json = (json.loads(json_data))
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))
    team_array = []
    days_array = []
    temp_team = []
    dict = {}
    #count = 0
    with open('distros.json', 'r') as f:
        distros_dict = json.load(f)
    for distro in distros_dict:
        team_array = (distro['Team'])
        days_array = (distro['Days'])
        temp_team = (distro['Team'])
        print(team_array)
        #print(days_array)
    count = len(team_array)
    a = []
    for x in range(0, count):
        a.append(x)
    random.shuffle(a)
    print(a)
    for x in range(0, count):
        temp_team[x] = team_array[a[x]]
    print(temp_team)
    days_array = (distro['Days'])
    print(days_array)

get_week_array()
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
    
    #fill each section with a proper amount of practices
    #ouput the full TimeSlots


def scheduleOneSection(availableTimeSlots,Teams):
    teamsLeft = []
    count =0
    for t in Teams:
        teamsLeft.append(count)
        count = count +1
    random.shuffle(teamsLeft)
    indexOfTeams = 0
    indexOfTimeSlots = 0
    while(teamsLeft.count != indexOfTeams and availableTimeSlots.count != indexOfTimeSlots):
        availableTimeSlots[indexOfTimeSlots] = structures.Event("practice").addTeam(Teams[teamsLeft[indexOfTeams]])
        indexOfTeams += 1
        indexOfTimeSlots += 1
    return availableTimeSlots



Testing_timeslots = []
for t in range(1,60):
    Testing_timeslots.append(structures.TimeSlot(t -1, t))

Testing_num_of_sections = 60/10
Testing_teams = []

for t in range(1,5):
    Testing_teams.append(structures.Team(str(t),t))

schedule(Testing_timeslots,Testing_teams,Testing_num_of_sections)

for t in range(0,59):
    print("working??")'''
