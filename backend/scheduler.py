import random
import structures




#week_
def schedule(week_array, TeamList):
    #make split into sections
    
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


Testing_teams = [structures.Team(str(i),i) for i in range(0,5)]

schedule(Testing_weeks,Testing_teams)

