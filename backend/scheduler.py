import random
import structures
import router
import json
import array

def get_week_array(json_string):
    
        
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


def read_Json_file():
    f = open("distros.txt", 'r')
    contents = f.read()
    get_week_array(contents)


#returns 2 things, teams and days
def parse_Json_dictionary(json_dictionary):
    #json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    #parsed_json = (json.loads(json_data))
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))
    team_objects_array = []
    #days_array = []
    
    temp_team = []
    count = 0
    new_team_array = []
    new_day_array = []
    
    team_objects_array = (json_string['team'])
    days_array = (json_string['day'])
    
    for elem in team_objects_array:
        new_team_array.append(elem['team'])
    for elem in days_array:
        new_day_array.append(elem['day'])
    return new_team_array,new_day_array

#games are in the format (teams[i],teams[j])
#return true if there is any 
def check_tuples_for_equivelances(game1, game2):
    flag = game1[0] == game2[0]
    flag = flag or game1[0] == game2[1]
    flag = flag or game1[1] == game2[0]
    flag = flag or game1[1] == game2[1]
    #flag should be true because we want all of the conflict edges
    return flag


#input list of teams
#input num_of_rounds
#returns the game list
def make_games(teams, num_of_rounds):
    game_list = []
    for round in range(0, num_of_rounds)
        for i in range(0, len(teams)):
            for j in range(i,len(teams)):
                if(i != j):
                    game_list.append((teams[i],teams[j])
    
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
    
    



    


def main(json_dictionary):
    #parse json_dictionary
    teams,days = parse_Json_dictionary(json_dictionary)
    #make games 

    #check if possible 
    #schedule games
    #format the final result
    #send to google calendar
        
    