from oig.Constants               import TT_Constants
from oig.pages.WelcomePage       import WelcomePage
from oig.BaseTestCase            import BaseTestCase
import unittest
import nose
from nose.plugins.attrib         import attr


#verify the organizational chart shows
class OrganizationalChartTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(OrganizationalChartTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        
    @attr(priority="low")
    def test_OrganizationalChartTest(self):
        organizational_chart_obj = WelcomePage(self.driver)
        organizational_chart_obj.click_organizational_chart_link()        

    def tearDown(self):
        super(OrganizationalChartTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



