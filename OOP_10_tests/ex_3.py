from main import IntegerList

# Submit in judge

from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(4, -3, 16, 100)

    def test_init_stores_only_ints(self):
        # No args
        i = IntegerList()
        self.assertEqual(i._IntegerList__data, [])

        # With args
        i = IntegerList(1, "srt", 9.5, [1, 2,3])

        self.assertEqual(i._IntegerList__data, [1])

    def test_get_data(self):
        result = self.integer_list.get_data()

        expected = [4, -3, 16, 100]
        self.assertEqual(expected, result)

    def test_add_not_integer_raises(self):
        result = self.integer_list.get_data()

        expected = [4, -3, 16, 100]
        self.assertEqual(expected, result)

        # Act
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("str")
        self.assertEqual(str(ex.exception), "Element is not Integer")

        result = self.integer_list.get_data()

        expected = [4, -3, 16, 100]
        self.assertEqual(expected, result)

    def test_add(self):
        result = self.integer_list.get_data()

        expected = [4, -3, 16, 100]
        self.assertEqual(expected, result)

        result = self.integer_list.add(5)

        expected = [4, -3, 16, 100, 5]
        self.assertEqual(expected, result)
        result = self.integer_list.get_data()
        self.assertEqual(expected, result)
        self.assertEqual(expected, self.integer_list._IntegerList__data)

    def test_remove_index_invalid_index_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(4)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 4)

        # Index is greater than length
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(5)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 4)

    def test_remove_index(self):
        self.assertEqual(len(self.integer_list.get_data()), 4)
        self.assertEqual(self.integer_list.get_data()[2], 16)

        result = self.integer_list.remove_index(2)

        self.assertEqual(16, result)
        self.assertEqual(len(self.integer_list.get_data()), 3)
        self.assertEqual(self.integer_list.get_data()[2], 100)

    def test_get_invalid_index_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(4)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(5)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 4)

    def test_get(self):
        self.assertEqual(len(self.integer_list.get_data()), 4)
        self.assertEqual(self.integer_list.get_data()[2], 16)

        result = self.integer_list.get(2)
        self.assertEqual(result, 16)
        self.assertEqual(len(self.integer_list.get_data()), 4)

    def test_insert_invalid_index_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 4)
        invalid_index = len(self.integer_list.get_data()) + 1

        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(invalid_index, 101)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 4)

        invalid_index +=1
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(invalid_index, 101)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integer_list.get_data()), 4)

    def test_insert_invalid_value_raises(self):
        self.assertEqual(len(self.integer_list.get_data()), 4)

        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(2, "asd")
        self.assertEqual(str(ex.exception), "Element is not Integer")

        self.assertEqual(len(self.integer_list.get_data()), 4)

    def test_insert(self):
        self.assertEqual(len(self.integer_list.get_data()), 4)
        self.assertEqual(self.integer_list.get_data()[2], 16)

        result = self.integer_list.insert(2, 101)

        self.assertIsNone(result)
        self.assertEqual(len(self.integer_list.get_data()), 5)
        self.assertEqual(self.integer_list.get_data()[2], 101)

    def test_get_biggest(self):
        result = self.integer_list.get_biggest()

        self.assertEqual(100, result)

        self.integer_list.insert(2, 200)

        result = self.integer_list.get_biggest()

        self.assertEqual(200, result)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_data()[2], 16)

        result = self.integer_list.get_index(16)
        self.assertEqual(result, 2)

        self.integer_list.add(16)
        self.assertEqual(self.integer_list.get_data()[4], 16)

        result = self.integer_list.get_index(16)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    main()