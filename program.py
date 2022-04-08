import Bot
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
import sys


def main():
    if len(sys.argv) > 3:
        print("System variables not correct")
        return

    bot = Bot.Bot()
    bot.start()
    bot.login()
    # bot.track_raid_frequency(60)
    bot.report_analyzer()
    # bot.get_raiders_table()
    # bot.get_resource_info()
    # bot.hero_adventure_picker()
    # sleep(5)

if __name__ == '__main__':
    main()