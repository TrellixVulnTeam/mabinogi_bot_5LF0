import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import enchants
enchant_search = enchants.EnchantSearcher()

load_dotenv()
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)
TOKEN = os.getenv('TOKEN')
@client.event
async def on_ready():
    print("Nerevarius' Assistant is ready to help.")

@client.command()
async def goodbye(ctx):
    await ctx.send("Bye")



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message_content = message.content
    if '.enchant' in message_content:
        if enchant_search.base_case(message_content):
            enchant = enchant_search.base_case(message_content)
            await message.channel.send(f"```{enchant}```")
        else:
            keyword = enchants.keyword_strip(message_content)
            enchant = enchant_search.searcher(keyword)
            if len(enchant) < 10:
                for items in enchant:
                    url = 'https://wiki.mabinogiworld.com'+items
                    if enchants.spoon(url):
                        enchants_info = enchants.spoon(url)
                        await message.channel.send(f"```{enchants_info}```")
                    else:
                        pass
            else:
                await message.channel.send(f"```{enchant}```")



    commands = ['.enchants', 'i like this bot', '.puppet','.pupconfused','.sov','.pie', '.roro', '777', '.angelabb']
    if ".commands" == message_content:
        await message.channel.send(f"``` {commands}```")
    if "i like this bot" == message_content or 'I like this bot' == message_content:
        await message.channel.send(f"OMO, i like you too {message.author.display_name}")
        await message.channel.send("https://media1.tenor.com/images/e969779fd9cb007be9308c163d7188ce/tenor.gif?itemid=19753550")
    if '.puppet' in message_content:
        await message.channel.send("Puppetoo is my Master, Lord, and Savior.")
    if '.pupconfused' in message_content or 'imconfusedpup' in message_content:
        await message.channel.send("https://media.tenor.com/images/5840bd903ee40a5f6efff728837036d5/tenor.gif")

    if '.soverykorean' == message_content or '.sov' == message_content:
        await message.channel.send("https://media2.giphy.com/media/1uPiL9Amv5zkk/giphy.gif?cid=82a1493bpmqpb1clmqtwxaim0ntt4rhf3i15va7z9de4u0rj&rid=giphy.gif&ct=g")
    
    if '.soveryboosted' in message_content or '.sovboosted' in message_content:
        await message.channel.send("https://gph.is/g/aNnvKqo") 

    if '.pie' in message_content:
        await message.channel.send("https://media1.giphy.com/media/YMLWuqqiNdY9YkpKIq/giphy.gif" or "https://gfycat.com/ripescentedindochinesetiger")

    if '.roro' in message_content or 'ryoung' in message_content:
        await message.channel.send("https://media1.tenor.com/images/8a5375e5beeeb497ac67c61ad648c990/tenor.gif?itemid=12911682")
    if '.gamble' in message_content or '777' in message_content:
        await message.channel.send("https://media.tenor.com/images/01f2fce15461365c59981176ece3791d/tenor.gif")
    if '.angelabb' in message_content:
        await message.channel.send("https://media0.giphy.com/media/Qv5TjYPMeesh3ALM4N/giphy.gif")
client.run(TOKEN)