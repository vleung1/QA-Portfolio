from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import SearchResultsPageMap


#this is a page object for the search results page containing a check for search results
#accessed after submitting a search from the search field bar 
class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super(SearchResultsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "id", 
                                         SearchResultsPageMap['SearchResultsId']
          )
        except:   
          raise IncorrectPageException
    
    
    
      
    

