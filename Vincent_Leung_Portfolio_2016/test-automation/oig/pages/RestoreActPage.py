from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import RestoreActPageMap


#this is a page object for the Restore Act info page
#accessed after clicking the Restore Act link 
class RestoreActPage(BasePage):

    def __init__(self, driver):
        super(RestoreActPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         RestoreActPageMap['RestoreActBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         RestoreActPageMap['GulfCoastEmailXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      