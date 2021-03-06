import unittest
import os
from datetime import datetime

from mock import patch, MagicMock

from jtalks.backup.Backuper import Backuper
from jtalks.settings.ScriptSettings import ScriptSettings


class BackuperTest(unittest.TestCase):

  def test_constructor_throws_if_folder_not_finished_with_slash(self):
    self.assertRaises(ValueError, Backuper, "folder", None, db_operations)

  @patch('os.makedirs')
  def test_backup_creates_folder_to_keep_backups(self, makedirs_method):
    sut.backup()
    now = datetime.now().strftime("%Y_%m_%dT%H_%M_%S")
    folder_to_create = "/tmp/unit-test/project1/{0}".format(now) #Couldn't find a way to mock date
    makedirs_method.assert_called_with(folder_to_create)

  def test_get_project_backup_folder(self):
      self.assertEqual("/tmp/unit-test/project1", sut.get_project_backup_folder())

  @patch('os.listdir')
  def test_get_list_of_backups(self, list_dir_method):
    list_dir_method.return_value = ["1", "2"]
    self.assertEqual(["1", "2"], sut.get_list_of_backups())

db_operations = MagicMock()
sut = Backuper("/tmp/", ScriptSettings(None, "project1", "unit-test"), db_operations)

if __name__ == '__main__':
  unittest.main()
