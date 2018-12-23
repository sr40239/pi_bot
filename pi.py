import discord
import CONSTS
import getImageURL
from numpy.random import *
client = discord.Client()


API_KEY = CONSTS.G_KEY
CUSTOM_SEARCH_ENGINE = CONSTS.ENGINE_KEY

page_limit = 1
search_word = '中島由貴'


@client.event
async def on_ready():
    print("Logged in " + client.user.name)
    print("-----")

@client.event
async def on_message(message):
    if client.user != message.author:
        repMsg = recognizeWord(message)
        if repMsg != "":
            await client.send_message(message.channel, repMsg)


def getZidoriUrl():
    imgList = getImageURL.getImageUrl(API_KEY, CUSTOM_SEARCH_ENGINE, search_word, page_limit)
    return imgList[randint(len(imgList))]

# ぴが返してくれる言葉
def recognizeWord(message):
    # 今はまだおうむ返し
    words = {}
    words['すき'] = "私も好きです!" + message.author.name + "さん!"
    words['かわいい'] = "ありがとうございます えへへ(//∇//)"
    words['自撮りちょうだい'] = getZidoriUrl()
    

    word = words.get(message.content, "")
    print("word = " + word)
    return word

client.run(CONSTS.TOKEN)