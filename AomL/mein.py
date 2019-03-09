import discord, asyncio, sys

dis_client = discord.Client()
mein_out_file = '.output'
word_set=set()

@dis_client.event
async def on_ready():
    print('Logged in as')
    print(dis_client.user.name)
    print(dis_client.user.id)
    print('------')

@dis_client.event
async def on_message(message):
    
    await printNotgarbo(message.author.name, ': ')
    await printNotgarbo(message.content)

    for i in message.content.split():
        word_set.add(await notGarbo(i))
        # print('the set is %s long' % len(word_set))

    if len( word_set ) > 500:
        with open(mein_out_file,'a') as output_file:
            output_file.write(await notGarbo(' '.join(word_set).lower()))
            output_file.write('\n')
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

async def notGarbo(garbo_text):
    try:
        potentially_garbp = garbo_text.encode(sys.stdout.encoding, errors='ignore').decode(sys.stdout.encoding, errors='ignore')
    except OSError:
        potentially_garbp = 'a'

    return potentially_garbp

async def printNotgarbo(garbo_text, garbo_end= '\n'):
    ungarbo = await notGarbo(garbo_text)
    print(ungarbo, end= garbo_end)

def main():


    with open(".token") as file:    
        token_wing_user = file.readline()
        token_wing_secret = file.readline()


    dis_client.run(token_wing_user, token_wing_secret)

main()