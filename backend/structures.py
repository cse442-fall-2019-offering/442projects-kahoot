'''
class Team:
    #_teamName
    #_id
    def __init__(self, teamName, id):
        self._teamName = teamName
        self._id = id
    def print_me():
        retString = "(" + self._teamName + str(self._id)+ ")"
        return retString
    
#end Team

class TimeSlot:
    def __init__(self, startTime,endTime):
        self._start = startTime
        self._end = endTime
        #calculate duration???
    

#end TimeSlot

class Event:
    def __init__(self, type):
        self._type = type #should be "Practice" or "Game"
        self._teamList = []

    def addTeam(team):
        _teamList.add(team)

    def schedule(start,end):
        _start = start
        _end = end
''' 


