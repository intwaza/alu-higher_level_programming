#!/usr/bin/python3
"""
Unit tests for Base class
Run with: python3 -m unittest test_base.py
"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset Base.__nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up any test files"""
        test_files = ["Rectangle.json", "Square.json", "Base.json"]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)

    def test_init_with_id(self):
        """Test Base initialization with id"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_init_without_id(self):
        """Test Base initialization without id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_init_mixed(self):
        """Test Base initialization mixed with and without id"""
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 89)
        self.assertEqual(b3.id, 2)

    def test_init_with_zero_id(self):
        """Test Base initialization with id = 0"""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_init_with_negative_id(self):
        """Test Base initialization with negative id"""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_to_json_string_empty_list(self):
        """Test to_json_string with empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")
        self.assertIsInstance(result, str)

    def test_to_json_string_none(self):
        """Test to_json_string with None"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")
        self.assertIsInstance(result, str)

    def test_to_json_string_valid_list(self):
        """Test to_json_string with valid list"""
        list_dict = [{"id": 1, "width": 10, "height": 7}]
        result = Base.to_json_string(list_dict)
        expected = '[{"id": 1, "width": 10, "height": 7}]'
        self.assertEqual(result, expected)
        self.assertIsInstance(result, str)

    def test_to_json_string_multiple_dicts(self):
        """Test to_json_string with multiple dictionaries"""
        list_dict = [
            {"id": 1, "width": 10, "height": 7},
            {"id": 2, "width": 5, "height": 3}
        ]
        result = Base.to_json_string(list_dict)
        parsed_result = json.loads(result)
        self.assertEqual(len(parsed_result), 2)
        self.assertEqual(parsed_result[0]["id"], 1)
        self.assertEqual(parsed_result[1]["id"], 2)

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string"""
        result = Base.from_json_string("")
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)

    def test_from_json_string_valid(self):
        """Test from_json_string with valid JSON string"""
        json_str = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(json_str)
        expected = [{"id": 1, "width": 10}]
        self.assertEqual(result, expected)
        self.assertIsInstance(result, list)

    def test_from_json_string_multiple(self):
        """Test from_json_string with multiple objects"""
        json_str = '[{"id": 1, "width": 10}, {"id": 2, "width": 5}]'
        result = Base.from_json_string(json_str)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 2)

    def test_save_to_file_none(self):
        """Test save_to_file with None"""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list"""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_rectangles(self):
        """Test save_to_file with Rectangle objects"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        
        data = json.loads(content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["width"], 10)
        self.assertEqual(data[0]["height"], 7)
        self.assertEqual(data[1]["width"], 2)
        self.assertEqual(data[1]["height"], 4)

    def test_save_to_file_squares(self):
        """Test save_to_file with Square objects"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        
        data = json.loads(content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["size"], 5)
        self.assertEqual(data[1]["size"], 7)

    def test_create_rectangle(self):
        """Test create method for Rectangle"""
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_create_rectangle_partial(self):
        """Test create method for Rectangle with partial attributes"""
        r = Rectangle.create(width=5, height=3)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)

    def test_create_square(self):
        """Test create method for Square"""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_create_square_partial(self):
        """Test create method for Square with partial attributes"""
        s = Square.create(size=7)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 7)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)

    def test_load_from_file_rectangles(self):
        """Test load_from_file with Rectangle objects"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 7)
        self.assertEqual(rectangles[1].width, 2)
        self.assertEqual(rectangles[1].height, 4)

    def test_load_from_file_squares(self):
        """Test load_from_file with Square objects"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[1].size, 7)

    def test_json_serialization_round_trip(self):
        """Test complete serialization cycle"""
        # Create objects
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        original_rectangles = [r1, r2]
        
        # Convert to dictionaries
        dict_list = [r.to_dictionary() for r in original_rectangles]
        
        # Convert to JSON string
        json_str = Base.to_json_string(dict_list)
        
        # Convert back to dictionaries
        loaded_dicts = Base.from_json_string(json_str)
        
        # Convert back to objects
        loaded_rectangles = [Rectangle.create(**d) for d in loaded_dicts]
        
        # Verify
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].width, original_rectangles[0].width)
        self.assertEqual(loaded_rectangles[1].width, original_rectangles[1].width)


if __name__ == '__main__':
    unittest.main()