from oig.Constants            import TT_Constants
from oig.pages.OigHotlinePage import OigHotlinePage
from oig.BaseTestCase         import BaseTestCase
import unittest
import nose
from nose.plugins.attrib      import attr


#verify functionality of filling out and submitting the OIG Hotline request form
class SendRequestTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SendRequestTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(URL.replace("default", "OigOnlineHotlineForm"))
     
    @attr(priority="high") 
    def test_SendRequestTest(self):
        oig_hotline_page_obj = OigHotlinePage(self.driver)
        oig_hotline_page_obj.submit_request()

    #verify that the page does not submit when one of the required fields are not filled out
    @attr(priority="high")
    def test_SendRequestTestValidation(self):
        oig_hotline_page_obj = OigHotlinePage(self.driver)
        oig_hotline_page_obj.validation_check()

    def tearDown(self):
        super(SendRequestTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



