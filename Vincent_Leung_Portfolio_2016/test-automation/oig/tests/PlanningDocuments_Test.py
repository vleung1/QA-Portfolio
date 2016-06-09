from oig.Constants                      import TT_Constants
from oig.pages.WelcomePage              import WelcomePage
from oig.pages.PlanningDocumentsPage    import PlanningDocumentsPage
from oig.BaseTestCase                   import BaseTestCase
import unittest
import nose
from nose.plugins.attrib                import attr


#verify Planning Documents page loads and verify the content update link loads
class PlanningDocumentsTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(PlanningDocumentsTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(TT_Constants['Base_URL'])

    @attr(priority="low") 
    def test_PlanningDocumentsTest(self):
        planning_documents_obj = WelcomePage(self.driver)
        planning_documents_obj.click_planning_documents_link()
        planning_documents_obj = PlanningDocumentsPage(self.driver)
        planning_documents_obj.verify_update_content()

    def tearDown(self):
        super(PlanningDocumentsTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



