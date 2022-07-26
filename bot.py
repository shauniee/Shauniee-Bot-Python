from http import client
import os
import random
from venv import create

import json

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

load_dotenv()

var_dict = json.load(open('variable.json'))
TOKEN = var_dict['TOKEN']

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix = '/', intents = intents)

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member}, welcome to Shauns discord channel <3'
    )

@bot.event
async def on_message(message):
    if message.author == client.user:
        await bot.process_commands(message)
    if message.content.startswith("Shauniee"):
        response = chatbot.request(message.content[7:])
        print(response)
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command(name = 'ay')
async def call_aoyu(ctx):
    call_ay = ("<@260750015109005312>  hi uw play!!!"),

    response = random.choice(call_ay)
    await ctx.send(response)

@bot.command(name = 'val')
async def play_val(ctx):
    val_everyone = ("@everyone hi want val?"),

    response = random.choice(val_everyone)
    await ctx.send(response)

@bot.command(name = 'twitch')
async def show_twitch(ctx):
    twitch_url = ("https://www.twitch.tv/shaunnieee"),

    response = random.choice(twitch_url)
    await ctx.send(response)

@bot.command(name = 'linkedin')
async def show_linkedin(ctx):
    linkedin_url = ("https://sg.linkedin.com/in/shaun-hoon"),

    response = random.choice(linkedin_url)
    await ctx.send(response)

@bot.command(name = 'github')
async def show_git(ctx):
    git_url = ("https://github.com/shauniee"),

    response = random.choice(git_url)
    await ctx.send(response)

bot.run(TOKEN)