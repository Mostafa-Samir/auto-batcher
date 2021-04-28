import unittest

from auto_batcher.validation import validate_callable, validate_int


def dummy_func():
    pass


def dummy_default_func():
    pass


class ValidationTest(unittest.TestCase):

    def test_validate_callable(self):
        """Tests the validate_callable method that verifies that an object is callable
        """

        self.assertEqual(validate_callable(dummy_func, "NOT CALLABLE"), dummy_func)

        with self.assertRaisesRegex(TypeError, "NOT CALLABLE"):
            validate_callable(5, "NOT CALLABLE")

    def test_validate_callable_with_default(self):
        """Tests the validate_callable method that verifies that an object is callable with a default given
        """

        self.assertEqual(
            validate_callable(dummy_func, "NOT CALLABLE", default=dummy_default_func),
            dummy_func
        )

        self.assertEqual(
            validate_callable(5, "NOT CALLABLE", default=dummy_default_func),
            dummy_default_func
        )

        with self.assertRaisesRegex(TypeError, "NOT CALLABLE"):
            validate_callable(5, "NOT CALLABLE", default=6)

    def test_validate_int(self):
        """Tests the validate_int method that verifies that an object is an integer
        """

        self.assertEqual(validate_int(50, "NOT INT"), 50)

        with self.assertRaisesRegex(TypeError, "NOT INT"):
            validate_int("50", "NOT INT")

    def test_validate_int_with_default(self):
        """Tests the validate_int method that verifies that an object is an int with a default given
        """

        self.assertEqual(
            validate_int(50, "NOT INT", default=100),
            50
        )

        self.assertEqual(
            validate_int("50", "NOT INT", default=100),
            100
        )

        with self.assertRaisesRegex(TypeError, "NOT INT"):
            validate_int("50", "NOT INT", default="100")
