import os
import unittest
import time
from tests import working_directory
import subprocess


class KedeHubLoadDBOnceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current_directory = os.path.abspath(os.path.dirname(__file__))
        cls.working_directory = working_directory
        cls.proc = subprocess.Popen(['/Users/dimitarbakardzhiev/git/kedematcher/venv311/bin/python', '-m' ,'tests'],
                                     cwd = '/Users/dimitarbakardzhiev/git/kedehub_server/',
                                     stdin=subprocess.PIPE)
        time.sleep(6.5)

    @classmethod
    def tearDownClass(cls):
        cls.proc.communicate(input=b"stop", timeout=5)
        cls.proc.terminate()
        time.sleep(5.5)