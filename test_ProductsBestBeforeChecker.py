import datetime
import os
import subprocess
import unittest

def call_command(command):
    return subprocess.check_output(command, shell=True).rstrip().decode("utf-8")

class TestProductsBestBeforeChecker(unittest.TestCase):

    def setUp(self):
        self.version = call_command("python ProductsBestBeforeChecker.py --version")

    def helper_RemoveFile(self, days):
        os.remove("test/date_in_{}_days.csv".format(days))

    def helper_SetExpiryDate(self, days):
        self.date = datetime.date.today()
        expiry_date = self.date + datetime.timedelta(days=days)
        file = open("test/date_in_{}_days.csv".format(days), "w+")
        file.write("abc; ; {}\r\ndef; ; {}\r\n".format(expiry_date.strftime("%d-%m-%Y"), expiry_date.strftime("%d-%m-%Y")))
        file.close()
        return expiry_date.strftime("%Y-%m-%d")

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
        self.assertEqual(self.version + "\r\n\r\nabc 2001-11-22\r\ndef 2001-06-12", value)

    def test_InvalidDateWithPoints(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_points.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2001-11-22\r\ndef 2001-06-12", value)

    def test_InvalidDateWithSlashes(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_slashes.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2001-11-22\r\ndef 2001-06-12", value)

    def test_InvalidDateWithSpaces(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_spaces.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2001-11-22\r\ndef 2001-06-12", value)

    def test_InvalidDateWithoutDay(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_without_day.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2001-11-15\r\ndef 2001-06-15\r\nghi 2001-11-15\r\njkl 2001-06-15", value)

    def test_InvalidDateShortenedYear(self):
        value = call_command("python ProductsBestBeforeChecker.py test/invalid_with_shortened_year.csv")
        self.assertEqual(self.version + "\r\n\r\nabc 2001-11-22\r\ndef 2001-06-15", value)

    def test_DateIn31Days(self):
        days = 31
        expiry_date = self.helper_SetExpiryDate(days)
        value = call_command("python ProductsBestBeforeChecker.py test/date_in_{}_days.csv".format(days))
        self.assertEqual(self.version, value)
        self.helper_RemoveFile(days)

    def test_DateIn30Days(self):
        days = 30
        expiry_date = self.helper_SetExpiryDate(days)
        value = call_command("python ProductsBestBeforeChecker.py test/date_in_{}_days.csv".format(days))
        self.assertEqual(self.version + "\r\n\r\nabc {}\r\ndef {}".format(expiry_date, expiry_date), value)
        self.helper_RemoveFile(days)


if __name__ == '__main__':
    unittest.main()
