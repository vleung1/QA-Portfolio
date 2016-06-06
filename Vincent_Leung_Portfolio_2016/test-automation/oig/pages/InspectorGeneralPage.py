from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import InspectorGeneralPageMap


#this is a page object for the Inspector General bio page
#accessed after clicking the Inspector General bio link 
class InspectorGeneralPage(BasePage):

    def __init__(self, driver):
        super(InspectorGeneralPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         InspectorGeneralPageMap['InspectorGeneralBioXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      