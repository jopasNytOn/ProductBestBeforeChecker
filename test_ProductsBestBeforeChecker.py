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

if __name__ == '__main__':
    unittest.main()
