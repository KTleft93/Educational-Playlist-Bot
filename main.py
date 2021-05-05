from selenium import webdriver

# Program ran in PyCharm Community 2020.2
# run pip install selenium from command line if encountering import issues
# Sometime the browser is slow to respond, in these cases the program may crash
# In these cases check your internet connection and run the program again
# This program was tested with google chrome https://chromedriver.chromium.org for chromedriver webdriver

import time

def login(browser):

        # Get Youtube URL
        browser.get("https://www.youtube.com")
        time.sleep(5)

        login = browser.find_element_by_css_selector("a[href='https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620']")
        login.click()
        time.sleep(5)

        # Log into test account
        username = browser.find_element_by_css_selector("[type='email']")
        username.send_keys("testing1deux3")
        nextGmailLoginButton = browser.find_element_by_css_selector("[class='VfPpkd-RLmnJb']")
        nextGmailLoginButton.click()
        time.sleep(5)
        password = browser.find_element_by_css_selector("[type='password']")
        password.send_keys("passclass99")
        nextGmailPasswordButton = browser.find_element_by_css_selector("[class='VfPpkd-RLmnJb']")
        nextGmailPasswordButton.click()
        time.sleep(5)

        # Search for Video
        search = browser.find_element_by_css_selector("[name='search_query']")
        searchButton = browser.find_element_by_css_selector("[id='search-icon-legacy']")
        # Change this to search a new video
        search.send_keys("news")
        searchButton.click()
        time.sleep(5)
        video = browser.find_element_by_css_selector("[class='title-and-badge style-scope ytd-video-renderer']")
        video.click()
        time.sleep(5)
        button = browser.find_element_by_css_selector("[aria-label='Save to playlist']")
        browser.execute_script("arguments[0].click();", button)
        #playListButton = browser.find_element_by_css_selector("[aria-label='Save to playlist']")
        #time.sleep(3)
       # playListButton.click()
        time.sleep(5)

        # Create and name playlist
        createPlaylist = browser.find_element_by_xpath('//a[@class="yt-simple-endpoint style-scope ytd-compact-link-renderer"]')
        time.sleep(5)
        createPlaylist.click()
        time.sleep(5)

        playlistName = browser.find_element_by_css_selector("[placeholder='Enter playlist name...']")
        playlistName.send_keys("Educational Leisure")
        time.sleep(5)
        createPlaylistButton = browser.find_element_by_xpath('//*[@id="actions"]/ytd-button-renderer/a')
        time.sleep(5)
        createPlaylistButton.click()

        # search for a new video and save to playlist
        search = browser.find_element_by_css_selector("[name='search_query']")
        searchButton = browser.find_element_by_css_selector("[id='search-icon-legacy']")
        search.clear()
        time.sleep(3)
        # change this to search for a new video tag
        search.send_keys("finance")
        searchButton.click()
        time.sleep(5)

        video = browser.find_element_by_css_selector("[class='title-and-badge style-scope ytd-video-renderer']")
        video.click()
        time.sleep(5)
        button = browser.find_element_by_css_selector("[aria-label='Save to playlist']")
        browser.execute_script("arguments[0].click();", button)
        time.sleep(5)

        addToPlaylist = browser.find_elements_by_id("checkboxContainer")
        addToPlaylist[1].click()
        time.sleep(3)
        closeAddToPlaylist = browser.find_element_by_css_selector("[icon='close']")
        closeAddToPlaylist.click()
        time.sleep(5)

        # search for a new video and save to playlist
        search = browser.find_element_by_css_selector("[name='search_query']")
        searchButton = browser.find_element_by_css_selector("[id='search-icon-legacy']")
        search.clear()
        time.sleep(3)
        # change this to search for a new video tag
        search.send_keys("how to")
        searchButton.click()
        time.sleep(5)

        video = browser.find_element_by_css_selector("[class='title-and-badge style-scope ytd-video-renderer']")
        video.click()
        time.sleep(5)
        button = browser.find_element_by_css_selector("[aria-label='Save to playlist']")
        browser.execute_script("arguments[0].click();", button)
        time.sleep(5)

        addToPlaylist = browser.find_elements_by_id("checkboxContainer")
        addToPlaylist[1].click()
        time.sleep(3)
        closeAddToPlaylist = browser.find_element_by_css_selector("[icon='close']")
        closeAddToPlaylist.click()
        time.sleep(5)


def main():
    browser = webdriver.Chrome()
    login(browser)
    time.sleep(5)
main()
