from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.UIMap               import ShareOnFacebookPageMap


#this is a page object for the Facebook post-login page containing the submit button
#accessed after logging into Facebook 
class ShareOnFacebookPage(BasePage):

    def __init__(self, driver):
        super(ShareOnFacebookPage, self).__init__(driver)

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "name", 
                                           ShareOnFacebookPageMap['ShareLinkButtonName']
          )
        except:   
          raise IncorrectPageException
    
    def share(self):
        self.click(10, 
                   "name", 
                   ShareOnFacebookPageMap['ShareLinkButtonName']
        )
        
    
      
    



