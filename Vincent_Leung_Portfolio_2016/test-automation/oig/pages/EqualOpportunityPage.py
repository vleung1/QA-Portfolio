from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import EqualOpportunityPageMap
import time


#this is a page object for the EEO page 
#accessed by clicking on the Equal Employement Opportunity link on the homepage
class EqualOpportunityPage(BasePage):

    def __init__(self, driver):
        super(EqualOpportunityPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         EqualOpportunityPageMap['EqualOpportunityBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    #method to verify all the links are present, then clicking each to download
    def click_and_download(self):
      self.wait_for_element_visibility(10,
                                      "id",
                                      EqualOpportunityPageMap['ReasonableAccomodationPdfId']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      EqualOpportunityPageMap['EeoPolicyDocId']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      EqualOpportunityPageMap['DisputeResolutionPdfId']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      EqualOpportunityPageMap['OfficialTimePdfId']
      )

      self.click(10,
                 "id",
                 EqualOpportunityPageMap['ReasonableAccomodationPdfId']
      )
      self.click(10,
                 "id",
                 EqualOpportunityPageMap['EeoPolicyDocId']
      )       
      self.click(10,
                 "id",
                 EqualOpportunityPageMap['DisputeResolutionPdfId']
      )
      self.click(10,
                 "id",
                 EqualOpportunityPageMap['OfficialTimePdfId']
      )
      time.sleep(1)

            


