from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OigHotlinePageMap
from oig.UIMap               import OigHotlineConfirmationPageMap


#this is a page object for the OIG Hotline page 
#accessed by clicking on the OIG Hotline link on the homepage
class OigHotlinePage(BasePage):

    def __init__(self, driver):
        super(OigHotlinePage, self).__init__(driver)
  
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "id", 
                                         OigHotlinePageMap['AnonymousRadioButtonId']
          )
        except:   
          raise IncorrectPageException
    
    #method to fill out all the fields and click the submit button
    def submit_request(self):
      self.click(10,
                 "id",
                 OigHotlinePageMap['AnonymousRadioButtonId']

      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['AllegedMisconductFieldId'], 
                            "This is a test. There was an alleged wrongdoing."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['ContractorFraudFieldId'], 
                            "This is a test. A contractor may or may not have committed fraud."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['IndividualDetailsFieldId'], 
                            "This is a test. This individual was a person."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['InappropriateHappeningsFieldId'], 
                            "This is a test. The wrongdoing was inappropriate."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['MisconductWhenFieldId'], 
                            "This is a test. The misconduct happened in the past."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['MisconductWhereFieldId'], 
                            "This is a test. The misconduct happened on Earth."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['MisconductHowFieldId'], 
                            "This is a test. The misconduct was carried out to break the rules."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['CorrectiveActionsFieldId'], 
                            "This is a test. There were no corrective actions taken."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['AdditionalInformationFieldId'], 
                            "This is a test. No additional information is available."
      )
      self.click(10, 
                 "cssSelector", 
                 OigHotlinePageMap['SubmitButtonCss']
      )
      self.wait_for_element_visibility(10, 
                                       "id", 
                                       OigHotlineConfirmationPageMap['ConfirmationMessageId']
      )

    #verify that the user would be unable to submit the form if at least one of the fields are not filled out
    #by leaving first field empty
    #function would return itself as the page should not change
    def validation_check(self):
      self.click(10,
                 "id",
                 OigHotlinePageMap['AnonymousRadioButtonId'],

      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['ContractorFraudFieldId'], 
                            "This is a test. A contractor may or may not have committed fraud."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['IndividualDetailsFieldId'], 
                            "This is a test. This individual was a person."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['InappropriateHappeningsFieldId'], 
                            "This is a test. The wrongdoing was inappropriate."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['MisconductWhenFieldId'], 
                            "This is a test. The misconduct happened in the past."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['MisconductWhereFieldId'], 
                            "This is a test. The misconduct happened on Earth."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['MisconductHowFieldId'], 
                            "This is a test. The misconduct was carried out to break the rules."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['CorrectiveActionsFieldId'], 
                            "This is a test. There were no corrective actions taken."
      )
      self.fill_out_field("id", 
                            OigHotlinePageMap['AdditionalInformationFieldId'], 
                            "This is a test. No additional information is available."
      )
      self.click(10, 
                 "cssSelector", 
                 OigHotlinePageMap['SubmitButtonCss']
      )
      return self
    

