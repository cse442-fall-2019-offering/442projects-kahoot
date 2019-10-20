
print("is this working?")

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
        self.event = None
        #calculate duration???
    def setEvent(event):
        self.event = event

#end TimeSlot

class Event:
    def __init__(self, type):
        self._type = type #should be "Practice" or "Game"
        self._teamList = [] #holds team id

    def addTeam(team):
        self._teamList.append(team)

    def schedule(start,end):
        self._start = start
        self,_end = end
    

team_list = {}
team_list.

