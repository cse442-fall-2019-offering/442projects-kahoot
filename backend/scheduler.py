import random
import structures
import router
import json
import array
import copy

'''def get_week_array(json_string):
    
        
    print(new_day_array)
    print(new_team_array)
    #temp_team = new_team_array
    
    count = len(new_team_array)
    a = []
    for x in range(0, count):
        a.append(x)
    random.shuffle(a)
    #print(a)
    #print(new_day_array)
    for x in range(0, count):
        temp_team.append(new_team_array[a[x]]) 
    #print(temp_team)
    final_team = {}
    for x in range(0, count):
        final_team.update({temp_team[x] : new_day_array[x]})
    print(final_team)
    return str(final_team)
'''
#locally testing json parser
'''
def read_Json_file():
    teams = []
    days = []
    timeOption = []
    weeks = []
    sdate = []
    practices = []
    f = open("distros.json")
    contents = json.load(f)
    f.close()
    type(contents)
    teaminfo = (contents['teaminfo'])
    #print(type(teaminfo))
    del teaminfo[0]
    #print(teaminfo)
    timing = (contents['timing'])
    del timing[0]
    #print(timing)
    options = (contents['options'])
    del options[0]
    #print(options)

    for elem in teaminfo:
        teams.append(elem['team'])
    for elem in timing:
        days.append(elem['day'])
        timeOption.append(elem['timeOption'])
    for elem in options:
        weeks.append(elem['weeks'])
        practices.append(elem['practices'])
        sdate.append(elem['sdate'])
    print(teams)
    print(days)
    print(timeOption)
    print(weeks)
    print(practices)
    print(sdate)


    #contents = 
    
    #temp = contents['teaminfo']
read_Json_file()
'''


#returns 2 things, teams and days
def parse_Json_dictionary(json_dictionary):
    '''
    team_objects_array = []
    
    temp_team = []
    count = 0
    new_team_array = []
    new_day_array = []
    
    team_objects_array = (json_dictionary['team'])
    days_array = (json_dictionary['day'])
    
    for elem in team_objects_array:
        new_team_array.append(elem['team'])
    for elem in days_array:
        new_day_array.append(elem['day'])
    return new_team_array,new_day_array
    '''
    teams = []
    days = []
    timeOption = []
    weeks = []
    sdate = []
    practices = []
    teaminfo = (json_dictionary['teaminfo'])
    del teaminfo[0]
    timing = (json_dictionary['timing'])
    del timing[0]
    options = (json_dictionary['options'])
    del options[0]

    for elem in teaminfo:
        teams.append(elem['team'])
    for elem in timing:
        days.append(elem['day'])
        timeOption.append(elem['timeOption'])
    for elem in options:
        weeks.append(elem['weeks'])
        practices.append(elem['practices'])
        sdate.append(elem['sdate'])
    return teams, days, timeOption, weeks, sdate, practices
    

#games are in the format (teams[i],teams[j])
#return true if there is any 
def check_tuples_for_equivelances(game1, game2):
    flag = game1[0] == game2[0]
    flag = flag or game1[0] == game2[1]
    flag = flag or game1[1] == game2[0]
    flag = flag or game1[1] == game2[1]
    #flag should be true because we want all of the conflict edges
    return flag


#input list of teams should be less than 8

#returns the game list for matching
def make_games(num_of_teams):
    '''
    game_list = []
    for round in range(0, num_of_rounds)
        for i in range(0, len(teams)):
            for j in range(i,len(teams)):
                if(i != j):
                    game_list.append((teams[i],teams[j]))
    
    if(len(teams) > 3):
        #add cases where we do not have the same games twice
        null = 0
    #create adjacency matrix with edges defined as games not being able to be scheduled together
    game_adj_graph[[0 for _ in range(len(game_list))] for _ in range(len(game_list))]
    for game_index in range(len(game_list)):
        for matrix_index in range(len(game_list)):
            if(check_tuples_for_equivelances(game_list[game_index],game_list[matrix_index])):
                game_adj_graph[game_index][matrix_index] = 1
            else:
                game_adj_graph[game_index][matrix_index] = 0
    #create weeks
    '''
    if(num_of_teams % 2 == 1):
        num_of_teams += 1
    weeks = []
    if(num_of_teams == 2):
        weeks.append([(1,2)])
    if(num_of_teams == 4):
        weeks.append([(1,2),(3,4)])
        weeks.append([(2,3),(1,4)])
        weeks.append([(1,3),(2,4)])
    if(num_of_teams == 6):
        weeks.append([(1,2),(3,4),(5,6)])
        weeks.append([(1,3),(2,6),(4,5)])
        weeks.append([(1,4),(2,5),(3,6)])
        weeks.append([(1,5),(2,3),(4,6)])
        weeks.append([(1,6),(2,4),(3,5)])
    if(num_of_teams == 8):
        weeks.append([(5,8),(3,7),(4,6),(1,2)])
        weeks.append([(2,3),(1,4),(6,8),(5,7)])
        weeks.append([(3,4),(2,5),(7,8),(1,6)])
        weeks.append([(1,8),(3,6),(2,7),(4,5)])
        weeks.append([(5,6),(2,8),(1,3),(4,7)])
        weeks.append([(6,7),(1,5),(2,4),(3,8)])
        weeks.append([(1,7),(4,8),(3,5),(2,6)])
    return weeks

def day_sort_function(elem):
    if("Monday" == elem[2]):
        time_sort_function(elem[2])
        return 1
    if("Tuesday" == elem[2]):
        time_sort_function(elem[2])
        return 2
    if("Wednesday" == elem[2]):
        time_sort_function(elem[2])
        return 3
    if("Thursday" == elem[2]):
        time_sort_function(elem[2])
        return 4
    if("Friday" == elem[2]):
        time_sort_function(elem[2])
        return 5
    if("Saturday" == elem[2]):
        time_sort_function(elem[2])
        return 6
    if("Sunday" == elem[2]):
        time_sort_function(elem[2])
        return 7
    return -1

def time_sort_function(elem):
    timelist = []
    for e in elem;
        timelist.append(e[1])
    sorted(timelist)

def make_shell_of_calendar(num_of_weeks, time_slots):
    week_array = []
    for x in time_slots:
        week_array.append(["_","PorG",x])
    week_array.sort(key = day_sort_function)
    calendar_shell = [copy.deepcopy(week_array) for _ in range(0,num_of_weeks)]
    return calendar_shell

def fill_in_calendar(calendar, teams, games_list):
    shuffable_team_list = copy.deepcopy(teams)
    random.shuffle(shuffable_team_list)
    #if()
    weekindex = 0
    finalCalendar = []
    #assume games_list size =< num of weeks
    for week in calendar:
        newWeek = copy.deepcopy(week)
        #practice schedule
        #make practices
        practice_shuffle_list = copy.deepcopy(teams)
        random.shuffle(practice_shuffle_list)
        index_of_timeSlot = 0
        for team in practice_shuffle_list:
            newWeek[index_of_timeSlot][0] = team
            newWeek[index_of_timeSlot][1] = "Practice"
            index_of_timeSlot += 1

        #schedule games
        next_index_of_game = len(week)-1
        ignore_team = -1
        if(len(teams) % 2 == 1):
            ignore_team = len(teams) + 1
        for game in games_list[weekindex]:
            if(game[0] == ignore_team or game[1] == ignore_team):
                continue
            newWeek[next_index_of_game][1] = "Game"
            team1 = shuffable_team_list[game[0] -1]
            team2 = shuffable_team_list[game[1] -1]
            
            newWeek[next_index_of_game][0] = team1+ " vs "+ team2
            
            next_index_of_game  = next_index_of_game - 1
        
        finalCalendar.append(newWeek)
        weekindex += 1
    return finalCalendar



def main(json_dictionary):
    

    #parse json_dictionary
    teams,timeslots = parse_Json_dictionary(json_dictionary)
    number_of_weeks = len(teams) - 1
    print("Number of Weeks" , number_of_weeks)
    #make games 
    games_per_weeks = make_games(len(teams))
    print(games_per_weeks)

    #make shell schedule
    calendar = make_shell_of_calendar(number_of_weeks, timeslots)
    print(calendar)
    #error handling
    #if(len(games_per_weeks)> len(calendar))
    
    #fill in calendar
    copy_of_teams = teams
    newcalendar = fill_in_calendar(calendar, copy_of_teams, games_per_weeks)
    print(newcalendar)

    json_output = json.dumps(newcalendar)

    print(json_output)

    #format the final result
    #send to google calendar
        
