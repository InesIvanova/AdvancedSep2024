from main import Car


# Submit

from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car("Test", "testModel", 2, 30)

    def test_init(self):
        self.assertEqual(self.car.make, "Test")
        self.assertEqual(self.car.model, "testModel")
        self.assertEqual(self.car.fuel_consumption, 2)
        self.assertEqual(self.car.fuel_capacity, 30)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("", "testModel", 2, 30)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

        with self.assertRaises(Exception) as ex:
            Car(None, "testModel", 2, 30)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("Test", "", 2, 30)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

        with self.assertRaises(Exception) as ex:
            Car("Test", None, 2, 30)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("Test", "testModel", 0, 30)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("Test", "testModel", -2, 30)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("Test", "testModel", 2, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("Test", "testModel", 2, -2)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_can_not_be_negative(self):
        c = Car("Test", "testModel", 2, 20)

        self.assertEqual(c.fuel_amount, 0)

        with self.assertRaises(Exception) as ex:
            c.fuel_amount = -1

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")
        self.assertEqual(c.fuel_amount, 0)

    def test_refuel_zero_or_negative_fuel_raises(self):
        self.assertEqual(self.car.fuel_amount, 0)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel(self):
        self.assertEqual(self.car.fuel_amount, 0)

        self.car.refuel(10)

        self.assertEqual(self.car.fuel_amount, 10)
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount, 11)

        # Overflow sets it to fuel capacity
        self.assertEqual(self.car.fuel_capacity, 30)

        self.car.refuel(self.car.fuel_capacity + 1)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_not_enough_fuel_raises(self):
        self.car.refuel(self.car.fuel_capacity)

        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            self.car.drive(3000)

        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive(self):
        self.car.refuel(self.car.fuel_capacity)
        self.assertEqual(self.car.fuel_amount, 30)

        self.car.drive(1000)

        self.assertEqual(self.car.fuel_amount, 10)

    def test_drive_just_enough_fuel(self):
        self.car.refuel(self.car.fuel_capacity)
        self.assertEqual(self.car.fuel_amount, 30)

        self.car.drive(1500)

        self.assertEqual(self.car.fuel_amount, 0)





if __name__ == "__main__":
    main()