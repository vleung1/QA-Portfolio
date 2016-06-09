from BasePage                        import BasePage
from BasePage                        import IncorrectPageException
from oig.Constants                   import TT_Constants
from oig.UIMap                       import FraudAlertsPageMap
from FraudSecuritiesPage             import FraudSecuritiesPage
from FraudSecuritiesScamPage         import FraudSecuritiesScamPage
from FraudSecuritiesPhonyPage        import FraudSecuritiesPhonyPage
from FraudHistoricalBondPage         import FraudHistoricalBondPage
from FraudBankInstrumentPage         import FraudBankInstrumentPage
from FraudProtectYourselfPage        import FraudProtectYourselfPage
from FraudOtherFraudPage             import FraudOtherFraudPage
from FraudAgainstMisusePage          import FraudAgainstMisusePage
from FraudBogusSightPage             import FraudBogusSightPage


#this is a page object for the Fraud Alerts page that contains links and documents
#accessed after clicking the Fraud Alerts link 
class FraudAlertsPage(BasePage):

    def __init__(self, driver):
        super(FraudAlertsPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         FraudAlertsPageMap['FraudAlertsBannerXpath']
          )
        except:   
          raise IncorrectPageException
    
    def verify_securities(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudSecuritiesLinkId']
      )
      return FraudSecuritiesPage(self.driver)
    
    def verify_securities_scam(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudSecuritiesScamsLinkId']
      )
      return FraudSecuritiesScamPage(self.driver)
    
    def verify_securities_phony(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudSecuritiesPhonyLinkId']
      )
      return FraudSecuritiesPhonyPage(self.driver)
    
    def verify_historical_bond(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudHistoricalBondLinkId']
      )
      return FraudHistoricalBondPage(self.driver)
    
    def verify_bank_instrument(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudBankInstrumentLinkId']
      )
      return FraudBankInstrumentPage(self.driver)
    
    def verify_protect_yourself(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudProtectYourselfLinkId']
      )
      return FraudProtectYourselfPage(self.driver)

    def verify_other_fraud(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudOtherFraudLinkId']
      )
      return FraudOtherFraudPage(self.driver)

    def verify_against_misuse(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudAgainstMisuseLinkId']
      )
      return FraudAgainstMisusePage(self.driver)

    def verify_bogus_sight(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudBogusSightLinkId']
      )
      return FraudBogusSightPage(self.driver)

    def click_and_download(self):
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudTigScamsDocId']
      )
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudThreatsDemandsDocId']
      )
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudAmericanBankersPdfId']
      )
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudAutomobileDealersPdfId']
      )
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudRealtorsAssociationPdfId']
      )
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudPromissoryNotePdfId']
      )
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudPrivateBondPdfId']
      )
      self.click(10,
                 "id",
                 FraudAlertsPageMap['FraudBpdCheckPdfId']
      )

    
      