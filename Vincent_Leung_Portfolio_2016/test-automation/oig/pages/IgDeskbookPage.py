from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import IgDeskbookPageMap
import time


#this is a page object for the Inspector General Deskbook page 
#accessed by clicking on the Office of Counsel link on the homepage and then following the Deskbook link
class IgDeskbookPage(BasePage):

    def __init__(self, driver):
        super(IgDeskbookPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         IgDeskbookPageMap['IgDeskbookBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    #method to verify all the links are present, then clicking each to download
    def click_and_download(self):
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookIntroId']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol1Part1Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol1Part2Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol1Part3Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol1Part4Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol2Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol3Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol4Part1Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol4Part2Id']
      )
      self.wait_for_element_visibility(10,
                                      "id",
                                      IgDeskbookPageMap['IgDeskbookVol4Part3Id']
      )

      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookIntroId']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol1Part1Id']
      )       
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol1Part2Id']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol1Part3Id']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol1Part4Id']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol2Id']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol3Id']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol4Part1Id']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol4Part2Id']
      )
      self.click(10,
                 "id",
                 IgDeskbookPageMap['IgDeskbookVol4Part3Id']
      )
            


