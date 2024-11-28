from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class SoccerPlayerTests(TestCase):
    def setUp(self):
        self.p = SoccerPlayer("TestTest", 16, 2, "Barcelona")

    def test_init(self):
        self.assertEqual(self.p.name, "TestTest")
        self.assertEqual(self.p.age, 16)
        self.assertEqual(self.p.goals, 2)
        self.assertEqual(self.p.team, "Barcelona")
        self.assertEqual(self.p.achievements, {})

        self.assertEqual(self.p._VALID_TEAMS, ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"])
        self.assertEqual(SoccerPlayer._VALID_TEAMS, ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"])

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.p.name = "Test5"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.p.name = "Test"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_invalid_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.p.age = 15
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_goals_are_negative_sets_them_to_null(self):
        self.assertEqual(self.p.goals, 2)

        self.p.goals = -1

        self.assertEqual(self.p.goals, 0)

    def test_invalid_team_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.p.team = "Invalid"
        valid_teams = SoccerPlayer._VALID_TEAMS
        self.assertEqual(str(ex.exception), f"Team must be one of the following: {', '.join(valid_teams)}!")

    def test_change_team_invalid_team(self):
        self.assertEqual(self.p.team, "Barcelona")

        result = self.p.change_team("Invalid")
        self.assertEqual(result, "Invalid team name!")

        self.assertEqual(self.p.team, "Barcelona")

    def test_change_team(self):
        self.assertEqual(self.p.team, "Barcelona")

        result = self.p.change_team("Juventus")

        self.assertEqual(result, "Team successfully changed!")

        self.assertEqual(self.p.team, "Juventus")

    def test_increment_add_new_achievement(self):
        self.assertEqual(self.p.achievements, {})

        result = self.p.add_new_achievement("Test")

        self.assertEqual(result, f"Test has been successfully added to the achievements collection!")

        self.assertEqual(self.p.achievements, {"Test": 1})

        # Increment

        result = self.p.add_new_achievement("Test")
        self.assertEqual(result, f"Test has been successfully added to the achievements collection!")
        self.assertEqual(self.p.achievements, {"Test": 2})

        # add new achievement to the collection
        result = self.p.add_new_achievement("Test2")
        self.assertEqual(result, f"Test2 has been successfully added to the achievements collection!")
        self.assertEqual(self.p.achievements, {"Test": 2, "Test2": 1})

    def test_comparison(self):
        p2 = SoccerPlayer("Test22", 18, 1, "Juventus")

        result = self.p < p2

        self.assertEqual(result, f"{self.p.name} is a better goal scorer than {p2.name}.")

        # Test the same
        result = p2 > self.p
        self.assertEqual(result, f"{self.p.name} is a better goal scorer than {p2.name}.")

        # Test eq is not considered

        p2.goals = 2
        result = p2 < self.p
        self.assertEqual(result, f"{p2.name} is a better goal scorer than {self.p.name}.")

        result = self.p < p2
        self.assertEqual(result, f"{self.p.name} is a better goal scorer than {p2.name}.")

        # Ours is less
        self.p.goals = 1

        self.assertLess(self.p.goals, p2.goals)
        result = self.p < p2
        self.assertEqual(result, f"{p2.name} is a top goal scorer! S/he scored more than {self.p.name}.")


    def test_comparison_less_than_or_equal(self):
        p2 = SoccerPlayer("Test22", 18, 2, "Juventus")

        with self.assertRaises(TypeError):
            result = self.p <= p2


if __name__ == "__main__":
    main()