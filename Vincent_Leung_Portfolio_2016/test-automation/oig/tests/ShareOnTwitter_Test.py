from oig.TestCaseTwitter            import TestCaseTwitter
from oig.Constants                  import TT_Constants
from oig.pages.ShareOnTwitterPage   import ShareOnTwitterPage
import unittest
import nose
from nose.plugins.attrib 			import attr


#verify ability to click the Share button on the homepage, then log into Twitter and share the page
class ShareOnTwitterTest(TestCaseTwitter, unittest.TestCase):

    def setUp(self):
        super(ShareOnTwitterTest, self).setUp()
      
    @attr(priority="medium") 
    def test_ShareOnTwitterTest(self):
        share_on_twitter_page_obj = ShareOnTwitterPage(self.driver)
        share_on_twitter_page_obj.share()
    
    def tearDown(self):
        super(ShareOnTwitterTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



