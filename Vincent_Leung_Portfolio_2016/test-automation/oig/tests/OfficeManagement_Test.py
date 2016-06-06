from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the Office of Management shows
class OfficeManagementTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(OfficeManagementTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="medium")
    def test_OfficeManagementTest(self):
        office_management_obj = WelcomePage(self.driver)
        office_management_obj.click_office_management_link()        

    def tearDown(self):
        super(OfficeManagementTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



