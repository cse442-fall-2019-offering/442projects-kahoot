import random
import structures.py



def schedule(availableTimeSlots, Teams, numOfSections):
    #make split into sections
    numOfTimeSlots = availableTimeSlots.count
    sizeOfSection = round(numOfTimeSlots/numOfSections)
    sectionHolder = []
    for i in 0..numOfSections:
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
    Testing_timeslots.append(TimeSlot(t -1, t))

Testing_num_of_sections = 60/10
Testing_teams = []

for t in range(1,5):
    Testing_teams.append(Team(str(t),t))

schedule(Testing_timeslots,Testing_teams,Testing_num_of_sections)

for t in range(0,59):
    print("working??")
