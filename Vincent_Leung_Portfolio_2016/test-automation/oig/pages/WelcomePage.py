from oig.Constants                    import TT_Constants
from oig.UIMap                        import WelcomePageMap
from BasePage                         import BasePage
from BasePage                         import IncorrectPageException
from InspectorGeneralPage             import InspectorGeneralPage
from OfficeAuditPage                  import OfficeAuditPage
from OfficeCounselPage                import OfficeCounselPage
from OfficeInvestigationsPage         import OfficeInvestigationsPage
from OfficeManagementPage             import OfficeManagementPage
from OrganizationalChartPage          import OrganizationalChartPage
from SearchResultsPage                import SearchResultsPage
from SearchResultsEmptyPage           import SearchResultsEmptyPage
from SearchResultsNoresultsPage       import SearchResultsNoresultsPage
from FacebookLoginPage                import FacebookLoginPage
from TwitterLoginPage                 import TwitterLoginPage


#this is a page object for the OIG homepage containing methods for use in test cases 
class WelcomePage(BasePage):

    def __init__(self, driver):
        super(WelcomePage, self).__init__(driver)

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         WelcomePageMap['WelcomeBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    #method for submitting a value into the search field
    def search(self, searchString):
        self.fill_out_field("xpath",
                            WelcomePageMap['SearchFieldXpath'],
                            searchString
        )
        self.click(10, 
                   "name", 
                   WelcomePageMap['SearchSubmitButtonName']
        )
        return SearchResultsPage(self.driver)

    #method for submitting an empty value into the search field
    def search_empty(self):
        self.click(10, 
                   "name", 
                   WelcomePageMap['SearchSubmitButtonName']
        )
        return SearchResultsEmptyPage(self.driver)

    #method for submitting a value into the search field that has zero results
    def search_invalid(self, searchString):
        self.fill_out_field("xpath",
                            WelcomePageMap['SearchFieldXpath'],
                            searchString
        )
        self.click(10, 
                   "name", 
                   WelcomePageMap['SearchSubmitButtonName']
        )
        return SearchResultsNoresultsPage(self.driver)
    
    #method for clicking the Share On Facebook button
    def click_share_on_facebook_button(self):
        mainWindowHandle = self.driver.window_handles
        self.hover_over(10,
                        "id",
                        WelcomePageMap['ShareButtonId']
        ) 
        self.click(10, 
                   "xpath", 
                   WelcomePageMap['FacebookShareButtonXpath']
        )
        allWindowHandles = self.driver.window_handles
        for handle in allWindowHandles:
         if handle != mainWindowHandle[0]:
          self.switch_to_window(handle)
          break
        return FacebookLoginPage(self.driver, 
                                 TT_Constants['Facebook_Username'],
                                 TT_Constants['Facebook_Password'] 
        )
    
    #method for clicking the Share on Twitter button    
    def click_share_on_twitter_button(self):
        mainWindowHandle = self.driver.window_handles
        self.hover_over(10,
                        "id",
                        WelcomePageMap['ShareButtonId']
        ) 
        self.click(10, 
                   "xpath", 
                   WelcomePageMap['TwitterShareButtonXpath']
        )
        allWindowHandles = self.driver.window_handles
        for handle in allWindowHandles:
         if handle != mainWindowHandle[0]:
          self.switch_to_window(handle)
          break
        return TwitterLoginPage(self.driver, 
                                 TT_Constants['Twitter_Username'],
                                 TT_Constants['Twitter_Password'] 
        )
      
    #method for verifying the organization chart link path and clicking to open it
    def click_organizational_chart_link(self):
        self.wait_until_element_clickable(10,
                                          "xpath",
                                          WelcomePageMap['OrganizationalChartPathXpath']
        )
        self.click(10,
                   "id",
                   WelcomePageMap['OrganizationalChartLinkId']
        )
        return OrganizationalChartPage(self.driver)

    #method for clicking the Inspector General bio link
    def click_inspector_general_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['InspectorGeneralLinkId']
        )
        return InspectorGeneralPage(self.driver) 

    #method for clicking the Office of Management link
    def click_office_management_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['OfficeManagementLinkId']
        )
        return OfficeManagementPage(self.driver)

    #method for clicking the Office of Investigations link
    def click_office_investigations_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['OfficeInvestigationsLinkId']
        )
        return OfficeInvestigationsPage(self.driver)

    #method for clicking the Office of Audit link
    def click_office_audit_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['OfficeAuditLinkId']
        )
        return OfficeAuditPage(self.driver)

    #method for clicking the Office of Counsel link
    def click_office_counsel_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['OfficeCounselLinkId']
        )
        return OfficeCounselPage(self.driver)