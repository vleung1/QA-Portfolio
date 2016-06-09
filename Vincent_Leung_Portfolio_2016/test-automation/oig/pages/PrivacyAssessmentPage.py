from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import PrivacyAssessmentPageMap


#this is a page object for the Privacy Impact Assessment page 
#accessed by clicking on the Privacy Impact Assessment link on the homepage
class PrivacyAssessmentPage(BasePage):

    def __init__(self, driver):
        super(PrivacyAssessmentPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         PrivacyAssessmentPageMap['PrivacyAssessmentBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    #method to verify all the links are present, then clicking each to download
    def click_and_download(self):
      self.wait_for_element_visibility(10,
                                      "id",
                                      PrivacyAssessmentPageMap['PrivacyAssessmentPdfId']
      )
      
      self.click(10,
                 "id",
                 PrivacyAssessmentPageMap['PrivacyAssessmentPdfId']
      )


