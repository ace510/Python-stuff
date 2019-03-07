import discord, asyncio, sys

dis_client = discord.Client()

@dis_client.event
async def on_ready():
    print('Logged in as')
    print(dis_client.user.name)
    print(dis_client.user.id)
    print('------')

@dis_client.event
async def on_message(message):
    

    print(notGarbo(message.author.name), end=': ')
    print(notGarbo(message.content), end='')

    for i in message.content.split():
        word_set.add(notGarbo(i).lower())
        print('the set is %s long' % len(word_set))

    if len( word_set ) > 500:
        with open('.output','a') as output_file:
            output_file.write(str(word_set))
            word_set.clear()


    # line.decode('utf-8','ignore').encode("utf-8")
    # (sys.stdout.encoding, errors='replace')
    # if message.content.startswith('!test'):
    #     counter = 0
    #     tmp = await dis_client.send_message(message.channel, 'Calculating messages...')
    #     async for log in dis_client.logs_from(message.channel, limit=100):
    #         if log.author == message.author:
    #             counter += 1
    #     await dis_client.edit_message(tmp, 'you have %s messages'  % counter)

    # elif message.content.startswith('!sleep'):
    #     await asyncio.sleep(5)
    #     await dis_client.send_message(message.channel, 'Done sleeping')

async def notGarbo(*garbo_text):
    for garbo_line in garbo_text:
        return garbo_line.encode(sys.stdout.encoding, errors='ignore').decode(sys.stdout.encoding)



with open(".token") as file:    
    token_wing_user = file.readline()
    token_wing_secret = file.readline()

word_set=set()

dis_client.run(token_wing_user, token_wing_secret)