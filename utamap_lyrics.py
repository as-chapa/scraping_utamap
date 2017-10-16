# -*- coding: utf-8 -*-

BASE_URL = 'https://www.uta-net.com/artist/7429/'
OUT_FILE_NAME = "output.csv"

import re

from selenium import webdriver as wd
browser = wd.PhantomJS()

browser.get(BASE_URL)

lyric_links = list()

#get next links
for link in browser.find_elements_by_tag_name("a"):
    if re.search('/song/',link.get_attribute("href")):
        lyric_links.append(link.get_attribute("href"))

#write lyric to file
with open(OUT_FILE_NAME, 'w') as fout:
    for lyric_link in lyric_links:
        browser.get(lyric_link)
        fout.write(browser.find_element_by_id("kashi_area").text + '\r\n')

browser.quit()
