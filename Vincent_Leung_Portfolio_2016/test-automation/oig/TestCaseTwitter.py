from oig.BaseTestCase            import BaseTestCase
from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.pages.TwitterLoginPage  import TwitterLoginPage


#wrap selenium calls to log in to Twitter
class TestCaseTwitter(BaseTestCase):

  def setUp(self):
      super(TestCaseTwitter, self).setUp()
      productPageURL = TT_Constants['Base_URL']
      self.navigate_to_page(productPageURL)
      welcome_page_obj = WelcomePage(self.driver)
      welcome_page_obj.click_share_on_twitter_button()
      action = TwitterLoginPage(self.driver, 
                                 TT_Constants['Twitter_Username'],
                                 TT_Constants['Twitter_Password']
      )
      action.login()
      

  def tearDown(self):
  	  super(TestCaseTwitter, self).tearDown()
