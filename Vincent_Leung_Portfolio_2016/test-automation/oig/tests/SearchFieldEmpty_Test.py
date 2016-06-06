from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#test the search field functionality on the OIG homepage by submitting an empty search and ensuring correct error message appears
class SearchFieldEmptyTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SearchFieldEmptyTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_SearchFieldEmptyTest(self):
        search_field_empty_obj = WelcomePage(self.driver)
        search_field_empty_obj.search_empty()        

    def tearDown(self):
        super(SearchFieldEmptyTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



