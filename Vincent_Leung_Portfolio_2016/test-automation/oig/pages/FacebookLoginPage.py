from BasePage                import BasePage
from ShareOnFacebookPage     import ShareOnFacebookPage
from BasePage                import IncorrectPageException
from oig.UIMap               import FacebookLoginPageMap


#this is a page object for the Facebook login page containing methods for logging in 
#accessed from the homepage at the bottom, hovering over the Share button and selecting Facebook 
class FacebookLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(FacebookLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "name", 
                                           FacebookLoginPageMap['UsernameFieldName']
          )
        except:   
          raise IncorrectPageException
    
    def login(self):
        self.fill_out_field("name", 
                            FacebookLoginPageMap['UsernameFieldName'], 
                            self.username
        )
        self.fill_out_field("name", 
                            FacebookLoginPageMap['PasswordFieldName'], 
                            self.password
        )
        self.click(10, 
                   "name", 
                   FacebookLoginPageMap['LoginButtonName']
        )
        return ShareOnFacebookPage(self.driver)
        
        
    
      
    




