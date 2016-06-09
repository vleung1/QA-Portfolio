from oig.Constants                  import TT_Constants
from oig.pages.WelcomePage          import WelcomePage
from oig.pages.EqualOpportunityPage import EqualOpportunityPage
from oig.BaseTestCase               import BaseTestCase
import unittest
import nose
from nose.plugins.attrib            import attr


#verify EEO page loads and able to download all the files on the page
class EqualOpportunityTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(EqualOpportunityTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(TT_Constants['Base_URL'])

    @attr(priority="low") 
    def test_EqualOpportunityTest(self):
        eeo_obj = WelcomePage(self.driver)
        eeo_obj.click_eeo_link()
        eeo_obj = EqualOpportunityPage(self.driver)
        eeo_obj.click_and_download()

    def tearDown(self):
        super(EqualOpportunityTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



