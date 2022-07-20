import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# TOKEN = ('Add your bot token here')

bot = commands.Bot(command_prefix = '/')

@bot.command(name = 'aoyu')
async def call_aoyu(ctx):
    call_ay = ("@tzuyu#9733 hi"),

    response = random.choice(call_ay)
    await ctx.send(response)

@bot.command(name = 'val')
async def play_val(ctx):
    val = ("@everyone hi want val?"),

    response = random.choice(val)
    await ctx.send(response)

@bot.command(name = 'twitch')
async def show_twitch(ctx):
    twitch = ("https://www.twitch.tv/shaunnieee"),

    response = random.choice(twitch)
    await ctx.send(response)

@bot.command(name = 'linkedin')
async def show_linkedin(ctx):
    linkedin = ("https://sg.linkedin.com/in/shaun-hoon"),

    response = random.choice(linkedin)
    await ctx.send(response)

@bot.command(name = 'github')
async def show_git(ctx):
    git = ("https://github.com/shauniee"),

    response = random.choice(git)
    await ctx.send(response)

bot.run(TOKEN)
