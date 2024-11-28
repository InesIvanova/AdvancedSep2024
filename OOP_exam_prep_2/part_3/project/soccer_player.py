class SoccerPlayer:
    _VALID_TEAMS = ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]

    def __init__(self, name: str, age: int, goals: int, team: str):
        self.name = name
        self.age = age
        self.goals = goals
        self.team = team
        self.achievements = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 5:
            raise ValueError("Name should be more than 5 symbols!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Players must be at least 16 years of age!")
        self.__age = value

    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, value):
        if value < 0:
            value = 0
        self.__goals = value

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        if value not in SoccerPlayer._VALID_TEAMS:
            raise ValueError(f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!")
        self.__team = value

    def change_team(self, new_team: str):
        if new_team not in SoccerPlayer._VALID_TEAMS:
            return "Invalid team name!"
        self.team = new_team
        return "Team successfully changed!"

    def add_new_achievement(self, achievement_name: str):
        if achievement_name not in self.achievements:
            self.achievements[achievement_name] = 0
        self.achievements[achievement_name] += 1
        return f"{achievement_name} has been successfully added to the achievements collection!"

    def __lt__(self, other):
        if self.goals < other.goals:
            return f"{other.name} is a top goal scorer! S/he scored more than {self.name}."
        return f"{self.name} is a better goal scorer than {other.name}."