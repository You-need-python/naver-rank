from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.google.co.kr/")

sleep(1)
elem = driver.find_element_by_name("q")
elem.send_keys('네이버')
elem.send_keys(Keys.RETURN)

sleep(0.5)
driver.find_elements_by_css_selector(".LC20lb.DKV0Md")[0].click()

sleep(0.5)
driver.find_element_by_css_selector(".keyword").click()

sleep(0.5)
driver.find_elements_by_css_selector(".range.NM_RTK_VIEW_filter_range")[4].click()
sleep(0.25)
driver.find_elements_by_css_selector(".range.NM_RTK_VIEW_filter_range")[9].click()
sleep(0.25)
driver.find_elements_by_css_selector(".range.NM_RTK_VIEW_filter_range")[14].click()
sleep(0.25)
driver.find_elements_by_css_selector(".range.NM_RTK_VIEW_filter_range")[19].click()
sleep(0.25)
driver.find_elements_by_css_selector(".range.NM_RTK_VIEW_filter_range")[24].click()

sleep(0.5)
driver.find_elements_by_css_selector(".age.NM_RKT_VIEW_filter_age")[5].click()
sleep(0.5)
driver.find_element_by_css_selector("#NM_RTK_VIEW_set_btn").click()

count = 1
rank = []
pure_keywords = []
keywords = driver.find_elements_by_css_selector("span.keyword")
for i in keywords:
    if len(i.text)>=1 and i.text not in pure_keywords:
        pure_keywords.append(i.text)
        rank.append(str(count) + '위: ' + i.text)
        count += 1

rank = '\n'.join(rank)
print(rank)

driver.close()

#cd selenium\Scripts
#activate