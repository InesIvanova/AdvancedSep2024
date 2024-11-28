from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)
        self.type = "royal"


    def attack(self):
        # TODO make it as base validation??
        self.ammunition -= 25
        if self.ammunition < 0:
            self.ammunition = 0