from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OrientationFirstDayPageMap


#this is a page object for the New Hire Orientation - On Your First Day info page
#accessed after clicking the On Your First Day link 
class OrientationFirstDayPage(BasePage):

    def __init__(self, driver):
        super(OrientationFirstDayPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationFirstDayBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationWelcomeLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationBeforeReportLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationFirstDayLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationNoFearLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationPayLeaveLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationBenefitsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationWorkersCompLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationEthicsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationWhistleblowerLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationHrConnectLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationForgottenLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationConstitutionLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       OrientationFirstDayPageMap['OrientationAbbreviationsLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      