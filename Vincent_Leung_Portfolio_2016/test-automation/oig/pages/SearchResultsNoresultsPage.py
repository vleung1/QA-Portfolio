from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import SearchResultsNoresultsPageMap


#this is a page object for the search results page containing a check for search results
#accessed after submitting an invalid search from the search field bar 
class SearchResultsNoresultsPage(BasePage):

    def __init__(self, driver):
        super(SearchResultsNoresultsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         SearchResultsNoresultsPageMap['SearchResultsXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    
      
    

