from oig.Constants                      import TT_Constants
from oig.pages.WelcomePage              import WelcomePage
from oig.pages.PrivacyAssessmentPage    import PrivacyAssessmentPage
from oig.BaseTestCase                   import BaseTestCase
import unittest
import nose
from nose.plugins.attrib                import attr


#verify Whistleblower page loads and able to download all the files on the page
class PrivacyAssessmentTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(PrivacyAssessmentTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(TT_Constants['Base_URL'])

    @attr(priority="low") 
    def test_PrivacyAssessmentTest(self):
        privacy_assessment_obj = WelcomePage(self.driver)
        privacy_assessment_obj.click_privacy_assessment_link()
        privacy_assessment_obj = PrivacyAssessmentPage(self.driver)
        privacy_assessment_obj.click_and_download()

    def tearDown(self):
        super(PrivacyAssessmentTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



