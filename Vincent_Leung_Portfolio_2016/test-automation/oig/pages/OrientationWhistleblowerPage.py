from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OrientationWhistleblowerPageMap


#this is a page object for the New Hire Orientation - Whistleblower Protection info page
#accessed after clicking the Whistleblower Protection link 
class OrientationWhistleblowerPage(BasePage):

    def __init__(self, driver):
        super(OrientationWhistleblowerPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationWhistleblowerBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationWelcomeLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationBeforeReportLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationFirstDayLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationNoFearLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationPayLeaveLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationBenefitsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationWorkersCompLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationEthicsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationWhistleblowerLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationHrConnectLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationForgottenLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationConstitutionLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationWhistleblowerPageMap['OrientationAbbreviationsLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      