import random
import structures
import router
import json
import array

def get_week_array(json_string):
    #json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    #parsed_json = (json.loads(json_data))
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))
    team_objects_array = []
    #days_array = []
    
    temp_team = []
    dict = {}
    count = 0
    new_team_array = []
    new_day_array = []
    
    with open(json_string, 'r') as f:
        distros_dict = json.load(f)
    for distro in distros_dict:
        team_objects_array = (distro['team'])
        days_array = (distro['day'])
        
        for elem in team_objects_array:
            new_team_array.append(elem['team'])
        for elem in days_array:
            new_day_array.append(elem['day'])
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
    for x in range(0, count):
        dict.update({temp_team[x] : new_day_array[x]})
    print(dict)

get_week_array('distros.json')