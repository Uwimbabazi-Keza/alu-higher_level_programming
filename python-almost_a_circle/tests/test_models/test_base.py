#!/usr/bin/python3
"""Unittest for Base module"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):
    """testing Base"""

    def test_none(self):
        """test"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_norm(self):
        """test"""
        base1 = Base()
        base2 = Base(5)
        self.assertEqual(base1.id, -1)
        self.assertEqual(base1.id, 5)

    def test_to_json_none(self):
        self.assertEqual('[]', Base.to_json_string(None))

    def test_to_json_empty(self):
        self.assertEqual('[]', Base.to_json_string([])

    def test_to_json_typeS(self):
        s = Square(8, 5, 3)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

        self.assertEqual(Base.to_json_string([{'id': 6}]), '[{"id": 6}]')

    def test_from_json_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_type(self):
        self.assertEqual(type(Base.from_json_string('[{"x": self.x}]')), list)

    def test_save_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_file_rectangle(self):
        rec = Rectangle(12, 6, 3, 7)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read())

    def test_load_file_empty(self):
        load = Rectangle.load_from_file()
        self.assertEqual([], load)

    def test_load_file_rectangle(self):
        rec = Rectangle(12, 8, 1, 9)
        Rectangle.save_to_file([rec])
        load = Rectangle.load_from_file()
        self.assertEqual(str(rec), str(load[0]))

    def test_load_file_square(self):
        sqr = Square(9, 3, 1)
        Square.save_to_file([sqr])
        load = Square.load_from_file()
        self.assertEqual(str(sqr), str(load[0]))

    def test_load_file__type_rec(self):
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        load = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in load))

    def test_load_file_type_sqr(self):
        sqr = Square(10, 2, 1)
        Square.save_to_file([sqr])
        load = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in load))
    def test_create_isNot(self):
        rec = Rectangle(6, 4, 2, 7)
        rec_dict = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dict)
        self.assertIsNot(rec, rec2)

    def test_create_rectangle(self):
        rec = Rectangle(15, 7, 4, 10)
        rec_dict = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dict)
        self.assertEqual("[Rectangle] (3) 4/10 - 15/7", str(rec))

if __name__ == '__main__':
    unittest.main()
