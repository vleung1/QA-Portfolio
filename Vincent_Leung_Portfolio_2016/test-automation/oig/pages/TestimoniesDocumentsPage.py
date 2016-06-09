from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import TestimoniesDocumentsPageMap


#this is a page object for the Testimonies & Other Documents info page
#accessed after clicking the Testimonies & Other Documents link 
class TestimoniesDocumentsPage(BasePage):

    def __init__(self, driver):
        super(TestimoniesDocumentsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         TestimoniesDocumentsPageMap['TestimoniesDocumentsBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      