# -*- coding: utf-8 -*-

import discord
from discord.ext import voice_recv

discord.opus._load_default()

bot = discord.Client(intents=discord.Intents.all())

vc: voice_recv.VoiceRecvClient


def callback(user, data: voice_recv.VoiceData):
    print(f"Got packet from {user}")

@bot.event
async def on_ready():
    print('Logged in as {0.id}/{0}'.format(bot.user))
    print('------')
    print('Set up your own trigger/event to connect and call vc.listen(...)')
    print('Example:')
    print('vc = await some_voice_channel.connect(cls=voice_recv.VoiceRecvClient)')
    print('vc.listen(voice_recv.BasicSink(callback))')

bot.run("token")
