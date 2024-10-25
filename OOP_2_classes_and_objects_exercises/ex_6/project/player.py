class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return (f"Skill {skill_name} added to the "
                f"collection of the player {self.name}")

    def player_info(self) -> str:
        result = (f"Name: {self.name}\n"
                f"Guild: {self.guild}\n"
                f"HP: {self.hp}\n"
                f"MP: {self.mp}\n")
        formatted_skills = [
            f"==={skill} - {mana}"
            for skill, mana in self.skills.items()
        ]
        result += "\n".join(formatted_skills) + "\n"
        return result