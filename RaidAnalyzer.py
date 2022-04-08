import datetime
from openpyxl import Workbook

class RaidAnalyzer:
    wb = Workbook()
    ws = wb.active
    ws.title = 'Raid statistics'

    def __init__(self):
        # self.current_timestamp = str(datetime.now())
        self.wb = Workbook()

    def add_info(self, arr):
        if len(arr) == 1:
            return

        rank = 0
        name = ""
        points = 0

        for i in range(len(arr)):
            if i == 0:
                s = arr[i].text
                if s == "?":
                    s = "0"

                rank = s
            elif i == 1:
                name = arr[i].text
            elif i == 2:
                s = arr[i].text
                points = s
        print(rank,name,points)
        # print(arr)
