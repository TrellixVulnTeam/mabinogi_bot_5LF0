import json
import alarms
import enchants
from dotenv import load_dotenv
from discord.ext import commands
import discord
from bs4 import BeautifulSoup
import os
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
        name="_enchant Enchant Name", value="Search Mabi Wiki for Enchant")
    embed.add_field(name="_reactrole emoji @rolename message",
                    value="Set Roles for Reactions")
    embed.add_field(name="_puppetoo", value="Puppetoo")
    embed.add_field(name="_puppethuh", value=" Confused Puppetoo")
    embed.add_field(name="_sovery", value="Banana")
    embed.add_field(name="_soveryboosted", value="Bigger Banana")
    embed.add_field(name="_roro", value="WHO")
    embed.add_field(name="_boots", value="My Nigga")
    embed.add_field(name="_pie", value="Slap")
    embed.add_field(name="_angelabb", value="Money")
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
    await ctx.channel.send("https://c.tenor.com/jo-G7N8cOZgAAAAM/cutie-guess-what.gif")


@client.command()
async def angelabb(ctx):
    await ctx.channel.send("https://c.tenor.com/nSAZJPpakoAAAAAC/p-diddy-money.gif")


client.run(TOKEN)
