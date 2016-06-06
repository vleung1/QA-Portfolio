from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#test the search field functionality on the OIG homepage
class SearchFieldTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SearchFieldTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_SearchFieldTest(self):
        search_field_obj = WelcomePage(self.driver)
        search_field_obj.search("office of inspector general")        

    def tearDown(self):
        super(SearchFieldTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



