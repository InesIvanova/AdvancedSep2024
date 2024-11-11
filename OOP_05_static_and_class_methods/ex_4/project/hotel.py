from typing import Optional

from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: list[Room] = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hote":
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> Optional[str]:
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number) -> Optional[str]:
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self) -> str:
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        result = (f"Hotel {self.name} has {self.guests} total guests\n"
                  f"Free rooms: {', '.join(free_rooms)}\n"
                  f"Taken rooms: {', '.join(taken_rooms)}")
        return result



