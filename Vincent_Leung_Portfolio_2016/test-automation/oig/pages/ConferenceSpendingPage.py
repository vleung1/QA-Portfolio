from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import ConferenceSpendingPageMap


#this is a page object for the Conference Spending Reports info page
#accessed after clicking the Reports on Conference Spending to Support Agency Operations in Accordance 
#with OMB M-12-12 link 
class ConferenceSpendingPage(BasePage):

    def __init__(self, driver):
        super(ConferenceSpendingPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         ConferenceSpendingPageMap['ConferenceSpendingBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         ConferenceSpendingPageMap['ConferenceSpending2015Xpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      