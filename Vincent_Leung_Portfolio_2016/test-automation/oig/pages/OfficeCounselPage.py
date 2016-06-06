from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OfficeCounselPageMap


#this is a page object for the Office of Counsel info page
#accessed after clicking the Office of Counsel link 
class OfficeCounselPage(BasePage):

    def __init__(self, driver):
        super(OfficeCounselPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         OfficeCounselPageMap['OfficeCounselBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      