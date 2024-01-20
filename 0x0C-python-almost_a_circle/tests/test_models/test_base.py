#!/usr/bin/python3
# test_base.py
# Michael Aroworade
"""Defines unittests for base.py.

Unittest classes:
    TestBaseInstantiation - line 23
    TestBaseToJsonString - line 76
    TestBaseSaveToFile - line 107
    TestBaseFromJsonString - line 173
    TestBaseLoadFromFile - line 278
    TestBaseSaveToFileCsv - line 337
    TestBaseLoadFromFile - line 407
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b1 = Base()
        b1.id = 15
        self.assertEqual(15, b1.id)

    def test_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instance)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)


class TestBaseToJsonString(unittest.TestCase):
    """Unittests for testing to_json_string method"""
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(2, 3, 5, 19, 2)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_empty_list(self):
        self.assertEqual([], Base.to_json_string([]))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def setUp(self):
        """Create Rectangle and Square instance"""
        self.r1 = Rectangle(10, 7, 2, 8, 5)
        self.r2 = Rectangle(2, 4, 1, 2, 3)
        self.s1 = Square(10, 7, 2, 8)
        self.s2 = Square(8, 1, 2, 3)

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        Rectangle.save_to_file([self.r1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([self.s1])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        Square.save_to_file([self.s1, self.s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBaseCreate(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittest for testing load_from_file method of Base class."""

    def setUp(self):
        self.r1 = Rectangle(10, 7, 2, 8, 1)
        self.r2 = Rectangle(2, 4, 5, 6, 2)
        self.s1 = Square(5, 1, 3, 3)
        self.s2 = Square(9, 5, 2, 3)

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        Rectangle.save_to_file([self.r1, self.r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(self.r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        Rectangle.save_to_file([self.r1, self.r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(self.r2), str(list_rectangles_output[1]))

    def test_load_from_file_first_square(self):
        Square.save_to_file([self.s1, self.s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(self.s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        Square.save_to_file([self.s1, self.s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(self.s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        Square.save_to_file([self.s1, self.s2])
        output = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))  # all(type(obj) == Square for obj in output)

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBaseSaveToFileCsv(unittest.TestCase):
    """Unittest for testing save_to_file_csv method of Base class."""

    def setUp(self):
        self.r1 = Rectangle(10, 7, 2, 8, 5)
        self.r2 = Rectangle(2, 4, 1, 2, 3)
        self.s1 = Square(10, 7, 2, 8)
        self.s2 = Square(8, 1, 2, 3)

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        Rectangle.save_to_file_csv([self.r1])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        Rectangle.save_to_file_csv([self.r1, self.r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        Square.save_to_file_csv([self.s1])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        Square.save_to_file_csv([self.s1, self.s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        Square.save_to_file_csv([self.s1])
        Square.save_to_file_csv([self.s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBaseLoadFromFileCsv(unittest.TestCase):
    """unittest for testing load_from_file_csv method of Base class."""

    def setUp(self):
        self.r1 = Rectangle(10, 7, 2, 8, 1)
        self.r2 = Rectangle(2, 4, 5, 6, 2)
        self.s1 = Square(5, 1, 3, 3)
        self.s2 = Square(9, 5, 2, 3)

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        Rectangle.save_to_file_csv([self.r1, self.r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(self.r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        Rectangle.save_to_file_csv([self.r1, self.r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(self.r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        Rectangle.save_to_file_csv([self.r1, self.r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_csv_first_square(self):
        Square.save_to_file_csv([self.s1, self.s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(self.s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        Square.save_to_file_csv([self.s1, self.s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(self.s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        Square.save_to_file_csv([self.s1, self.s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()

