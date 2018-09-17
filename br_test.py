"""
Write a smoke test to verify the functionality of the B/R home page. You may use selenium web-driver to do this.
This doesn’t have to be exhaustive, but feel free to add additional ideas of what could be automated if you are
running out of time.
"""

"""
This test quickly opens the b/r homepage, checks the title, and checks that a link (NFL on the top bar) is working.
The next  bits of functionality I'd check would be to confirm an image is loading properly, then see if I could find a
date on the page to confirm I wasn't looking at something cached. Lastly, I'd mess around with the Edit Teams
functionality, but would need to go through a dummy account creation for that.

The only gotcha in my setup is that the chromedriver needs to be sitting in a folder on C:/ (or change the location
in the code below). 
"""
import br_page
from selenium import webdriver


driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")


def test_BR():
    br = br_page.MainPage(driver)
    br.open_page()
    assert br.is_title_good()
    assert br.is_nfl_link_working()
    driver.quit()


test_BR()
