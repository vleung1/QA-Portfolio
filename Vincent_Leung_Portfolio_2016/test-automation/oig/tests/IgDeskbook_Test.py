from oig.Constants            import TT_Constants
from oig.pages.IgDeskbookPage import IgDeskbookPage
from oig.BaseTestCase         import BaseTestCase
import unittest
from nose.plugins.attrib      import attr


#verify Inspector General Deskbook page loads and able to download all the files on the page
class IgDeskbookTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(IgDeskbookTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(URL.replace("default", "igdeskbook"))

    @attr(priority="medium") 
    def test_IgDeskbookTest(self):
        ig_deskbook_page_obj = IgDeskbookPage(self.driver)
        ig_deskbook_page_obj.click_and_download()

    def tearDown(self):
        super(IgDeskbookTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



