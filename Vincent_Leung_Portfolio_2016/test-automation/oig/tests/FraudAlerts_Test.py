from oig.Constants                             import TT_Constants
from oig.pages.WelcomePage                     import WelcomePage
from oig.pages.FraudAlertsPage                 import FraudAlertsPage
from oig.BaseTestCase                          import BaseTestCase
import unittest
import nose
from nose.plugins.attrib                       import attr


#verify Fraud Alerts page loads, the subpages load, and documents/PDFs are downloadable
class FraudAlertsPageTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(FraudAlertsPageTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(TT_Constants['Base_URL'])

    @attr(priority="high") 
    def test_FraudAlertsPageTest(self):
        fraud_alerts_obj = WelcomePage(self.driver)
        fraud_alerts_obj.click_fraud_alerts_link()
        fraud_alerts_obj = FraudAlertsPage(self.driver)
        fraud_alerts_obj.click_and_download()
        fraud_alerts_obj.verify_securities()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_securities_scam()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_securities_phony()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_historical_bond()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_bank_instrument()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_protect_yourself()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_other_fraud()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_against_misuse()
        self.driver.execute_script("window.history.go(-1)")
        fraud_alerts_obj.verify_bogus_sight()
        self.driver.execute_script("window.history.go(-1)")
        
    def tearDown(self):
        super(FraudAlertsPageTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()
