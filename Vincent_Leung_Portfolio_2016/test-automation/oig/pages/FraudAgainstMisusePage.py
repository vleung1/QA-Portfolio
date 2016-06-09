from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudAgainstMisusePageMap


#this is a page object for the Fraud Alerts - Prohibition Against Misuse of Treasury Names, Terms, Symbols, Stationary, Etc. info page
#accessed after clicking the Prohibition Against Misuse of Treasury Names, Terms, Symbols, Stationary, Etc. link 
class FraudAgainstMisusePage(BasePage):

    def __init__(self, driver):
        super(FraudAgainstMisusePage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudAgainstMisusePageMap['FraudAgainstMisuseBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      