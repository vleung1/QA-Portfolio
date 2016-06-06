from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the informational page for the Office of Audit shows
class OfficeAuditTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(OfficeAuditTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="medium")
    def test_OfficeAuditTest(self):
        office_audit_obj = WelcomePage(self.driver)
        office_audit_obj.click_office_audit_link()        

    def tearDown(self):
        super(OfficeAuditTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



