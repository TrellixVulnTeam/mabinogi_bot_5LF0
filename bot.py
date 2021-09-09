import json
import alarms
import enchants
from dotenv import load_dotenv
from discord.ext import commands
import discord
from bs4 import BeautifulSoup
import os
import random
enchant_search = enchants.EnchantSearcher()


load_dotenv()
client = commands.Bot(command_prefix='*', intents=discord.Intents.all())
TOKEN = os.getenv('TOKEN')


@client.event
async def on_ready():
    print("Nerevarius' Assistant is ready to help.")


@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Nerevarius Assistant Bot",
                          description="Commands:")
    embed.add_field(name="Search Enchant on Mabi Wiki", value="*enchant")
    embed.add_field(name="Creates a message to react for role",
                    value="*reactrole [emoji] [@rolename] message")
    embed.add_field(name="Puppet", value="*puppet")
    embed.add_field(name="Puppet Confused", value=" *pupconfused")
    embed.add_field(name="Sov", value="*sovery")
    embed.add_field(name="Sov Boosted", value="*soveryboosted")
    embed.add_field(name="Roro", value="*roro")
    embed.add_field(name="Boots", value="*boots")
    embed.add_field(name="Pie", value="*pie")
    embed.add_field(name="Angelabb", value="*angelabb")
    embed.add_field(name="Root", value="*root")
    embed.add_field(name="Dogens", value="*dogens")
    embed.add_field(name="Gamble", value="*gamble")
    embed.add_field(name="Tymiat", value="*tymi")
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
async def puppet(ctx):
    await ctx.channel.send("Puppetoo is my Master, Lord, and Savior.")

@client.command()
async def pupconfused(ctx):
    pupconfused = ["https://media2.giphy.com/media/1X7lCRp8iE0yrdZvwd/giphy.gif","https://media.tenor.com/images/5840bd903ee40a5f6efff728837036d5/tenor.gif"]
    await ctx.channel.send(random.choice(pupconfused))


@client.command()
async def sovery(ctx):
    sovery = ["https://tenor.com/XWLX.gif", "https://media2.giphy.com/media/1uPiL9Amv5zkk/giphy.gif?cid=82a1493bpmqpb1clmqtwxaim0ntt4rhf3i15va7z9de4u0rj&rid=giphy.gif&ct=g", "https://tenor.com/oVKZ.gif"]
    await ctx.channel.send(random.choice(sovery))


@client.command()
async def soveryboosted(ctx):
    boosted = ["https://tenor.com/6JtP.gif", "https://gph.is/g/aNnvKqo", "https://tenor.com/bnwng.gif"]
    await ctx.channel.send(random.choice(boosted))


@client.command()
async def roro(ctx):
    roro = ["https://media1.tenor.com/images/8a5375e5beeeb497ac67c61ad648c990/tenor.gif?itemid=12911682","https://tenor.com/bbAHQ.gif"]
    await ctx.channel.send(random.choice(roro))


@client.command()
async def boots(ctx):
    boots = ["https://gfycat.com/fluidbothkatydid"]
    await ctx.channel.send(random.choice(boots))


@client.command()
async def pie(ctx):
    pies = ["https://c.tenor.com/A39Xp0MakpwAAAAC/cutie-pie-kitten.gif", "https://tenor.com/zmHF.gif", "https://tenor.com/bdVoh.gif", "https://tenor.com/bleVO.gif", "https://tenor.com/649f.gif"]
    await ctx.channel.send(random.choice(pies))


@client.command()
async def angelabb(ctx):
    rich = ["https://tenor.com/1h4u.gif","https://c.tenor.com/nSAZJPpakoAAAAAC/p-diddy-money.gif"]
    await ctx.channel.send(random.choice(rich))

@client.command()
async def root(ctx):
    root = ["https://tenor.com/view/spongebob-squarepants-patrick-star-im-rooting-for-you-cheer-cheering-gif-5104276","https://c.tenor.com/MFE6UiMEpRoAAAAC/math-zack-galifianakis.gif"]
    await ctx.channel.send(random.choice(root))

@client.command()
async def dogens(ctx):
    dogens = ["https://gfycat.com/cleverfeminineemeraldtreeskink"]
    await ctx.channel.send(random.choice(dogens))
    
@client.command()
async def gamble(ctx):
    gamble = ["https://tenor.com/view/lets-do-it-daniel-craig-heidi-gardner-saturday-night-live-lets-go-gif-16611656","https://tenor.com/view/bet-push-press-bets-betting-gif-17073187","https://tenor.com/view/bet-donewiththis-buttom-gif-14635640", "https://c.tenor.com/xIEnL_BZP6gAAAAM/bet-casino.gif"]
    await ctx.channel.send(random.choice(gamble))
    
@client.command()
async def tymi(ctx):
    tymi = ["https://media0.giphy.com/media/101DNxoBTatF16/giphy.gif", "https://i.pinimg.com/originals/de/8b/0c/de8b0c92f3ea0101fea07e8759aa8980.gif","https://media0.giphy.com/media/1k0Y1V6iVwmSNScu65/giphy.gif"]
    await ctx.channel.send(random.choice(tymi))

    
client.run(TOKEN)
