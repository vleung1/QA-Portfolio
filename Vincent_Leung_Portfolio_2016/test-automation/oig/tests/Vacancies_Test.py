from oig.Constants                  import TT_Constants
from oig.pages.WelcomePage          import WelcomePage
from oig.pages.VacanciesPage        import VacanciesPage
from oig.BaseTestCase               import BaseTestCase
import unittest
import nose
from nose.plugins.attrib            import attr


#verify Vacancies page loads and able to download all the files on the page
class VacanciesTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(VacanciesTest, self).setUp()
        URL = TT_Constants['Base_URL']
        self.navigate_to_page(TT_Constants['Base_URL'])

    @attr(priority="low") 
    def test_VacanciesTest(self):
        vacancies_obj = WelcomePage(self.driver)
        vacancies_obj.click_vacancies_link()
        vacancies_obj = VacanciesPage(self.driver)
        vacancies_obj.click_and_download()

    def tearDown(self):
        super(VacanciesTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



