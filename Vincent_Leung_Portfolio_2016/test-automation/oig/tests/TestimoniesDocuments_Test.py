from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the Testimonies & Documents page shows
class TestimoniesDocumentsTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(TestimoniesDocumentsTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_TestimoniesDocumentsTest(self):
        testimonies_documents_obj = WelcomePage(self.driver)
        testimonies_documents_obj.click_testimonies_documents_link()        

    def tearDown(self):
        super(TestimoniesDocumentsTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



