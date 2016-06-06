from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#test the search field functionality on the OIG homepage by submitting an invalid search and ensuring correct error message appears
class SearchFieldNoresultsTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SearchFieldNoresultsTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_SearchFieldNoresultsTest(self):
        search_field_noresults_obj = WelcomePage(self.driver)
        search_field_noresults_obj.search_invalid("THISSEARCHPARAMETERSHOULDYIELDNORESULTS")        

    def tearDown(self):
        super(SearchFieldNoresultsTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



