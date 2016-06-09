from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudHistoricalBondPageMap


#this is a page object for the Fraud Alerts - Historical Bond Fraud info page
#accessed after clicking the Historical Bond Fraud link 
class FraudHistoricalBondPage(BasePage):

    def __init__(self, driver):
        super(FraudHistoricalBondPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudHistoricalBondPageMap['FraudHistoricalBondBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      