import os
import time
import unittest
from tests import working_directory
import subprocess
from kedehub.kedegit import KedeGit

class KedeGitTest(unittest.TestCase):

    def _make_kedegit(self, project_name):
        return KedeGit(project_name)

    def setUp(self):
        print()
        print(self.id())
        self.current_directory = os.path.abspath(os.path.dirname(__file__))
        self.working_directory = working_directory
        self.proc = subprocess.Popen(['/Users/dimitarbakardzhiev/git/kedematcher/venv39/bin/python3', '-m' ,'tests'],
                                     cwd = '/Users/dimitarbakardzhiev/git/kedehub_server/',
                                     stdin=subprocess.PIPE)
        time.sleep(5.5)
        self.kedegit = self._make_kedegit('test')

    def tearDown(self):
        self.proc.communicate(input=b"stop", timeout=5)
        self.proc.terminate()
        time.sleep(5.5)