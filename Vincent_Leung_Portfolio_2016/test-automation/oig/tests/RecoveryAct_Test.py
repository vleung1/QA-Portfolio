from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.pages.RecoveryActPage   import RecoveryActPage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the Reports page shows and verify each link on the page
class RecoveryActTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(RecoveryActTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low ")
    def test_RecoveryActTest(self):
        recovery_act_obj = WelcomePage(self.driver)
        recovery_act_obj.click_recovery_act_link()
        recovery_act_obj = RecoveryActPage(self.driver)        
        recovery_act_obj.verify_recovery_documents()

    def tearDown(self):
        super(RecoveryActTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



