from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.pages.ReportsPage       import ReportsPage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the Reports page shows and verify each link on the page
class ReportsTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(ReportsTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="high")
    def test_ReportsTest(self):
        reports_obj = WelcomePage(self.driver)
        reports_obj.click_reports_link()
        reports_obj = ReportsPage(self.driver)        
        reports_obj.verify_reports_audit()
        reports_obj.verify_reports_other()
        reports_obj.verify_reports_congress()
        reports_obj.verify_reports_investigations()
        reports_obj.verify_reports_peer()

    def tearDown(self):
        super(ReportsTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



