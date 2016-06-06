#UI mapping of WebElements in each page object
ContactPageMap = dict(FirstNameFieldXpath  = "//input[contains(@name, 'first')]",
                      LastNameFieldXpath   = "//input[contains(@name, 'last')]",
                      EmailFieldXpath      = "(//input[contains(@id, 'input')])[3]",
                      CommentFieldXpath    = "//textarea",
                      SubmitButtonXpath    = "//span[.='Submit']",
                      ThankYouMessageXpath = "//div[contains(text(), 'Thank you')]"
)

FacebookLoginPageMap = dict(UsernameFieldName = "email",
                            PasswordFieldName = "pass",
                            LoginButtonName   = "login"
)

TwitterLoginPageMap = dict(UsernameFieldId  = "username_or_email",
                           PasswordFieldId  = "password",
                           LoginButtonXpath = "//input[@value='Log in and Tweet']"
)

ShareOnFacebookPageMap = dict(ShareLinkButtonName = "__CONFIRM__"
)

ShareOnTwitterPageMap = dict(ShareLinkButtonXpath = "//input[@value='Tweet']"
)

WelcomePageMap = dict(WelcomeBannerXpath           = "//img[@alt='Office of the Inspector General']",
	                    SearchFieldXpath             = "//input[@class='usagov-search-autocomplete']",
	                    SearchSubmitButtonName       = "mynewbutton2",
                      ShareButtonId                = "anch_205",
                      FacebookShareButtonXpath     = "//span[contains(text(), 'Facebook')]",
                      TwitterShareButtonXpath      = "//span[contains(text(), 'Twitter')]",
                      OrganizationalChartLinkId    = "anch_178",
                      OrganizationalChartPathXpath = "//a[contains(@href, '/ig/Agency%20Documents/Organizational%20Chart.jpg')]", 
                      InspectorGeneralLinkId       = "anch_172",
                      OfficeManagementLinkId       = "anch_176",
                      OfficeInvestigationsLinkId   = "anch_175",
                      OfficeAuditLinkId            = "anch_173",
                      OfficeCounselLinkId          = "anch_174"
)

SearchResultsPageMap = dict(SearchResultsId = "summary"
)

SearchResultsEmptyPageMap = dict(SearchResultsXpath = "//p[contains(text(), 'Please enter a search term in the box above')]"
)

SearchResultsNoresultsPageMap = dict(SearchResultsXpath = "//p[contains(text(), 'Try entering fewer or broader query terms')]"
)

OigHotlineConfirmationPageMap = dict(ConfirmationMessageId = "ctl00_PlaceHolderMain_FormSubmittedContent",
)

OigHotlinePageMap = dict(AnonymousRadioButtonId         = "ctl00_PlaceHolderMain_Confidentiality_0",
                         AllegedMisconductFieldId       = "ctl00_PlaceHolderMain_WhoCommittedTheWrongDoing",
                         ContractorFraudFieldId         = "ctl00_PlaceHolderMain_ContractorOrGranteeFraudInformation",
                         IndividualDetailsFieldId       = "ctl00_PlaceHolderMain_WhatTheIndividualsDid",
                         InappropriateHappeningsFieldId = "ctl00_PlaceHolderMain_InappropriateHappenings",
                         MisconductWhenFieldId          = "ctl00_PlaceHolderMain_WhenMisconductOrWrongdoingOccured",
                         MisconductWhereFieldId         = "ctl00_PlaceHolderMain_WhereMisconductOrWrongdoingOccured",
                         MisconductHowFieldId           = "ctl00_PlaceHolderMain_HowWasMisconductOrWrongdoingCommitted",
                         CorrectiveActionsFieldId       = "ctl00_PlaceHolderMain_CurrentCorrectiveActionsOrStatus",
                         AdditionalInformationFieldId   = "ctl00_PlaceHolderMain_WhereCanAdditionalInformationBeFound",
                         SubmitButtonCss                = "input[value='Submit']",
)

OrganizationalChartPageMap = dict(OrganizationalChartPictureCss = "img"
)

InspectorGeneralPageMap = dict(InspectorGeneralBioXpath = "//div[contains(text(), 'Thorson')]"
)

OfficeManagementPageMap = dict(OfficeManagementBannerXpath = "//div[contains(text(), 'OIG Office of Management')]"
)

OfficeInvestigationsPageMap = dict(OfficeInvestigationsBannerXpath = "//div[contains(text(), 'OIG Office of Investigations')]"
)

OfficeAuditPageMap = dict(OfficeAuditBannerXpath = "//div[contains(text(), 'Office of Audit')]"
)

OfficeCounselPageMap = dict(OfficeCounselBannerXpath = "//div[contains(text(), 'Office of Counsel')]"
)

IgDeskbookPageMap = dict(IgDeskbookBannerXpath = "//div[contains(text(), 'The Inspector General Deskbook')]",
                         IgDeskbookIntroId     = "anch_202",
                         IgDeskbookVol1Part1Id = "anch_203",
                         IgDeskbookVol1Part2Id = "anch_204",
                         IgDeskbookVol1Part3Id = "anch_205",
                         IgDeskbookVol1Part4Id = "anch_206",
                         IgDeskbookVol2Id      = "anch_207",
                         IgDeskbookVol3Id      = "anch_208",
                         IgDeskbookVol4Part1Id = "anch_209",
                         IgDeskbookVol4Part2Id = "anch_210",
                         IgDeskbookVol4Part3Id = "anch_211"
)