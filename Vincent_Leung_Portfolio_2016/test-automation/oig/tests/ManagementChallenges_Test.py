from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the Management Challenges Letter informational page shows
class ManagementChallengesTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(ManagementChallengesTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_ManagementChallengesTest(self):
        management_challenges_obj = WelcomePage(self.driver)
        management_challenges_obj.click_management_challenges_link()        

    def tearDown(self):
        super(ManagementChallengesTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



