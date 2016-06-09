from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the Restore Act shows, and check for presence of the correct contact email link
class RestoreActTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(RestoreActTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_RestoreActTest(self):
        restore_act_obj = WelcomePage(self.driver)
        restore_act_obj.click_restore_act_link()        

    def tearDown(self):
        super(RestoreActTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



