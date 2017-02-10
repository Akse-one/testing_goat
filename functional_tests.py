from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
#user hears about an online to-do app
#user goes to check the homepage
        self.browser.get('http://127.0.0.1:8000/')

 #User notices the  page title and header mention To-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
#User is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a To-Do item'
        )
#User types in a to-do item
        inputbox.send_keys('Finish the obey_goat book')
#User hits enter and the page updates and  now lists the todo item
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Finish the obey_goat book' for row in rows),
            "New To-Do Item did not appear in table"
        )
#There is still a text box inviting user to add another to-do item
        self.fail('Finish the test!')
#The page updates again and now displays 2 to-do items
#User wonders if the site will remember their lists, the user sees that there is a unique url
#for the list
#There is also some explaination text to that effect
#User visits url. The to-do list is there
#The user is satisfied
if __name__ == '__main__':
    unittest.main(warnings='ignore')