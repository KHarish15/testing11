import pytest
from playwright.sync_api import Playwright, sync_playwright

# Test successful login
def test_login_success(page):
    page.fill("#inputEmail", "john.doe@example.com")
    page.fill("#inputPassword", "P@ssw0rd123")
    page.click("button[type='submit']")
    # Check for successful login logic (e.g., redirection, etc.)

# Test invalid email format
def test_login_invalid_email(page):
    # ERROR HANDLING: Invalid email format
    # Tests that login fails with an error message for an invalid email
    page.fill("#inputEmail", "invalid_email_format")
    page.fill("#inputPassword", "short")
    page.click("button[type='submit']")
    # Check if an error message is displayed (example)

# Test missing email
def test_login_missing_email(page):
    # ERROR HANDLING: Missing email
    # Tests that login fails with an error message if no email is entered
    page.fill("#inputPassword", "noemail@123")
    page.click("button[type='submit']")
    # Check if an error message is displayed (example)

# Test missing password
def test_login_missing_password(page):
    # ERROR HANDLING: Missing password
    # Tests that login fails if no password is entered
    page.fill("#inputEmail", "harry.potter@hogwarts.edu")
    page.click("button[type='submit']")
    # Check for an error message.

# Test for empty fields
def test_login_empty_fields(page):
  #ERROR HANDLING: Empty email field 
  # Tests if input fields validate correctly with empty fields
  page.fill("#inputEmail", "")
  page.fill("#inputPassword", "")
  page.click("button[type='submit']")
  # Assert an error message about both email and password

# Run test function
def run_tests(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("file:///path/to/your/login.html") # Replace with your HTML file path
    test_login_success(page)
    test_login_invalid_email(page)
    test_login_missing_email(page)
    test_login_missing_password(page)
    test_login_empty_fields(page)
    context.close()
    browser.close()

#Run tests using pytest --browser=chromium
@pytest.fixture(scope="module")
def page(playwright):
	  browser = playwright.chromium.launch(headless=False)
	  context = browser.new_context()
	  page = context.new_page()
	  yield page
	  context.close()
	  browser.close()
    

# Run tests
if __name__ == "__main__":
    with sync_playwright() as playwright:
        run_tests(playwright)