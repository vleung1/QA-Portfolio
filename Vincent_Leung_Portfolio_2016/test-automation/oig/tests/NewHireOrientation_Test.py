from oig.Constants                             import TT_Constants
from oig.pages.WelcomePage                     import WelcomePage
from oig.pages.NewHireOrientationPage          import NewHireOrientationPage
from oig.BaseTestCase                          import BaseTestCase
import unittest
import nose
from nose.plugins.attrib                       import attr


#verify Planning Documents page loads and verify the content update link loads
class NewHireOrientationTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(NewHireOrientationTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(TT_Constants['Base_URL'])

    @attr(priority="medium") 
    def test_NewHireOrientationTest(self):
        new_hire_obj = WelcomePage(self.driver)
        new_hire_obj.click_new_hire_link()
        new_hire_obj = NewHireOrientationPage(self.driver)
        new_hire_obj.verify_before_report()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_first_day()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_no_fear()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_pay_leave()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_benefits()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_workers_comp()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_ethics()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_whistleblower_protection()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_hr_connect()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_forgotten()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_constitution_initiative()
        self.driver.execute_script("window.history.go(-1)")
        new_hire_obj.verify_abbreviations()
        self.driver.execute_script("window.history.go(-1)")
        """
        This download test is deprecated. PDF links are no longer active.
        
        new_hire_obj.click_and_download()
        """

    def tearDown(self):
        super(NewHireOrientationTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



