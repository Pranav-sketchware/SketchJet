import discord
from discord.ext import commands
import os
import time
import random
import asyncio
import json
import os
if os.path.isdir('bank.json'):
  os.chdir('bank.json') 
client = commands.Bot(command_prefix = '.') 
@client.event
async def on_ready():
  print('Bot Ready')
  
@client.command()
async def hi(ctx):
  await ctx.send(f"hi")
  
@client.command(aliases=[])
async def bye(ctx):
  await ctx.send('Byeeeee {0.author.mention}')
@client.command(aliases=[])
async def superdie(ctx):
  await ctx.send('Lem`me book a home for you in hell')
@client.command(aliases=[]) 
async def supermegladondie(ctx):
  await ctx.send('An ancient salt water beast named `Megladon` ate {0.author.mention}')
@client.command(aliases=[])
async def s(ctx):
  await ctx.send('This command does not exist. Use .<command name> instead. Forgot/Don`t know the commands? Type .help to get a list of available commands')
client.remove_command("help")
@client.command(aliases=['h'])
async def help(ctx):
  embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
  embedVar.add_field(name="Field1", value="Subtitle 1", inline=False)
  embedVar.add_field(name="Field2", value="Subtitle 2", inline=False)
  await ctx.send(embed=embedVar)
@client.command(aliases=['clr'])
async def clear(ctx, amount):
  await ctx.channel.purge(limit=int(amount)) 
@client.command()
async def ping(ctx):
    random_number = random.randint(0,16777215)
    hex_number =format(random_number,'x')
    hex_number = '#'+hex_number
    message = await ctx.send("Ping Pong🏓")
    before = time.monotonic()
    ping = (time.monotonic() - before * 1000) 
    embed = discord.Embed(title="Ping Pong is", description=f"`{int(ping)} ms`", color=0x00ff00)
    await message.edit(embed=embed)
@client.command(aliases=['bal'])
async def balance(ctx):
  user = ctx.author.id

  wallet = (user) ["wallet"]
  bank = (user)["bank"]
await ctx.send('pls beg') 
client.run('ODA4NTg1NDQ5ODQ4NDM4ODE1.YCIr4g.fCFbliEijAdJRPyJzIhKfrK11_E')
