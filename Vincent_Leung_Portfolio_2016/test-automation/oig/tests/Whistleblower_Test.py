from oig.Constants                  import TT_Constants
from oig.pages.WelcomePage          import WelcomePage
from oig.pages.WhistleblowerPage    import WhistleblowerPage
from oig.BaseTestCase               import BaseTestCase
import unittest
import nose
from nose.plugins.attrib            import attr


#verify Whistleblower page loads and able to download all the files on the page
class WhistleblowerTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(WhistleblowerTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(TT_Constants['Base_URL'])

    @attr(priority="medium") 
    def test_WhistleblowerTest(self):
        whistleblower_obj = WelcomePage(self.driver)
        whistleblower_obj.click_whistleblower_link()
        whistleblower_obj = WhistleblowerPage(self.driver)
        whistleblower_obj.click_and_download()

    def tearDown(self):
        super(WhistleblowerTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



