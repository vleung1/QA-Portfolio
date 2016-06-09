from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import IgActPageMap


#this is a page object for the IG Act info page
#accessed after clicking the Inspector General Act link 
class IgActPage(BasePage):

    def __init__(self, driver):
        super(IgActPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         IgActPageMap['IgActBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      