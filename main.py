import os
import glob

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
from instabot import Bot

bot = Bot()
bot.login(username="i.m_MAFIAa", password="Aspire3")
bot.follow(['aliaabhatt','alluarjunonline'])
# bot.unfollow("wscubetechindia")
# def follows():
#     followlist = []
#     rvalue = int(input("How many people do You want to follow"))
#     for i in range(rvalue):
#         infollow = input("Enter list")
#         followlist.append(infollow)
#     # print(followlist)
#     for item in followlist:
#         bot.follow(followlist[])
# follows()