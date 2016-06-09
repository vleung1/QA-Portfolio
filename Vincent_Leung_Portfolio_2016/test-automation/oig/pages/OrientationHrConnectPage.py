from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OrientationHrConnectPageMap


#this is a page object for the New Hire Orientation - HR Connect info page
#accessed after clicking the HR Connect link 
class OrientationHrConnectPage(BasePage):

    def __init__(self, driver):
        super(OrientationHrConnectPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationHrConnectBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationWelcomeLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationBeforeReportLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationFirstDayLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationNoFearLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationPayLeaveLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationBenefitsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationWorkersCompLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationEthicsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationWhistleblowerLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationHrConnectLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationForgottenLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationConstitutionLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationHrConnectPageMap['OrientationAbbreviationsLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      