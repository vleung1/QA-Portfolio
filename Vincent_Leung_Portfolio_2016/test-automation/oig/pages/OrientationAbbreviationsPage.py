from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OrientationAbbreviationsPageMap


#this is a page object for the New Hire Orientation - Key Abbreviations info page
#accessed after clicking the Key Abbreviations link 
class OrientationAbbreviationsPage(BasePage):

    def __init__(self, driver):
        super(OrientationAbbreviationsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationAbbreviationsBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationWelcomeLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationBeforeReportLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationFirstDayLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationNoFearLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationPayLeaveLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationBenefitsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationWorkersCompLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationEthicsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationWhistleblowerLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationHrConnectLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationForgottenLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationConstitutionLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationAbbreviationsPageMap['OrientationAbbreviationsLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      