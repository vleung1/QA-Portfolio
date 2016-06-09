from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import ReportsPageMap
from oig.UIMap               import ReportsAuditPageMap
from oig.UIMap               import ReportsOtherPageMap
from oig.UIMap               import ReportsCongressPageMap
from oig.UIMap               import ReportsInvestigationsPageMap
from oig.UIMap               import ReportsPeerPageMap


#this is a page object for the Reports page containing all the report subsections
#accessed after clicking the Reports link 
class ReportsPage(BasePage):

    def __init__(self, driver):
        super(ReportsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         ReportsPageMap['ReportsPageBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    def verify_reports_audit(self):
      self.click(10,
                 "id",
                 ReportsPageMap['ReportsAuditLinkId']
      )
      self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       ReportsAuditPageMap['ReportsAuditBannerXpath']
      )
      self.driver.execute_script("window.history.go(-1)")

    def verify_reports_other(self):
      self.click(10,
                 "id",
                 ReportsPageMap['ReportsOtherLinkId']
      )
      self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       ReportsOtherPageMap['ReportsOtherBannerXpath']
      )
      self.driver.execute_script("window.history.go(-1)")

    def verify_reports_congress(self):
      self.click(10,
                 "id",
                 ReportsPageMap['ReportsCongressLinkId']
      )
      self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       ReportsCongressPageMap['ReportsCongressBannerXpath']
      )
      self.driver.execute_script("window.history.go(-1)")

    def verify_reports_investigations(self):
      self.click(10,
                 "id",
                 ReportsPageMap['ReportsInvestigationsLinkId']
      )
      self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       ReportsInvestigationsPageMap['ReportsInvestigationsBannerXpath']
      )
      self.driver.execute_script("window.history.go(-1)")

    def verify_reports_peer(self):
      self.click(10,
                 "id",
                 ReportsPageMap['ReportsPeerLinkId']
      )
      self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       ReportsPeerPageMap['ReportsPeerBannerXpath']
      )
      self.driver.execute_script("window.history.go(-1)")

    
      