from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pandas as pd

from time import sleep
import random


import RaidAnalyzer
import ResourceAnalyzer
import HeroAnalyzer

class Bot:

    url = 'https://nys.x5.international.travian.com/'
    username = 'smoleon pottah'
    password = 'kojikuracjeovo'
    raid_analyzer = RaidAnalyzer.RaidAnalyzer()
    resource_analyzer = ResourceAnalyzer.ResourceAnalyzer()
    # hero_analyzer = HeroAnalyzer.HeroAnalyzer()



    def start(self):
        self.options = Options()
        self.options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        self.options.add_argument('--disable-gpu')
        self.options.add_argument("--headless")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options= self.options,
                                       executable_path=r'C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
        self.driver.get(self.url + 'login.php')
        sleep(1)

    def login(self):
        self.driver.find_element_by_css_selector('input.text').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        accept_cookies =self.driver.find_elements_by_id('cmpbntyestxt')
        if len(accept_cookies)>0:
            accept_cookies[0].click()
        other_cookies = self.driver.find_elements_by_class_name('cmpwelcomeprps')
        if len(other_cookies)>0:
            other_cookies[0].click()
        self.driver.find_element_by_id('s1').click()
        sleep(1)

    def get_raiders_table(self):
        self.driver.get(self.url + "statistiken.php?id=0&idSub=3")

        # Raiders table
        table = self.driver.find_element_by_id("top10_raiders")
        # Get info from table
        rows = table.find_elements_by_tag_name("tr")
        # col = rows[-1].find_elements_by_tag_name("td")  # My raid info
        # print(col[0])
        for row in rows:
            col = row.find_elements_by_tag_name('td')
            self.raid_analyzer.add_info(col)

    def get_resource_info(self):
        self.driver.get(self.url + 'dorf1.php')
        # Get resource fields table
        res_fields = self.driver.find_element_by_id('resourceFieldContainer')
        self.resource_analyzer.get_res_lvls(res_fields)

        # Get warehouse and granary current resources
        stock_bar = self.driver.find_element_by_id('stockBar')
        self.resource_analyzer.get_stock(stock_bar)

        production = self.driver.find_element_by_id('production')
        self.resource_analyzer.get_res_production(production)

    def get_buildings_info(self):
        self.driver.get(self.url + 'dorf2.php')
        # Get village id
        village_id = self.driver.find_element_by_id('village_map')


    def hero_adventure_picker(self):
        values = self.hero_analyzer.get_health()

    def track_raid_frequency(self,frequency):
        self.driver.get(self.url + 'position_details.php?x=-100&y=-100')
        self.raids = self.driver.find_element_by_class_name('tabContainer')
        print(self.raids)
        # self.raid0 = self.driver.find_elements_by_partial_link_text('today')
        # self.raid0[1].click()
        # print(self.raid0)
        # self.link = self.driver.find_element_by_xpath('//*[@id="troop_info"]/tbody/tr[1]/td/a[1]').get_attribute('href')
        # print(self.link)
        links = []
        for i in range(60):
            for tr in range(1,6):
                links.append(self.driver.find_element_by_xpath('//*[@id="troop_info"]/tbody/tr['
                                                                    + str(tr)
                                                                    + ']/td/a[1]').get_attribute('href'))
            sleep(frequency)
            self.driver.refresh()
            sleep(5)

        links = list(set(links))

        self.df = pd.DataFrame({'col':links})
        self.df.to_csv(path_or_buf='E:\Pandas csv\links.csv')
        print(links)

    def report_analyzer(self):
        df = pd.read_csv(filepath_or_buffer='E:\Pandas csv\links.csv', names=['Kurac', 'Links'])
        link = df.Links.tolist()
        player_names =[]
        village_names = []
        times = []
        for report in link:
            self.driver.get(report)
            player_name = self.driver.find_element_by_class_name('player').text
            village_name = self.driver.find_element_by_xpath('//*[@id="reportWrapper"]/div[2]/div[2]/div[2]/div/a[2]').text
            time = self.driver.find_element_by_class_name('time').text
            player_names.append(player_name)
            village_names.append(village_name)
            times.append(time)

        final = pd.DataFrame({'Player name': player_names,
                              'Village name': village_names,
                              'Date and time': times
                              })
        final.to_csv(path_or_buf='E:\Pandas csv\\final1hour.csv')



