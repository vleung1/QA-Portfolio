from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the biography of the Inspector General shows
class InspectorGeneralTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(InspectorGeneralTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="high")
    def test_InspectorGeneralTest(self):
        inspector_general_obj = WelcomePage(self.driver)
        inspector_general_obj.click_inspector_general_link()        

    def tearDown(self):
        super(InspectorGeneralTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



