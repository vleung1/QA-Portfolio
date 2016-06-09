from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import VacanciesPageMap
import time


#this is a page object for the Vacancies page 
#accessed by clicking on the Vacancies link on the homepage
class VacanciesPage(BasePage):

    def __init__(self, driver):
        super(VacanciesPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         VacanciesPageMap['VacanciesBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    #method to verify all the links are present, then clicking each to download
    def click_and_download(self):
      self.wait_for_element_visibility(10,
                                      "id",
                                      VacanciesPageMap['ApplicantGuideId']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      VacanciesPageMap['VeteranGuideId']
      )

      self.click(10,
                 "id",
                 VacanciesPageMap['ApplicantGuideId']
      )
      self.click(10,
                 "id",
                 VacanciesPageMap['VeteranGuideId']
      )
      time.sleep(5)
            

