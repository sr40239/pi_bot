import discord
TOKEN = ""
client = discord.Client()

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


# ぴが返してくれる言葉
def recognizeWord(message):
    # 今はまだおうむ返し
    words = {}
    words['すき'] = "私もです!" + message.author.name + "さん!"
    words['かわいい'] = "ありがとうございます えへへ(//∇//)"

    word = words.get(message.content, "")
    print("word = " + word)
    return word

client.run(TOKEN)