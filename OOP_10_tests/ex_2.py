from main import Cat


# Submit from here on in judge
from unittest import TestCase, main


class CatTests(TestCase):
    def test_init(self):
        c = Cat("Test")

        self.assertEqual(c.name, "Test")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)

    def test_cat_eats(self):
        c = Cat("Test")

        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)

        result = c.eat()

        self.assertIsNone(result)

        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size, 1)

    def test_cat_eats_already_def_raises(self):
        # Arrange
        c = Cat("Test")
        c.eat()

        self.assertEqual(c.size, 1)
        self.assertTrue(c.sleepy)
        self.assertTrue(c.fed)

        # ACT
        with self.assertRaises(Exception) as ex:
            c.eat()

        # ASSERT
        self.assertEqual(str(ex.exception), "Already fed.")
        self.assertEqual(c.size, 1)
        self.assertTrue(c.sleepy)
        self.assertTrue(c.fed)

    def test_sleep_cat_not_fed_raises(self):
        c = Cat("Test")

        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)

        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual(str(ex.exception), "Cannot sleep while hungry")

        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)

    def test_cat_sleeps(self):
        c = Cat("Test")
        c.eat()

        self.assertTrue(c.sleepy)

        result = c.sleep()
        self.assertFalse(c.sleepy)
        self.assertIsNone(result)


if __name__ == "__main__":
    main()