from BasePage                import BasePage
from ShareOnTwitterPage      import ShareOnTwitterPage
from BasePage                import IncorrectPageException
from oig.UIMap               import TwitterLoginPageMap


#this is a page object for the Twitter login page containing methods for logging in 
#accessed from the homepage at the bottom, hovering over the Share button and selecting Twitter 
class TwitterLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(TwitterLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "id", 
                                           TwitterLoginPageMap['UsernameFieldId']
          )
        except:   
          raise IncorrectPageException
    
    def login(self):
        self.fill_out_field("id", 
                            TwitterLoginPageMap['UsernameFieldId'], 
                            self.username
        )
        self.fill_out_field("id", 
                            TwitterLoginPageMap['PasswordFieldId'], 
                            self.password
        )
        self.click(10, 
                   "xpath", 
                   TwitterLoginPageMap['LoginButtonXpath']
        )
        return ShareOnTwitterPage(self.driver)
        
        
    
      
    




