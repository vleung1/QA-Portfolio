from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the SBLF initiative shows, and check for header for list of reports
class SblfTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SblfTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="medium")
    def test_SblfTest(self):
        sblf_obj = WelcomePage(self.driver)
        sblf_obj.click_sblf_link()        

    def tearDown(self):
        super(SblfTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



