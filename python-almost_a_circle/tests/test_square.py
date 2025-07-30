#!/usr/bin/python3
"""
Unit tests for Square class
Run with: python3 -m unittest test_square.py
"""

import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Reset Base.__nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up any test files"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_inherits_from_rectangle(self):
        """Test Square inherits from Rectangle and Base"""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_square_creation_basic(self):
        """Test Square creation with size only"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_square_creation_with_x(self):
        """Test Square creation with x parameter"""
        s = Square(5, 2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

    def test_square_creation_with_x_y(self):
        """Test Square creation with x and y parameters"""
        s = Square(5, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_creation_with_all_params(self):
        """Test Square creation with all parameters"""
        s = Square(5, 2, 3, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 89)

    def test_square_id_assignment(self):
        """Test Square ID assignment"""
        s1 = Square(5)
        s2 = Square(3)
        s3 = Square(1, 0, 0, 12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)

    def test_size_property_getter(self):
        """Test size property getter"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.size, s.width)
        self.assertEqual(s.size, s.height)

    def test_size_property_setter(self):
        """Test size property setter"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_validation_type(self):
        """Test size validation for type"""
        s = Square(5)
        
        with self.assertRaises(TypeError) as cm:
            s.size = "9"
        self.assertEqual(str(cm.exception), "width must be an integer")
        
        with self.assertRaises(TypeError) as cm:
            s.size = 9.5
        self.assertEqual(str(cm.exception), "width must be an integer")
        
        with self.assertRaises(TypeError) as cm:
            Square("5")
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_size_validation_value(self):
        """Test size validation for value"""
        s = Square(5)
        
        with self.assertRaises(ValueError) as cm:
            s.size = 0
        self.assertEqual(str(cm.exception), "width must be > 0")
        
        with self.assertRaises(ValueError) as cm:
            s.size = -1
        self.assertEqual(str(cm.exception), "width must be > 0")
        
        with self.assertRaises(ValueError) as cm:
            Square(-5)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_square_x_y_validation(self):
        """Test x and y validation (inherited from Rectangle)"""
        with self.assertRaises(TypeError) as cm:
            Square(5, "2")
        self.assertEqual(str(cm.exception), "x must be an integer")
        
        with self.assertRaises(TypeError) as cm:
            Square(5, 2, "3")
        self.assertEqual(str(cm.exception), "y must be an integer")
        
        with self.assertRaises(ValueError) as cm:
            Square(5, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")
        
        with self.assertRaises(ValueError) as cm:
            Square(5, 2, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_square_inherits_methods(self):
        """Test Square inherits methods from Rectangle"""
        s = Square(5)
        # Test that methods exist and are callable
        self.assertTrue(hasattr(s, 'area'))
        self.assertTrue(hasattr(s, 'display'))
        self.assertTrue(hasattr(s, 'update'))
        self.assertTrue(callable(s.area))
        self.assertTrue(callable(s.display))
        self.assertTrue(callable(s.update))

    def test_square_area_calculation(self):
        """Test area calculation for Square"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        
        s2 = Square(3)
        self.assertEqual(s2.area(), 9)
        
        s3 = Square(1)
        self.assertEqual(s3.area(), 1)

    def test_square_display_basic(self):
        """Test display method for Square"""
        s = Square(2)
        expected_output = "##\n##\n"
        
        with StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_square_display_with_size_3(self):
        """Test display method for larger Square"""
        s = Square(3)
        expected_output = "###\n###\n###\n"
        
        with StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_square_display_with_x_y(self):
        """Test display method with x and y offsets"""
        s = Square(2, 2, 1)
        expected_output = "\n  ##\n  ##\n"
        
        with StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_square_str_method(self):
        """Test __str__ method for Square"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        
        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        
        s4 = Square(4, 1, 2, 99)
        self.assertEqual(str(s4), "[Square] (99) 1/2 - 4")

    def test_square_update_with_args(self):
        """Test update method with positional arguments for Square"""
        s = Square(5)
        
        s.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)  # Should remain unchanged
        
        s.update(1, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 0)  # Should remain unchanged
        
        s.update(1, 2, 3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 0)  # Should remain unchanged
        
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_update_with_kwargs(self):
        """Test update method with keyword arguments for Square"""
        s = Square(5)
        
        s.update(x=12)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.size, 5)  # Should remain unchanged
        
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)
        
        s.update(size=7, id=89, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.y, 1)

    def test_square_update_args_priority(self):
        """Test that args takes priority over kwargs for Square"""
        s = Square(5)
        s.update(89, 3, size=7, id=100)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 3)
        # kwargs should be ignored when args are present

    def test_square_to_dictionary(self):
        """Test to_dictionary method for Square"""
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s_dict, expected)
        self.assertIsInstance(s_dict, dict)

    def test_square_to_dictionary_default_values(self):
        """Test to_dictionary with default values"""
        s = Square(5)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'x': 0, 'size': 5, 'y': 0}
        self.assertEqual(s_dict, expected)

    def test_square_to_dictionary_update_cycle(self):
        """Test using to_dictionary with update for Square"""
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        
        s2 = Square(1, 1)
        s2.update(**s1_dict)
        
        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)
        self.assertIsNot(s1, s2)  # Different objects

    def test_square_save_and_load(self):
        """Test save_to_file and load_from_file for Square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        
        # Verify file was created
        self.assertTrue(os.path.exists("Square.json"))
        
        # Load squares from file
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        
        # Verify loaded squares
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[1].size, 7)
        self.assertEqual(squares[1].x, 9)
        self.assertEqual(squares[1].y, 1)

    def test_square_save_empty_list(self):
        """Test save_to_file with empty list"""
        Square.save_to_file([])
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_square_save_none(self):
        """Test save_to_file with None"""
        Square.save_to_file(None)
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_square_load_nonexistent_file(self):
        """Test load_from_file when file doesn't exist"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_square_create_method(self):
        """Test create class method for Square"""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_create_partial(self):
        """Test create method with partial attributes"""
        s = Square.create(size=7)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 7)

    def test_square_vs_rectangle_difference(self):
        """Test that Square and Rectangle have different __str__ and to_dictionary"""
        s = Square(5, 1, 2, 3)
        r = Rectangle(5, 5, 1, 2, 3)
        
        # Different string representations
        self.assertNotEqual(str(s), str(r))
        self.assertIn("Square", str(s))
        self.assertIn("Rectangle", str(r))
        
        # Different dictionary representations
        s_dict = s.to_dictionary()
        r_dict = r.to_dictionary()
        self.assertIn("size", s_dict)
        self.assertNotIn("size", r_dict)
        self.assertIn("width", r_dict)
        self.assertIn("height", r_dict)


if __name__ == '__main__':
    unittest.main()