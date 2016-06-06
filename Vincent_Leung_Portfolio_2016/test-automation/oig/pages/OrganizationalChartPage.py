from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OrganizationalChartPageMap


#this is a page object for the organizational chart page
#accessed after clicking the organizational chart link 
class OrganizationalChartPage(BasePage):

    def __init__(self, driver):
        super(OrganizationalChartPage, self).__init__(driver)
  
    def _verify_page(self):

          return self
          
    
    
    
    
      