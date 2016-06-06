from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the Office of Investigations shows
class OfficeInvestigationsTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(OfficeInvestigationsTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="medium")
    def test_OfficeInvestigationsTest(self):
        office_investigations_obj = WelcomePage(self.driver)
        office_investigations_obj.click_office_investigations_link()        

    def tearDown(self):
        super(OfficeInvestigationsTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



