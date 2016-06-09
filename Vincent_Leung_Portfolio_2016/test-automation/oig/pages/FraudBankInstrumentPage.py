from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudBankInstrumentPageMap


#this is a page object for the Fraud Alerts - Prime Bank Instrument Fraud info page
#accessed after clicking the Prime Bank Instrument Fraud link 
class FraudBankInstrumentPage(BasePage):

    def __init__(self, driver):
        super(FraudBankInstrumentPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudBankInstrumentPageMap['FraudBankInstrumentBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      