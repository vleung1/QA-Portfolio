from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the Office of Counsel shows
class OfficeCounselTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(OfficeCounselTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="medium")
    def test_OfficeCounselTest(self):
        office_counsel_obj = WelcomePage(self.driver)
        office_counsel_obj.click_office_counsel_link()        

    def tearDown(self):
        super(OfficeCounselTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



