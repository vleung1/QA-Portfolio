from oig.TestCaseFacebook           import TestCaseFacebook
from oig.Constants                  import TT_Constants
from oig.pages.ShareOnFacebookPage  import ShareOnFacebookPage
import unittest
import nose
from nose.plugins.attrib 			import attr


#verify ability to click the Share button on the homepage, then log into Facebook and share the page
class ShareOnFacebookTest(TestCaseFacebook, unittest.TestCase):

    def setUp(self):
        super(ShareOnFacebookTest, self).setUp()
      
    @attr(priority="medium") 
    def test_ShareOnFacebookTest(self):
        share_on_facebook_page_obj = ShareOnFacebookPage(self.driver)
        share_on_facebook_page_obj.share()
    
    def tearDown(self):
        super(ShareOnFacebookTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



