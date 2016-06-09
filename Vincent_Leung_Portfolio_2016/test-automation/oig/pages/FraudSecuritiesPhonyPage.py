from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudSecuritiesPhonyPageMap


#this is a page object for the Fraud Alerts - Examples of Known Phony Securities info page
#accessed after clicking the Examples of Known Phony Securities link 
class FraudSecuritiesPhonyPage(BasePage):

    def __init__(self, driver):
        super(FraudSecuritiesPhonyPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudSecuritiesPhonyPageMap['FraudSecuritiesPhonyBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      