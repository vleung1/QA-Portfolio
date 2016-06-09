from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudOtherFraudPageMap


#this is a page object for the Fraud Alerts - Other Fraud Sites of Interest info page
#accessed after clicking the Other Fraud Sites of Interest link 
class FraudOtherFraudPage(BasePage):

    def __init__(self, driver):
        super(FraudOtherFraudPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudOtherFraudPageMap['FraudOtherFraudBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      