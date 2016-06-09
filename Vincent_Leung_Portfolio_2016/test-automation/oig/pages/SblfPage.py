from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import SblfPageMap


#this is a page object for the SBLF info page
#accessed after clicking the Small Business Lending Fund Program and State Small Business Credit Initiative link 
class SblfPage(BasePage):

    def __init__(self, driver):
        super(SblfPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         SblfPageMap['SblfBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         SblfPageMap['SblfReportsLinksXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      