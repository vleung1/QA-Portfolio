from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudSecuritiesScamPageMap


#this is a page object for the Fraud Alerts - Scams Involving Treasury Securities info page
#accessed after clicking the Scams Involving Treasury Securities link 
class FraudSecuritiesScamPage(BasePage):

    def __init__(self, driver):
        super(FraudSecuritiesScamPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudSecuritiesScamPageMap['FraudSecuritiesScamsBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      