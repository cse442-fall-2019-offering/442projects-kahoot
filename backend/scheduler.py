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
    team_names = []
    #days_array = []
    
    temp_team = []
    dict = {}
    count = 0
    
    with open(json_string, 'r') as f:
        distros_dict = json.load(f)
    for distro in distros_dict:
        team_objects_array = (distro['team'])
        #days_array = (distro['Days'])
        #temp_team = (distro['Team'])
        print(team_objects_array)
    '''count = len(team_array)
    a = []
    for x in range(0, count):
        a.append(x)
    random.shuffle(a)
    print(a)
    for x in range(0, count):
        temp_team[x] = team_array[a[x]]
    print(temp_team)
    days_array = (distro['Days'])
    print(days_array)'''
get_week_array('distros.json')