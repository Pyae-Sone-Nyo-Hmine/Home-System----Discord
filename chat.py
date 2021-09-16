import discord
import time


### Set the discord bot token if not already ###
### Go to discord developer portal for bot   ###

client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith('BoB image'):
        try:
            await message.channel.send(file=discord.File('image.png'))
        except:
            await message.channel.send("Image not available.")

    if message.content.startswith('BoB clear'):
        await message.channel.send("Deleting history ...")
        time.sleep(1)
        await message.channel.purge()

    if message.content.startswith("Hi"):
        await message.channel.send("Hello")


client.run("Enter token of discord bot here!!")
