import discord

from settings.settings import settingsManager


# @client.event
# async def on_message(message):
#     print(message)
# if message.author == client.user:
#     return
# # Download All Pictures  Code Section
# if message.content.startswith('!download'):
#     await message.channel.send("Ok !")
#     messages = await message.channel.history(limit=200).flatten()
#     try:
#         os.makedirs('/Pics/' + message.channel.category.name + '/' + message.channel.name)
#     except:
#         print("Error Creating Directory")
#     for x in messages:
#         print(x.content)
#         for a in x.attachments:
#             url = a.url
#             if url[0:26] == "https://cdn.discordapp.com":
#                 r = requests.get(url, stream=True)
#                 imageName = str(uuid.uuid4()) + '.jpg'
#                 dest = '/Pics/' + message.channel.category.name + '/' + message.channel.name + '/' + imageName
#                 with open(dest, 'wb') as out_file:
#                     print('Saving image: ' + imageName)
#                     shutil.copyfileobj(r.raw, out_file)
#     await message.channel.send("Finished Downloading!")
#


# @client.event
# async def on_ready():
#     print('Logged in as ' + client.user.name)


def main():
    client = discord.Client()
    client.run(settingsManager.getToken())


if __name__ == "__main__":
    main()
