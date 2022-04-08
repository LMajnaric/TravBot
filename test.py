from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
# options = Options()
# options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# driver = webdriver.Chrome(options= options,
#                           executable_path=r'C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
# driver.get('http://google.com/')

import pandas as pd

# list1 = ['https://nys.x5.international.travian.com/report?id=211806856&aid=47', 'https://nys.x5.international.travian.com/report?id=211856349&aid=47', 'https://nys.x5.international.travian.com/report?id=211776634&aid=47', 'https://nys.x5.international.travian.com/report?id=211650087&aid=47', 'https://nys.x5.international.travian.com/report?id=211621870&aid=47', 'https://nys.x5.international.travian.com/report?id=211687074&aid=47', 'https://nys.x5.international.travian.com/report?id=211832460&aid=47', 'https://nys.x5.international.travian.com/report?id=211622702&aid=47', 'https://nys.x5.international.travian.com/report?id=211729698&aid=47', 'https://nys.x5.international.travian.com/report?id=211691219&aid=47', 'https://nys.x5.international.travian.com/report?id=211907204&aid=47', 'https://nys.x5.international.travian.com/report?id=211853269&aid=47', 'https://nys.x5.international.travian.com/report?id=211678555&aid=47', 'https://nys.x5.international.travian.com/report?id=211782262&aid=47', 'https://nys.x5.international.travian.com/report?id=211854632&aid=47', 'https://nys.x5.international.travian.com/report?id=211640927&aid=47', 'https://nys.x5.international.travian.com/report?id=211970801&aid=47', 'https://nys.x5.international.travian.com/report?id=211878644&aid=47', 'https://nys.x5.international.travian.com/report?id=211839847&aid=47', 'https://nys.x5.international.travian.com/report?id=211951480&aid=47', 'https://nys.x5.international.travian.com/report?id=211824998&aid=47', 'https://nys.x5.international.travian.com/report?id=211906405&aid=47', 'https://nys.x5.international.travian.com/report?id=211798644&aid=47', 'https://nys.x5.international.travian.com/report?id=211954898&aid=47', 'https://nys.x5.international.travian.com/report?id=211646107&aid=47', 'https://nys.x5.international.travian.com/report?id=211890944&aid=47', 'https://nys.x5.international.travian.com/report?id=211575068&aid=47', 'https://nys.x5.international.travian.com/report?id=211606763&aid=47', 'https://nys.x5.international.travian.com/report?id=211708154&aid=47', 'https://nys.x5.international.travian.com/report?id=211584164&aid=47', 'https://nys.x5.international.travian.com/report?id=211965706&aid=47', 'https://nys.x5.international.travian.com/report?id=211735649&aid=47', 'https://nys.x5.international.travian.com/report?id=211625656&aid=47', 'https://nys.x5.international.travian.com/report?id=211736301&aid=47', 'https://nys.x5.international.travian.com/report?id=211879425&aid=47', 'https://nys.x5.international.travian.com/report?id=211734158&aid=47', 'https://nys.x5.international.travian.com/report?id=211678398&aid=47', 'https://nys.x5.international.travian.com/report?id=211592123&aid=47', 'https://nys.x5.international.travian.com/report?id=211949188&aid=47', 'https://nys.x5.international.travian.com/report?id=211851305&aid=47', 'https://nys.x5.international.travian.com/report?id=211759074&aid=47', 'https://nys.x5.international.travian.com/report?id=211869208&aid=47', 'https://nys.x5.international.travian.com/report?id=211976883&aid=47', 'https://nys.x5.international.travian.com/report?id=211567282&aid=47', 'https://nys.x5.international.travian.com/report?id=211801814&aid=47', 'https://nys.x5.international.travian.com/report?id=211713983&aid=47', 'https://nys.x5.international.travian.com/report?id=211916630&aid=47', 'https://nys.x5.international.travian.com/report?id=211929908&aid=47', 'https://nys.x5.international.travian.com/report?id=211745166&aid=47']
#
# list1 = list(set(list1))
# print(len(list1))

# df = pd.DataFrame({'col':list1})
# df.to_csv(path_or_buf='E:\Pandas csv\links.csv')
df = pd.read_csv(filepath_or_buffer='E:\Pandas csv\\2.csv')
# print(df.head())
col_one_list = df['content'].tolist()
print(col_one_list)
mylist = ["%.4d" % i for i in range(10000)]
print(mylist)
for i in range(len(col_one_list)):
    col_one_list[i]=str(col_one_list[i])

print(col_one_list)

l3 = [x for x in mylist if x not in col_one_list]
print(l3)
print(len(l3))