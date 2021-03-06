from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
# User hears about an online to-do app
# User goes to check the homepage

        self.browser.get('http://127.0.0.1:8000/')

# User notices the  page title and header mention To-do lists

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

# User is invited to enter a to-do item straight away

        inputbox = self.browser.find_element_by_id('id_new_item')

# User types in a to-do item

        inputbox.send_keys('Use book to make dollah')

# User hits enter and the page updates and  now lists the todo item

        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Finish the obey_goat book ')

# There is still a text box inviting user to add another to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use book to make dollah')
        inputbox.send_keys(Keys.Enter)
# The page updates again and now displays 2 to-do items
        self.check_for_row_in_list_table('1: Finish the obay_goat book')
        self.check_for_row_in_list_table('2: Use book to make dollah')
# User wonders if the site will remember their lists, the user sees that there is a unique url
# for the list
# There is also some explaination text to that effect
# User visits url. The to-do list is there
# The user is satisfied
if __name__ == '__main__':
    unittest.main(warnings='ignore')