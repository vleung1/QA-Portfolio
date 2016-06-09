from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import RecoveryActPageMap
from oig.UIMap               import RecoveryActDocumentsPageMap


#this is a page object for the Recovery Act informational page
#accessed after clicking the American Recovery & Reinvestment Act of 2009 link 
class RecoveryActPage(BasePage):

    def __init__(self, driver):
        super(RecoveryActPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         RecoveryActPageMap['RecoveryActBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    def verify_recovery_documents(self):
      self.click(10,
                 "id",
                 RecoveryActPageMap['RecoveryActDocumentsLinkId']
      )
      self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       RecoveryActDocumentsPageMap['RecoveryActDocumentsBannerXpath']
      )

    

    
      