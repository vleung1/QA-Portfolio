from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import FraudBogusSightPageMap


#this is a page object for the Fraud Alerts - Bogus Sight Drafts/Bills of Exchange Drawn on the Treasury info page
#accessed after clicking the Bogus Sight Drafts/Bills of Exchange Drawn on the Treasury link 
class FraudBogusSightPage(BasePage):

    def __init__(self, driver):
        super(FraudBogusSightPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudBogusSightPageMap['FraudBogusSightBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      