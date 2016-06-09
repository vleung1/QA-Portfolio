from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import ManagementChallengesPageMap


#this is a page object for the Management Challenges Letter page containing links to the documents for download
#accessed after clicking the Management Challenges Letter link 
class ManagementChallengesPage(BasePage):

    def __init__(self, driver):
        super(ManagementChallengesPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         ManagementChallengesPageMap['ManagementChallengesBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      