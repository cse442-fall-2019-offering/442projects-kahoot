
class Team:
    #_teamName
    #_id
    __init__(self,teamname,id):
        self._teamName = teamname
        self._id = id
#end Team

class TimeSlot:
    __init__(self, startTime,endTime):
        self._start = startTime
        self._end = endTime
        #calculate duration???
#end TimeSlot

class Event:
    __init__(self, type):
        self._type = type #should be "Practice" or "Game"
        self._teamList = []

    addTeam(team):
        _teamList.add(team)

    schedule(start,end):
        _start = start
        _end = end

    
