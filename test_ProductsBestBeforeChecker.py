import os
import subprocess
import unittest

def call_command(command):
    return subprocess.check_output(command, shell=True).rstrip().decode("utf-8")

class TestProductsBestBeforeChecker(unittest.TestCase):

    def test_ValidDateWithDashes(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_dashes.csv")
        self.assertEqual(version, value)

    def test_ValidDateWithPoints(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_points.csv")
        self.assertEqual(version, value)

    def test_ValidDateWithSlashes(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_slashes.csv")
        self.assertEqual(version, value)

    def test_ValidDateWithSpaces(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_spaces.csv")
        self.assertEqual(version, value)

    def test_ValidDateWithoutDay(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/valid_without_day.csv")
        self.assertEqual(version, value)

    def test_ValidDateShortenedYear(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/valid_with_shortened_year.csv")
        self.assertEqual(version, value)

    def test_InvalidDateWithDashes(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_dashes.csv")
        self.assertEqual(version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithPoints(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_points.csv")
        self.assertEqual(version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithSlashes(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_slashes.csv")
        self.assertEqual(version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithSpaces(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_spaces.csv")
        self.assertEqual(version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-12", value)

    def test_InvalidDateWithoutDay(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_without_day.csv")
        self.assertEqual(version + "\r\n\r\nabc 2022-11-15\r\ndef 2022-06-15\r\nghi 2022-11-15\r\njkl 2022-06-15", value)

    def test_InvalidDateShortenedYear(self):
        version = call_command("python ProductsBestBeforeChecker.py --version")
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_shortened_year.csv")
        self.assertEqual(version + "\r\n\r\nabc 2022-11-22\r\ndef 2022-06-15", value)

if __name__ == '__main__':
    unittest.main()
