from oig.BaseTestCase            import BaseTestCase
from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.pages.FacebookLoginPage import FacebookLoginPage


#wrap selenium calls to log in to Facebook
class TestCaseFacebook(BaseTestCase):

  def setUp(self):
      super(TestCaseFacebook, self).setUp()
      productPageURL = TT_Constants['Base_URL']
      self.navigate_to_page(productPageURL)
      welcome_page_obj = WelcomePage(self.driver)
      welcome_page_obj.click_share_on_facebook_button()
      action = FacebookLoginPage(self.driver, 
                                 TT_Constants['Facebook_Username'],
                                 TT_Constants['Facebook_Password']
      )
      action.login()
      

  def tearDown(self):
  	  super(TestCaseFacebook, self).tearDown()
