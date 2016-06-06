from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OfficeAuditPageMap


#this is a page object for the Office of Audit info page
#accessed after clicking the Office of Audit link 
class OfficeAuditPage(BasePage):

    def __init__(self, driver):
        super(OfficeAuditPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         OfficeAuditPageMap['OfficeAuditBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      