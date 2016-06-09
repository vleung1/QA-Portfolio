from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the Inspector General Act shows
class IgActTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(IgActTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_IgActTest(self):
        ig_act_obj = WelcomePage(self.driver)
        ig_act_obj.click_ig_act_link()        

    def tearDown(self):
        super(IgActTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



