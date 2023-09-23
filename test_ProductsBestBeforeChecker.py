import os
import subprocess
import unittest

def call_command(command):
    return subprocess.check_output(command, shell=True).rstrip().decode("utf-8")

class TestProductsBestBeforeChecker(unittest.TestCase):

    def setUp(self):
        self.version = call_command("python ProductsBestBeforeChecker.py --version")

    def test_ValidDateWithDashes(self):
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_dashes.csv")
        self.assertEqual(self.version, value)

    def test_ValidDateWithPoints(self):
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_points.csv")
        self.assertEqual(self.version, value)

    def test_ValidDateWithSlashes(self):
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_slashes.csv")
        self.assertEqual(self.version, value)

    def test_ValidDateWithSpaces(self):
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_spaces.csv")
        self.assertEqual(self.version, value)

    def test_ValidDateWithoutDay(self):
        value = call_command("python ProductsBestBeforeChecker.py test/valid_without_day.csv")
        self.assertEqual(self.version, value)

    def test_ValidDateShortenedYear(self):
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_shortened_year.csv")
        self.assertEqual(self.version, value)

    def test_InvalidDateWithDashes(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_dashes.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithPoints(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_points.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithSlashes(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_slashes.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithSpaces(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_spaces.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithoutDay(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_without_day.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2022-11-15\r\ndef 2022-06-15\r\nghi 2022-11-15\r\njkl 2022-06-15", value)

    def test_InvalidDateShortenedYear(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_shortened_year.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-15", value)

if __name__ == '__main__':
    unittest.main()
