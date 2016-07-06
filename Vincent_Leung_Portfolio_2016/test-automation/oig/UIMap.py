# -*- coding: utf-8 -*-
#UI mapping of WebElements in each page object
WelcomePageMap = dict(WelcomeBannerXpath           = "//img[@alt='Office of the Inspector General']",
                      SearchFieldXpath             = "//input[@class='usagov-search-autocomplete']",
                      SearchSubmitButtonName       = "mynewbutton2",
                      ShareButtonId                = "anch_205",
                      FacebookShareButtonXpath     = "//span[contains(text(), 'Facebook')]",
                      TwitterShareButtonXpath      = "//span[contains(text(), 'Twitter')]",
                      OrganizationalChartLinkId    = "anch_178",
                      InspectorGeneralLinkId       = "anch_172",
                      OfficeManagementLinkId       = "anch_176",
                      OfficeInvestigationsLinkId   = "anch_175",
                      OfficeAuditLinkId            = "anch_173",
                      OfficeCounselLinkId          = "anch_174",
                      ReportsLinkId                = "anch_179",
                      RecoveryActLinkId            = "anch_180",
                      EqualOpportunityLinkId       = "anch_181",
                      IgActLinkId                  = "anch_183",
                      ManagementChallengesLinkId   = "anch_184",
                      SblfLinkId                   = "anch_186",
                      ConferenceSpendingLinkId     = "anch_189",
                      RestoreActLinkId             = "anch_190",
                      TestimoniesDocumentsLinkId   = "anch_192",
                      VacanciesLinkId              = "anch_195",
                      WhistleblowerLinkId          = "anch_194",
                      PrivacyAssessmentLinkId      = "anch_188",
                      PlanningDocumentsLinkId      = "anch_187",
                      NewHireOrientationLinkId     = "anch_185",
                      FraudAlertsLinkId            = "anch_182"
)

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

OrganizationalChartPageMap = dict(OrganizationalChartXpath = "//img[contains(@src, 'Chart.jpg')]"
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

ReportsPageMap = dict(ReportsPageBannerXpath      = "//div[contains(text(), 'Reports')]",
                      ReportsAuditLinkId          = "anch_202",
                      ReportsOtherLinkId          = "anch_203",
                      ReportsCongressLinkId       = "anch_205",
                      ReportsInvestigationsLinkId = "anch_206",
                      ReportsPeerLinkId           = "anch_207"
)

ReportsAuditPageMap = dict(ReportsAuditBannerXpath = "//div[contains(text(), 'Audit and Evaluation Reports')]"
)

ReportsOtherPageMap = dict(ReportsOtherBannerXpath = "//div[contains(text(), 'Other Documents')]"
)

ReportsCongressPageMap = dict(ReportsCongressBannerXpath = "//div[contains(text(), 'Semiannual Reports to Congress')]"
)

ReportsInvestigationsPageMap = dict(ReportsInvestigationsBannerXpath = "//div[contains(text(), 'Investigations Reports')]"
)

ReportsPeerPageMap = dict(ReportsPeerBannerXpath = "//div[contains(text(), 'Peer Audit Reports')]"
)

RecoveryActPageMap = dict(RecoveryActBannerXpath     = "//div[contains(text(), 'Recovery Act')]",
                          RecoveryActDocumentsLinkId = "anch_203"
)

RecoveryActDocumentsPageMap = dict(RecoveryActDocumentsBannerXpath = "//a[contains(text(), 'Audit Reports: Recovery Act')]"
)

EqualOpportunityPageMap = dict(EqualOpportunityBannerXpath = "//div[contains(text(), 'Equal Employment Opportunity')]",
                               ReasonableAccomodationPdfId = "anch_202",
                               EeoPolicyDocId              = "anch_203",
                               DisputeResolutionPdfId      = "anch_204",
                               OfficialTimePdfId           = "anch_205"
)

IgActPageMap = dict(IgActBannerXpath = "//div[contains(text(), 'Inspector General Act of 1978')]"
)

ManagementChallengesPageMap = dict(ManagementChallengesBannerXpath = "//div[contains(text(), 'Management Challenges Letter')]"
)

SblfPageMap = dict(SblfBannerXpath       = "//div[contains(text(), 'Small Business Lending Fund Program and State Small Business Credit Initiative')]",
                   SblfReportsLinksXpath = "//strong[contains(text(), 'SBLF Program and SSBCI Reports')]"
)

ConferenceSpendingPageMap = dict(ConferenceSpendingBannerXpath = "//div[contains(text(), 'Reports on Conference Spending to Support Agency Operations')]",
                                 ConferenceSpending2015Xpath   = "//td[contains(text(), '​$340,612.71')]"
)

RestoreActPageMap = dict(RestoreActBannerXpath = "//div[contains(text(), 'The Restore Act')]",
                         GulfCoastEmailXpath   = "//a[@href='mailto:GulfCoastRestorationHotline@oig.treas.gov']"
)

TestimoniesDocumentsPageMap = dict(TestimoniesDocumentsBannerXpath = "//div[contains(text(), 'Testimonies & Other Documents')]"
)

VacanciesPageMap = dict(VacanciesBannerXpath = "//div[contains(text(), 'Vacancies')]",
                        ApplicantGuideId     = "anch_205",
                        VeteranGuideId       = "anch_206"
)

WhistleblowerPageMap = dict(WhistleblowerPathXpath = "//div[contains(text(), 'Whistleblower Protection')]",
                            WhistleblowerPdfXpath  = "//a[@href='/about/organizational-structure/ig/Agency%20Documents/Whistleblower%20Protection%20Ombudsman.pdf']" 
)

PrivacyAssessmentPageMap = dict(PrivacyAssessmentBannerXpath = "//div[contains(text(), 'Privacy Impact Assessment')]",
                                PrivacyAssessmentPdfId       = "anch_203"
)

PlanningDocumentsPageMap = dict(PlanningDocumentsBannerXpath = "//div[contains(text(), 'Planning Documents')]",
                                ContentUpdateLinkId          = "anch_202"
)

EmailUpdatesPageMap = dict(EmailAddressFieldId = "email"
)

FraudAlertsPageMap = dict(FraudAlertsBannerXpath        = "//div[contains(text(), 'Fraud Alerts')]",
                          FraudSecuritiesLinkId         = "anch_206",
                          FraudSecuritiesScamsLinkId    = "anch_207",
                          FraudSecuritiesPhonyLinkId    = "anch_208",
                          FraudHistoricalBondLinkId     = "anch_209",
                          FraudBankInstrumentLinkId     = "anch_210",
                          FraudProtectYourselfLinkId    = "anch_211",
                          FraudOtherFraudLinkId         = "anch_212",
                          FraudAgainstMisuseLinkId      = "anch_213",
                          FraudBogusSightLinkId         = "anch_214",
                          FraudTigScamsDocId            = "anch_205",
                          FraudThreatsDemandsDocId      = "anch_216",
                          FraudAmericanBankersPdfId     = "anch_217",
                          FraudAutomobileDealersPdfId   = "anch_218",
                          FraudRealtorsAssociationPdfId = "anch_219",
                          FraudPromissoryNotePdfId      = "anch_220",
                          FraudPrivateBondPdfId         = "anch_221",
                          FraudBpdCheckPdfId            = "anch_222"
)

FraudSecuritiesPageMap = dict(FraudSecuritiesBannerXpath = "//h2[contains(text(), 'How Marketable Treasury Securities Work')]"
)

FraudSecuritiesScamPageMap = dict(FraudSecuritiesScamsBannerXpath = "//h2[contains(text(), 'Scams Involving Treasury Securities')]"
)

FraudSecuritiesPhonyPageMap = dict(FraudSecuritiesPhonyBannerXpath = "//h2[contains(text(), 'Examples of Known Phony Securities')]"
)

FraudHistoricalBondPageMap = dict(FraudHistoricalBondBannerXpath = "//h2[contains(text(), 'Historical Bond Fraud')]"
)

FraudBankInstrumentPageMap = dict(FraudBankInstrumentBannerXpath = "//h2[contains(text(), 'Prime Bank Investment Fraud')]"
)

FraudProtectYourselfPageMap = dict(FraudProtectYourselfBannerXpath = "//h2[contains(text(), 'How to Protect Yourself from Investment Scams')]"
)

FraudOtherFraudPageMap = dict(FraudOtherFraudBannerXpath = "//h2[contains(text(), 'Other Fraud Sites of Interest')]"
)

FraudAgainstMisusePageMap = dict(FraudAgainstMisuseBannerXpath = "//h2[contains(text(), 'Prohibition Against Misuse of Treasury Names, Terms, Symbols, Stationery, Etc.')]"
)

FraudBogusSightPageMap = dict(FraudBogusSightBannerXpath = "//h2[contains(text(), 'Bogus Sight Drafts/Bills of Exchange Drawn on the Treasury')]"
)

NewHireOrientationPageMap = dict(OrientationWelcomeBannerXpath     = "//div[contains(text(), 'Welcome')]",
                                 OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                 OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                 OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                 OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                 OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                 OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                 OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                 OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                 OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                 OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                 OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                 OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                 OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']",
                                 OrientationEeoPdfId               = "anch_216",
                                 OrientationDiversityPdfId         = "anch_217"
)

OrientationBeforeReportPageMap = dict(OrientationBeforeReportBannerXpath = "//div[contains(text(), 'Before You Report')]",
                                      OrientationWelcomeLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                      OrientationBeforeReportLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                      OrientationFirstDayLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                      OrientationNoFearLinkXpath         = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                      OrientationPayLeaveLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                      OrientationBenefitsLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                      OrientationWorkersCompLinkXpath    = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                      OrientationEthicsLinkXpath         = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                      OrientationWhistleblowerLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                      OrientationHrConnectLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                      OrientationForgottenLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                      OrientationConstitutionLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                      OrientationAbbreviationsLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationFirstDayPageMap = dict(OrientationFirstDayBannerXpath    = "//div[contains(text(), 'On Your First Day')]",
                                  OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                  OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                  OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                  OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                  OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                  OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                  OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                  OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                  OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                  OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                  OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                  OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                  OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationNoFearPageMap = dict(OrientationNoFearBannerXpath      = "//div[contains(text(), 'No Fear Act')]",
                                OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationPayLeavePageMap = dict(OrientationPayLeaveBannerXpath    = "//div[contains(text(), 'Pay & Leave')]",
                                  OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                  OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                  OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                  OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                  OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                  OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                  OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                  OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                  OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                  OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                  OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                  OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                  OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
) 

OrientationBenefitsPageMap = dict(OrientationBenefitsBannerXpath    = "//div[contains(text(), 'Benefits')]",
                                  OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                  OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                  OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                  OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                  OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                  OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                  OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                  OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                  OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                  OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                  OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                  OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                  OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationWorkersCompPageMap = dict(OrientationWorkersCompBannerXpath = "//div[contains(text(), 'Compensation')]",
                                     OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                     OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                     OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                     OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                     OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                     OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                     OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                     OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                     OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                     OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                     OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                     OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                     OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationEthicsPageMap = dict(OrientationEthicsBannerXpath      = "//div[contains(text(), 'Ethics')]",
                                OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationWhistleblowerPageMap = dict(OrientationWhistleblowerBannerXpath = "//div[contains(text(), 'Whistleblower Protection')]",
                                       OrientationWelcomeLinkXpath         = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                       OrientationBeforeReportLinkXpath    = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                       OrientationFirstDayLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                       OrientationNoFearLinkXpath          = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                       OrientationPayLeaveLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                       OrientationBenefitsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                       OrientationWorkersCompLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                       OrientationEthicsLinkXpath          = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                       OrientationWhistleblowerLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                       OrientationHrConnectLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                       OrientationForgottenLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                       OrientationConstitutionLinkXpath    = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                       OrientationAbbreviationsLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
) 

OrientationHrConnectPageMap = dict(OrientationHrConnectBannerXpath   = "//div[contains(text(), 'HR Connect')]",
                                   OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                   OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                   OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                   OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                   OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                   OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                   OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                   OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                   OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                   OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                   OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                   OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                   OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
) 

OrientationForgottenPageMap = dict(OrientationForgottenBannerXpath   = "//div[contains(text(), 'What Have I Forgotten?')]",
                                   OrientationWelcomeLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                   OrientationBeforeReportLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                   OrientationFirstDayLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                   OrientationNoFearLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                   OrientationPayLeaveLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                   OrientationBenefitsLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                   OrientationWorkersCompLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                   OrientationEthicsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                   OrientationWhistleblowerLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                   OrientationHrConnectLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                   OrientationForgottenLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                   OrientationConstitutionLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                   OrientationAbbreviationsLinkXpath = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationConstitutionPageMap = dict(OrientationConstitutionBannerXpath = "//div[contains(text(), 'Constitution Initiative')]",
                                      OrientationWelcomeLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                      OrientationBeforeReportLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                      OrientationFirstDayLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                      OrientationNoFearLinkXpath         = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                      OrientationPayLeaveLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                      OrientationBenefitsLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                      OrientationWorkersCompLinkXpath    = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                      OrientationEthicsLinkXpath         = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                      OrientationWhistleblowerLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                      OrientationHrConnectLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                      OrientationForgottenLinkXpath      = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                      OrientationConstitutionLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                      OrientationAbbreviationsLinkXpath  = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)

OrientationAbbreviationsPageMap = dict(OrientationAbbreviationsBannerXpath = "//div[contains(text(), 'Key Abbreviations')]",
                                       OrientationWelcomeLinkXpath         = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Welcome.aspx']",
                                       OrientationBeforeReportLinkXpath    = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Before-You-Report.aspx']",
                                       OrientationFirstDayLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/On-Your-First-Day.aspx']",
                                       OrientationNoFearLinkXpath          = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/No-Fear.aspx']",
                                       OrientationPayLeaveLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Pay--Leave.aspx']",
                                       OrientationBenefitsLinkXpath        = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Benefits.aspx']",
                                       OrientationWorkersCompLinkXpath     = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Workers%27-Compensation.aspx']",
                                       OrientationEthicsLinkXpath          = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Ethics.aspx']",
                                       OrientationWhistleblowerLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Whistleblower-Protection.aspx']",
                                       OrientationHrConnectLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/HR-Connect.aspx']",
                                       OrientationForgottenLinkXpath       = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/What-Have-I-Forgotten.aspx']",
                                       OrientationConstitutionLinkXpath    = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Constitution-Initiative.aspx']",
                                       OrientationAbbreviationsLinkXpath   = "//a[@href='/about/organizational-structure/ig/Pages/New%20Employee%20Orientation/Key-Abbreviations.aspx']"
)



