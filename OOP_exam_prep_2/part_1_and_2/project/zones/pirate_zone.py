from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)
        self.type = "pirate"


    def zone_info(self):
        result = "@Pirate Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"

        pirate_ships = [s for s in self.ships if s.__class__.__name__ == "RoyalBattleship"]
        result += (f"Battleships currently in the Pirate Zone: "
                   f"{len(self.ships)}, "
                   f"{len(pirate_ships)} out of them are Royal Battleships.")

        ordered_ships = self.get_ships()
        result += f"\n#{', '.join([s.name for s in ordered_ships])}#" if ordered_ships else ""
        return result
