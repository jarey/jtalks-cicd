import unittest
from jtalks.Tomcat import Tomcat
from jtalks.backup.Backuper import Backuper
from jtalks.settings.ScriptSettings import ScriptSettings


class TomcatTest(unittest.TestCase):
  def test_paths(self):
    tomcat = Tomcat(Backuper("/", None, None), ScriptSettings(build=None, project='project1', env='unit-test'))

    self.assertEquals('project1.xml', tomcat.get_config_name())
    self.assertEquals('project1.ehcache.xml', tomcat.get_ehcache_config_name())
    self.assertEquals('location overriden by project config/conf/Catalina/localhost',
                      tomcat.get_config_folder_location())
    self.assertEquals('location overriden by project config/webapps', tomcat.get_web_apps_location())
    self.assertTrue(tomcat.get_config_file_location().endswith('.jtalks/environments/unit-test/project1.xml'))


if __name__ == '__main__':
  unittest.main()