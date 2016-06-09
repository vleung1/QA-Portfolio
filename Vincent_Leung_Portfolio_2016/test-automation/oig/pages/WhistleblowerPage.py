from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import WhistleblowerPageMap


#this is a page object for the Whistleblower page 
#accessed by clicking on the Whistleblower link on the homepage
class WhistleblowerPage(BasePage):

    def __init__(self, driver):
        super(WhistleblowerPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         WhistleblowerPageMap['WhistleblowerPathXpath']
          )
        except:   
          raise IncorrectPageException
    
    #method to verify all the links are present, then clicking each to download
    def click_and_download(self):
      self.wait_for_element_visibility(10,
                                      "xpath",
                                      WhistleblowerPageMap['WhistleblowerPdfXpath']
      )
      
      self.click(10,
                 "xpath",
                 WhistleblowerPageMap['WhistleblowerPdfXpath']
      )


