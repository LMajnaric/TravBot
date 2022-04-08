import Bot
# //*[@id="resourceFieldContainer"]/a[2]
# /html/body/div[4]/div[3]/div[2]/div/div[1]/a[4]/div
# /html/body/div[4]/div[3]/div[2]/div/div[1]/a[15]/div
# /html/body/div[4]/div[3]/div[2]/div/div[1]/a[16]/div
# //*[@id="resourceFieldContainer"]
class ResourceAnalyzer:
    def __init__(self):
        pass

    def get_res_lvls(self,res_fields):
        # Lists for each resource
        self.wood = []
        self.clay = []
        self.iron = []
        self.crop = []

        self.wood_slots = []
        self.clay_slots = []
        self.iron_slots = []
        self.crop_slots = []


        def numbering(res_lvl):
            # If field is level 0 actually write 0 instead of an empty string
            if res_lvl == '':
                return '0'
            else:
                return res_lvl

        for i in range(1,19):
            # Search for resource level number and resource level type using xpath
            # and sort everything into the defined lists
            resource_lvl = res_fields.find_element_by_xpath('//*[@id="resourceFieldContainer"]/div['+ str(i) +']/div').text
            res_name = res_fields.find_element_by_xpath('//*[@id="resourceFieldContainer"]/div[' + str(i) + ']').get_attribute('class').split()
            if res_name[3] == 'gid1':
                # print('Wood: ', end="", flush=True)
                self.wood.append(numbering(resource_lvl))
                self.wood_slots.append(res_name[4].strip('buildingSlot'))
            elif res_name[3] == 'gid2':
                # print('Clay: ', end="", flush=True)
                self.clay.append(numbering(resource_lvl))
                self.clay_slots.append(res_name[4].strip('buildingSlot'))
            elif res_name[3] == 'gid3':
                # print('Iron: ', end="", flush=True)
                self.iron.append(numbering(resource_lvl))
                self.iron_slots.append(res_name[4].strip('buildingSlot'))
            elif res_name[3] == 'gid4':
                # print('Crop: ', end="", flush=True)
                self.crop.append(numbering(resource_lvl))
                self.crop_slots.append(res_name[4].strip('buildingSlot'))
            # if resource_lvl == '':
            #     print('0')
            # else:
            #     print(resource_lvl)
            # Uncomment these if you want your resources to be printed like Wood: X, Crop: Y etc.
        print('Wood levels: ',self.wood,'\nClay levels: ',self.clay,'\nIron levels: ',self.iron ,'\nCrop levels: ',self.crop)
        print('Wood ids: ',self.wood_slots, '\nClay ids: ',self.clay_slots, '\nIron ids: ',self.iron_slots, '\nCrop ids:  ',self.crop_slots )

    def get_stock(self,stock):
        storage = []
        for i in range(1,5):
            capacity = stock.find_element_by_id('l'+str(i)).text
            storage.append(capacity)
        print('Total resources: ',storage)

    def get_res_production(self,production):
        prod = []
        numbers = production.find_elements_by_class_name('num')
        for number in numbers:
            prod.append(number.text)
            # print(number.text)
        # Escape unicode characters before getting the production
        prod = [key.strip('\u202c') for key in prod]
        prod = [key.strip('\u202d') for key in prod]
        print('Hourly production: ',prod)

    # def upgrade_lowest_lvl_res(self):
        # self.driver.get(Bot.url + 'build.php?id=')