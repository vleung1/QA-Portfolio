from BasePage                        import BasePage
from BasePage                        import IncorrectPageException
from oig.Constants                   import TT_Constants
from oig.UIMap                       import NewHireOrientationPageMap
from OrientationBeforeReportPage     import OrientationBeforeReportPage
from OrientationFirstDayPage         import OrientationFirstDayPage
from OrientationNoFearPage           import OrientationNoFearPage
from OrientationPayLeavePage         import OrientationPayLeavePage
from OrientationBenefitsPage         import OrientationBenefitsPage
from OrientationWorkersCompPage      import OrientationWorkersCompPage
from OrientationEthicsPage           import OrientationEthicsPage
from OrientationWhistleblowerPage    import OrientationWhistleblowerPage
from OrientationHrConnectPage        import OrientationHrConnectPage
from OrientationForgottenPage        import OrientationForgottenPage
from OrientationConstitutionPage     import OrientationConstitutionPage
from OrientationAbbreviationsPage    import OrientationAbbreviationsPage


#this is a page object for the New Hire Orientation documents
#accessed after clicking the New Hire Orientation link 
class NewHireOrientationPage(BasePage):

    def __init__(self, driver):
        super(NewHireOrientationPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         NewHireOrientationPageMap['OrientationWelcomeBannerXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationWelcomeLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationBeforeReportLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationFirstDayLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationNoFearLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationPayLeaveLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationBenefitsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationWorkersCompLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationEthicsLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationWhistleblowerLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationHrConnectLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationForgottenLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationConstitutionLinkXpath']
          )
          self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       NewHireOrientationPageMap['OrientationAbbreviationsLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    def verify_before_report(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationBeforeReportLinkXpath']
      )
      return OrientationBeforeReportPage(self.driver)

    def verify_first_day(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationFirstDayLinkXpath']
      )
      return OrientationFirstDayPage(self.driver)
    
    def verify_no_fear(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationNoFearLinkXpath']
      )
      return OrientationNoFearPage(self.driver)
    
    def verify_pay_leave(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationPayLeaveLinkXpath']
      )
      return OrientationPayLeavePage(self.driver)
    
    def verify_benefits(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationBenefitsLinkXpath']
      )
      return OrientationBenefitsPage(self.driver)
    
    def verify_workers_comp(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationWorkersCompLinkXpath']
      )
      return OrientationWorkersCompPage(self.driver)
    
    def verify_ethics(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationEthicsLinkXpath']
      )
      return OrientationEthicsPage(self.driver)

    def verify_whistleblower_protection(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationWhistleblowerLinkXpath']
      )
      return OrientationWhistleblowerPage(self.driver)

    def verify_hr_connect(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationHrConnectLinkXpath']
      )
      return OrientationHrConnectPage(self.driver)

    def verify_forgotten(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationForgottenLinkXpath']
      )
      return OrientationForgottenPage(self.driver)

    def verify_constitution_initiative(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationConstitutionLinkXpath']
      )
      return OrientationConstitutionPage(self.driver)

    def verify_abbreviations(self):
      self.click(10,
                 "xpath",
                 NewHireOrientationPageMap['OrientationAbbreviationsLinkXpath']
      )
      return OrientationAbbreviationsPage(self.driver)

    def click_and_download(self):
      self.click(10,
                 "id",
                 NewHireOrientationPageMap['OrientationEeoPdfId']
      )
      self.click(10,
                 "id",
                 NewHireOrientationPageMap['OrientationDiversityPdfId']
      )
    
      