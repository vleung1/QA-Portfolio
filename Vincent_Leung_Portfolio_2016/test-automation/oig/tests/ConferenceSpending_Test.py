from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the Conference Spending Reports shows, and check for presence of FY2015 report
class ConferenceSpendingTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(ConferenceSpendingTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="medium")
    def test_SblfTest(self):
        conference_spending_obj = WelcomePage(self.driver)
        conference_spending_obj.click_conference_spending_link()        

    def tearDown(self):
        super(ConferenceSpendingTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



