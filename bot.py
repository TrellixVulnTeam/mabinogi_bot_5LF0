import json
import alarms
import enchants
from dotenv import load_dotenv
from discord.ext import commands
import discord
from bs4 import BeautifulSoup
import os
<< << << < HEAD
enchant_search = enchants.EnchantSearcher()


load_dotenv()
client = commands.Bot(command_prefix='_', intents=discord.Intents.all())
TOKEN = os.getenv('TOKEN')


@client.event
async def on_ready():
    print("Nerevarius' Assistant is ready to help.")


@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Nerevarius Assistant Bot",
                          description="Commands:")
    embed.add_field(
        name="-enchant Enchant Name", value="Search Mabi Wiki for Enchant")
    embed.add_field(name="-reactrole emoji @rolename message",
                    value="Set Roles for Reactions")
    embed.add_field(name="-puppetoo", value="Puppetoo")
    embed.add_field(name="-puppetoo", value=" Confused Puppetoo")
    embed.add_field(name="-sovery", value="Banana")
    embed.add_field(name="-soveryboosted", value="Bigger Banana")
    embed.add_field(name="-roro", value="WHO")
    embed.add_field(name="-boots", value="My Nigga")
    embed.add_field(name="-pie", value="Slap")
    embed.add_field(name="-angelabb", value="Money")
    await ctx.channel.send(content=None, embed=embed)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Enchant Searching Feature


@client.command()
async def enchant(ctx, *message):

    enchant_key = ""
    enchant_key = " ".join(message)
    if enchant_search.base_case(enchant_key):
        enchant = enchant_search.base_case(enchant_key)
        enchant_emb = discord.Embed(description=enchant)
        await ctx.channel.send(embed=enchant_emb)
    else:
        keyword = enchant_key
        enchant = enchant_search.searcher(keyword)
        if len(enchant) < 10:
            urls = []
            for items in enchant:
                url = 'https://wiki.mabinogiworld.com'+items
                if enchants.spoon(url):
                    enchants_info = enchants.spoon(url)
                    enchant_emb = discord.Embed(description=enchants_info)
                    await ctx.channel.send(embed=enchant_emb)
                else:
                    pass
        else:
            enchant_emb = discord.Embed(description=enchant)
            await ctx.channel.send(embed=enchant_emb)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alarm

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# React to Roles


@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass
    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name:
                    role = discord.utils.get(client.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name:
                role = discord.utils.get(client.get_guild(
                    payload.guild_id).roles, id=x['role_id'])

                await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


@client.command()
async def reactrole(ctx, emoji, role: discord.Role, *, message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {'role_name': role.name,
                          'role_id': role.id,
                          'emoji': emoji,
                          'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Friends


@client.command()
async def puppetoo(ctx):
    await ctx.channel.send("Puppetoo is my Master, Lord, and Savior.")


async def puppethuh(ctx):
    await ctx.channel.send("https://media.tenor.com/images/5840bd903ee40a5f6efff728837036d5/tenor.gif")


@client.command()
async def sovery(ctx):
    await ctx.channel.send("https://media2.giphy.com/media/1uPiL9Amv5zkk/giphy.gif?cid=82a1493bpmqpb1clmqtwxaim0ntt4rhf3i15va7z9de4u0rj&rid=giphy.gif&ct=g")


@client.command()
async def soveryboosted(ctx):
    await ctx.channel.send("https://gph.is/g/aNnvKqo")


@client.command()
async def roro(ctx):
    await ctx.channel.send("https://media1.tenor.com/images/8a5375e5beeeb497ac67c61ad648c990/tenor.gif?itemid=12911682")


@client.command()
async def boots(ctx):
    await ctx.channel.send("https://gfycat.com/fluidbothkatydid")


@client.command()
async def pie(ctx):
    await ctx.channel.send("https://media3.giphy.com/media/ZEkZXknM3STeDyk0u1/giphy.gif")


@client.command()
async def angelabb(ctx):
    await ctx.channel.send("https://c.tenor.com/nSAZJPpakoAAAAAC/p-diddy-money.gif")


client.run(TOKEN)
== == == =
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

    commands = ['.enchants', 'i like this bot', '.puppet',
                '.pupconfused', '.sov', '.pie', '.roro', '777', '.angelabb']
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

    if '.boots' == message_content or '.boot' == message_content:
        await message.channel.send("https://gfycat.com/fluidbothkatydid")
client.run(TOKEN)
>>>>>> > dcfa04fcbcedef58a48ea18f083cf8e41225f2c8
