from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import PlanningDocumentsPageMap
from oig.UIMap               import EmailUpdatesPageMap


#this is a page object for the Planning Documents informational page
#accessed after clicking the Planning Documents link 
class PlanningDocumentsPage(BasePage):

    def __init__(self, driver):
        super(PlanningDocumentsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         PlanningDocumentsPageMap['PlanningDocumentsBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    def verify_update_content(self):
      self.click(10,
                 "id",
                 PlanningDocumentsPageMap['ContentUpdateLinkId']
      )
      self.wait_for_element_visibility(10, 
                                       "id", 
                                       EmailUpdatesPageMap['EmailAddressFieldId']
      )

    

    
      