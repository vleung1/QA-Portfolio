from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OfficeInvestigationsPageMap


#this is a page object for the Office of Investigations info page
#accessed after clicking the Office of Investigations link 
class OfficeInvestigationsPage(BasePage):

    def __init__(self, driver):
        super(OfficeInvestigationsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         OfficeInvestigationsPageMap['OfficeInvestigationsBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      