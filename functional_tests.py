from selenium import webdriver
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
            self.fail('Finish the test!')

	    #User is invited to enter a to-do item straight away

	    #User types in a to-do item

	    #User hits enter and the page updates and  now lists the todo item

	    #There is stull a text box inviting user to add another to-do item

	    #The page updates again and now displays 2 to-do items

	    #User wonders if the site will remember their lists, the user sees that there is a unique url 
	    #for the list
            #There is also some explaination text to that effect

            #User visits url. The to-do list is there

            #The user is satisfied
if __name__ == '__main__':
    unittest.main(warnings='ignore')

