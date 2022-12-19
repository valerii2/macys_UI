import time

import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:


    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        # homepage_nav.driver.delete_cookie('ak_bmsc')    # delete cookie which protect from automation
        # cookies = homepage_nav.driver.get_cookies()  # get all cookies from site
        # print(cookies)
        # cookies_names = [cookie['name'] for cookie in cookies]   #  get all names in cookies list
        # print('-----------------------------------------------------------------------------')
        # print(cookies_names)
        # actual_links = homepage_nav.get_nav_links_text()
        # print(actual_links)
        # expected_links = homepage_nav.NAV_LINK_TEXT
        # print(expected_links)
        # assert expected_links == actual_links, 'Validating Nav Links Text'
        for index in range(8):
            homepage_nav.get_nav_links()[index].click()   # clicking all head bar links in range
            # homepage_nav.driver.delete_all_cookies()    # deleting all cookies for pass security checking on automation
        # homepage_nav.get_nav_link_by_name('Shoes').click()  # search and open link by name
        #     homepage_nav.driver.delete_cookie('ak_bmsc')  #  delete cookie which protect from automation
            time.sleep(2)

