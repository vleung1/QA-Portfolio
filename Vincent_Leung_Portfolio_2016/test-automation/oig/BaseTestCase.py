from selenium import webdriver
import unittest
from oig.Constants import TT_Constants


#wrap selenium calls to open a specific browser, maximize window, and navigate to a page
class BaseTestCase(object):

  def setUp(self):
      if TT_Constants['Browser'].lower() == "firefox":
         """
         set Firefox preferences to bypass the file download confirmation window
         """
         profile = webdriver.FirefoxProfile()
         profile.set_preference('browser.download.folderList', 2)
         profile.set_preference('browser.download.manager.showWhenStarting', False)
         profile.set_preference('browser.helperApps.alwaysAsk.force', False)
         profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf,application/x-pdf,image/jpeg,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document')
         profile.set_preference('plugin.disable_full_page_plugin_for_types', 'application/pdf,image/jpeg,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document')
         profile.set_preference('pdfjs.disabled', True)
      	 self.driver = webdriver.Firefox(profile)
         self.driver.maximize_window()
      elif TT_Constants['Browser'].lower() == "chrome":
      	 self.driver = webdriver.Chrome()
         self.driver.maximize_window()
      elif TT_Constants['Browser'].lower() == "ie": 
         self.driver = webdriver.Ie()
         self.driver.maximize_window()
      else:
      	raise Exception("This browser is not supported at the moment.")

  def navigate_to_page(self, url):
      self.driver.get(url)

  def tearDown(self):
  	  self.driver.quit()
