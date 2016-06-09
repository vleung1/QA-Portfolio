from oig.Constants                    import TT_Constants
from oig.UIMap                        import WelcomePageMap
from BasePage                         import BasePage
from BasePage                         import IncorrectPageException
from SearchResultsPage                import SearchResultsPage
from SearchResultsEmptyPage           import SearchResultsEmptyPage
from SearchResultsNoresultsPage       import SearchResultsNoresultsPage
from FacebookLoginPage                import FacebookLoginPage
from TwitterLoginPage                 import TwitterLoginPage
from InspectorGeneralPage             import InspectorGeneralPage
from OfficeAuditPage                  import OfficeAuditPage
from OfficeCounselPage                import OfficeCounselPage
from OfficeInvestigationsPage         import OfficeInvestigationsPage
from OfficeManagementPage             import OfficeManagementPage
from OrganizationalChartPage          import OrganizationalChartPage
from ReportsPage                      import ReportsPage
from RecoveryActPage                  import RecoveryActPage
from EqualOpportunityPage             import EqualOpportunityPage
from IgActPage                        import IgActPage
from ManagementChallengesPage         import ManagementChallengesPage
from SblfPage                         import SblfPage
from ConferenceSpendingPage           import ConferenceSpendingPage
from RestoreActPage                   import RestoreActPage
from TestimoniesDocumentsPage         import TestimoniesDocumentsPage
from VacanciesPage                    import VacanciesPage
from WhistleblowerPage                import WhistleblowerPage
from PrivacyAssessmentPage            import PrivacyAssessmentPage
from PlanningDocumentsPage            import PlanningDocumentsPage
from NewHireOrientationPage           import NewHireOrientationPage
from FraudAlertsPage                  import FraudAlertsPage


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
        mainWindowHandle = self.driver.window_handles
        self.click(10,
                   "id",
                   WelcomePageMap['OrganizationalChartLinkId']
        )
        allWindowHandles = self.driver.window_handles
        for handle in allWindowHandles:
         if handle != mainWindowHandle[0]:
          self.switch_to_window(handle)
          break
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

    #method for clicking the Reports link and verifying each report subsection link
    def click_reports_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['ReportsLinkId']
        )
        return ReportsPage(self.driver)

    #method for clicking the Recovery Act link
    def click_recovery_act_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['RecoveryActLinkId']
        )
        return RecoveryActPage(self.driver)

    #method for clicking the EEO link
    def click_eeo_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['EqualOpportunityLinkId']
        )
        return EqualOpportunityPage(self.driver)

    #method for clicking the Inspector General Act link
    def click_ig_act_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['IgActLinkId']
        )
        return IgActPage(self.driver)

    #method for clicking the Management Challenges Letter link
    def click_management_challenges_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['ManagementChallengesLinkId']
        )
        return ManagementChallengesPage(self.driver)

    #method for clicking the SBLF and SSBCI link
    def click_sblf_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['SblfLinkId']
        )
        return SblfPage(self.driver)

    #method for clicking the Conference Spending Reports link
    def click_conference_spending_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['ConferenceSpendingLinkId']
        )
        return ConferenceSpendingPage(self.driver)

    #method for clicking the Restore Act link
    def click_restore_act_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['RestoreActLinkId']
        )
        return RestoreActPage(self.driver)

    #method for clicking the Testimonies & Other Documents link
    def click_testimonies_documents_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['TestimoniesDocumentsLinkId']
        )
        return TestimoniesDocumentsPage(self.driver)

    #method for clicking the Vacancies link
    def click_vacancies_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['VacanciesLinkId']
        )
        return VacanciesPage(self.driver)

    #method for clicking the Whistleblower link
    def click_whistleblower_link(self):
        mainWindowHandle = self.driver.window_handles
        self.click(10,
                   "id",
                   WelcomePageMap['WhistleblowerLinkId']
        )
        allWindowHandles = self.driver.window_handles
        for handle in allWindowHandles:
         if handle != mainWindowHandle[0]:
          self.switch_to_window(handle)
          break
        return WhistleblowerPage(self.driver)

    #method for clicking the Privacy Impact Assessment link
    def click_privacy_assessment_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['PrivacyAssessmentLinkId']
        )
        return PrivacyAssessmentPage(self.driver)

    #method for clicking the Planning Documents link
    def click_planning_documents_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['PlanningDocumentsLinkId']
        )
        return PlanningDocumentsPage(self.driver)

    #method for clicking the New Hire Orientation link
    def click_new_hire_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['NewHireOrientationLinkId']
        )
        return NewHireOrientationPage(self.driver)

    #method for clicking the Fraud Alerts link
    def click_fraud_alerts_link(self):
        self.click(10,
                   "id",
                   WelcomePageMap['FraudAlertsLinkId']
        )
        return FraudAlertsPage(self.driver)