from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.UIMap               import ShareOnTwitterPageMap


#this is a page object for the Twitter post-login page containing the submit button 
#accessed after logging into Twitter 
class ShareOnTwitterPage(BasePage):

    def __init__(self, driver):
        super(ShareOnTwitterPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "xpath", 
                                           ShareOnTwitterPageMap['ShareLinkButtonXpath']
          )
        except:   
          raise IncorrectPageException
    
    def share(self):
        self.click(10, 
                   "xpath", 
                   ShareOnTwitterPageMap['ShareLinkButtonXpath']
        )
        
    
      
    



