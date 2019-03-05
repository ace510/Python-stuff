import discord
import asyncio

dis_client = discord.Client()

@dis_client.event
async def on_ready():
    print('Logged in as')
    print(dis_client.user.name)
    print(dis_client.user.id)
    print('------')

@dis_client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await dis_client.send_message(message.channel, 'Calculating messages...')
        async for log in dis_client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await dis_client.edit_message(tmp, 'you have %s messages'  % counter)

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await dis_client.send_message(message.channel, 'Done sleeping')

token_file = open("C:\\valley_forge\\Python-stuff\\Project_Baez\\.token")
token_wing = token_file.read()
print(token_wing)
dis_client.run('ianhclark510@gmail.com','G00glebaby!')