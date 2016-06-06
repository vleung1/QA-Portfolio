from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import SearchResultsEmptyPageMap


#this is a page object for the search results page containing a check for search results
#accessed after submitting a blank search from the search field bar 
class SearchResultsEmptyPage(BasePage):

    def __init__(self, driver):
        super(SearchResultsEmptyPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         SearchResultsEmptyPageMap['SearchResultsXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      
    

