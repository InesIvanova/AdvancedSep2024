from main import Worker


# Submit from here on in judge

from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_init(self):
        w = Worker("Test", 1000, 100)

        self.assertEqual(w.name, "Test")
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 100)
        self.assertEqual(w.money, 0)

    def test_worker_works_no_energy_raises(self):
        # Create worker with no energy
        # Arrange
        w = Worker("Test", 1000, 0)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")

        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

        # Test if energy is less than zero
        w = Worker("Test", 1000, -1)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, -1)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")

        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, -1)

    def test_worker_works(self):
        w = Worker("Test", 1000, 100)

        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)

        result = w.work()

        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 99)

        self.assertIsNone(result)

    def test_worker_rest(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.energy, 100)

        result = w.rest()

        self.assertEqual(w.energy, 101)
        self.assertIsNone(result)

    def test_info(self):
        w = Worker("Test", 1000, 100)

        result = w.get_info()
        expected_result = "Test has saved 0 money."

        self.assertEqual(expected_result, result)

        w.work()
        result = w.get_info()
        expected_result = "Test has saved 1000 money."
        self.assertEqual(expected_result, result)

    def test_worker_works_money_increases(self):
        w = Worker("Test", 1000, 100)

        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)

        expected_energy = w.energy - 3
        expected_money = w.money + w.salary * 3

        w.work()
        w.work()
        w.work()

        self.assertEqual(expected_money, w.money)
        self.assertEqual(expected_energy, w.energy)


if __name__ == "__main__":
    main()