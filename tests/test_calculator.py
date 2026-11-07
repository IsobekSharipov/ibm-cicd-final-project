"""Unit tests discovered by nose2."""

import unittest

from app.calculator import add, subtract


class CalculatorTests(unittest.TestCase):
    """Verify the sample application logic."""

    def test_add(self):
        """Adding two integers returns their sum."""
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        """Subtracting two integers returns their difference."""
        self.assertEqual(subtract(8, 3), 5)


if __name__ == "__main__":
    unittest.main()
