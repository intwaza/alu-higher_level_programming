#!/usr/bin/python3
"""
Unit tests for Rectangle class
Run with: python3 -m unittest test_rectangle.py
"""

import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Reset Base.__nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up any test files"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_inherits_from_base(self):
        """Test Rectangle inherits from Base"""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_rectangle_creation_basic(self):
        """Test Rectangle creation with width and height only"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rectangle_creation_with_x(self):
        """Test Rectangle creation with x parameter"""
        r = Rectangle(10, 2, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

    def test_rectangle_creation_with_x_y(self):
        """Test Rectangle creation with x and y parameters"""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_creation_with_all_params(self):
        """Test Rectangle creation with all parameters"""
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_rectangle_id_assignment(self):
        """Test Rectangle ID assignment"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(5, 3)
        r3 = Rectangle(1, 1, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_width_validation_type(self):
        """Test width validation for type"""
        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10.5, 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            Rectangle(None, 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_width_validation_value(self):
        """Test width validation for value"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(-1, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_validation_type(self):
        """Test height validation for type"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2.5)
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_height_validation_value(self):
        """Test height validation for value"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, -1)
        self.assertEqual(str(cm.exception), "height must be > 0")

        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 0)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_x_validation_type(self):
        """Test x validation for type"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, "3")
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_x_validation_value(self):
        """Test x validation for value"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_validation_type(self):
        """Test y validation for type"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2)
            r.y = []
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_y_validation_value(self):
        """Test y validation for value"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_property_setters(self):
        """Test property setters work correctly"""
        r = Rectangle(10, 2)
        r.width = 5
        r.height = 7
        r.x = 3
        r.y = 4
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_property_setters_validation(self):
        """Test property setters with validation"""
        r = Rectangle(10, 2)
        
        with self.assertRaises(ValueError):
            r.width = -10
        
        with self.assertRaises(TypeError):
            r.height = "5"

    def test_area_calculation(self):
        """Test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        
        r2 = Rectangle(8, 7)
        self.assertEqual(r2.area(), 56)
        
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.area(), 1)

    def test_display_basic(self):
        """Test display method without x and y"""
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_display_with_x(self):
        """Test display method with x offset"""
        r = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_display_with_y(self):
        """Test display method with y offset"""
        r = Rectangle(2, 2, 0, 2)
        expected_output = "\n\n##\n##\n"
        
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_display_with_x_and_y(self):
        """Test display method with both x and y offsets"""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        
        self.assertEqual(output, expected_output)

    def test_str_method(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")
        
        r3 = Rectangle(1, 2)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 1/2")

    def test_update_with_args(self):
        """Test update method with positional arguments"""
        r = Rectangle(10, 10, 10, 10)
        
        r.update(89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)  # Should remain unchanged
        
        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)  # Should remain unchanged
        
        r.update(89, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 10)  # Should remain unchanged
        
        r.update(89, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 10)  # Should remain unchanged
        
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_with_kwargs(self):
        """Test update method with keyword arguments"""
        r = Rectangle(10, 10, 10, 10)
        
        r.update(height=1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 10)  # Should remain unchanged
        
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)
        
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)

    def test_update_args_priority_over_kwargs(self):
        """Test that args takes priority over kwargs"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=4, width=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)  # Should not be updated by kwargs

    def test_update_invalid_kwargs(self):
        """Test update with invalid keyword arguments"""
        r = Rectangle(10, 10, 10, 10)
        original_str = str(r)
        r.update(invalid_attr=99)
        # Should remain unchanged since invalid_attr doesn't exist
        self.assertEqual(str(r), original_str)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(10, 2, 1, 9, 1)
        r_dict = r.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r_dict, expected)
        self.assertIsInstance(r_dict, dict)

    def test_to_dictionary_default_values(self):
        """Test to_dictionary with default values"""
        r = Rectangle(5, 3)
        r_dict = r.to_dictionary()
        expected = {'x': 0, 'y': 0, 'id': 1, 'height': 3, 'width': 5}
        self.assertEqual(r_dict, expected)

    def test_to_dictionary_update_cycle(self):
        """Test using to_dictionary with update"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        
        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)
        self.assertIsNot(r1, r2)  # Different objects

    def test_rectangle_immutable_after_to_dictionary(self):
        """Test that modifying dictionary doesn't affect original object"""
        r = Rectangle(10, 2, 1, 9, 1)
        r_dict = r.to_dictionary()
        r_dict['width'] = 999
        self.assertEqual(r.width, 10)  # Should remain unchanged


if __name__ == '__main__':
    unittest.main()