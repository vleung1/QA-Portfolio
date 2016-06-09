from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudProtectYourselfPageMap


#this is a page object for the Fraud Alerts - How to Protect Yourself from Investment Scams info page
#accessed after clicking the How to Protect Yourself from Investment Scams link 
class FraudProtectYourselfPage(BasePage):

    def __init__(self, driver):
        super(FraudProtectYourselfPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudProtectYourselfPageMap['FraudProtectYourselfBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      