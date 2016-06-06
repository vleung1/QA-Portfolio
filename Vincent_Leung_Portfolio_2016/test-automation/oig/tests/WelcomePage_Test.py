from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the homepage loads
class WelcomePageTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(WelcomePageTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="high")
    def test_WelcomePageTest(self):
        welcome_page_obj = WelcomePage(self.driver)
        welcome_page_obj._verify_page()

    def tearDown(self):
        super(WelcomePageTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



