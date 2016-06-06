from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OfficeManagementPageMap


#this is a page object for the Office of Management info page
#accessed after clicking the Office of Management link 
class OfficeManagementPage(BasePage):

    def __init__(self, driver):
        super(OfficeManagementPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         OfficeManagementPageMap['OfficeManagementBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      