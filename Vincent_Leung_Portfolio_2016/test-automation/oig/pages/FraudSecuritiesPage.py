from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudSecuritiesPageMap


#this is a page object for the Fraud Alerts - How Marketable Treasury Securities Work info page
#accessed after clicking the How Marketable Treasury Securities Work link 
class FraudSecuritiesPage(BasePage):

    def __init__(self, driver):
        super(FraudSecuritiesPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudSecuritiesPageMap['FraudSecuritiesBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      