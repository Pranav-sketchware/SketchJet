import os
import sys
import time
import json
import math
import random
import socket
import discord
import asyncio
import datetime
from time import sleep
from discord import member
from threading import Thread
from discord.ext import commands
from flask import Flask, render_template, redirect
from discord.ext.commands import cooldown, BucketType, MissingPermissions





client = commands.Bot(command_prefix='.')





def updateWallet(var):
  with open('wallet.json', 'w') as f:
    json.dump(var, f)






#making a web server



app = Flask('')

@app.route('/')
def index():
	return 'Bot is online!'

def run():
	app.run(host="0.0.0.0", port=8080)

def webserver():
	server = Thread(target=run)
	server.start()

webserver()






#get host name


def get_Host_name_IP(): 

    try: 

        host_name = socket.gethostname() 

        host_ip = of
        print("Hostname :  ",host_name) 

        print("IP : ", host_ip) 

    except: 

        print("Unable to get Hostname and IP") 

#function end


@client.event
async def on_ready():
	print('Bot Ready')
	get_Host_name_IP()


  





#restart


def restart():
	os.system('cls' if os.name == 'nt' else 'clear')
	python = sys.executable
	os.execl(python, python, *sys.argv)


@client.command()
async def mute(ctx, member: discord.Member):
	role_members = discord.utils.get(ctx.guild.roles, name='Members')
	role_muted = discord.utils.get(ctx.guild.roles, name='Members')
	await member.add_roles(role_muted)
	await context.send("User Was Muted")


#spam


@client.command()
async def stop(ctx):
	restart()



@client.command()
@commands.has_role('spammer')
async def spam(ctx, msg, amt):
  cnt = 0
  tf = True
  while tf:
    cnt += 1
    time.sleep(1)
    await ctx.send(msg.replace('&', " "))
    if cnt == int(amt):
      tf = False



@spam.error
async def spam_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		await ctx.send(
		    "Sorry, but you don't have `spammer` role, which is necessary to avoid unwanted spams :pensive:!"
		)


#general
@client.command()
async def hi(ctx):
	await ctx.send(f"hi")


@client.command(aliases=[])
async def bye(ctx):
	await ctx.send('Byeeee ' + ctx.author.mention)


@client.command(aliases=[])
async def superdie(ctx):
	await ctx.send('Lem`me book a home for you in hell')


@client.command(aliases=[])
async def supermegladondie(ctx):
	await ctx.send('An ancient salt water beast named `Megladon` ate ' +
	               ctx.author.mention)


@client.command(aliases=[])
async def s(ctx):
	await ctx.send(
	    'This command does not exist. Use .<command name> instead. Forgot/Don`t know the commands? Type `.help` to get a list of available commands'
	)


client.remove_command("help")


@client.command(aliases=['h'])
async def help(ctx):
	embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
	embedVar.add_field(name="Field1", value="Subtitle 1", inline=False)
	embedVar.add_field(name="Field2", value="Subtitle 2", inline=False)
	await ctx.send(embed=embedVar)


@client.command(aliases=['purge', 'clr'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
	await ctx.channel.purge(limit=int(amount) + 1)

@clear.error
async def spam_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(
		    "Sorry, but you don't have `Manage_Messages` Permission, which is necessary to avoid unwanted purges :pensive:!"
		)


@client.command()
async def ping(ctx):
	random_number = random.randint(0, 16777215)
	hex_number = format(random_number, 'x')
	hex_number = '#' + hex_number
	message = await ctx.send("Ping Pong🏓")
	before = time.monotonic()
	ping = (time.monotonic() - before * 1000)
	embed = discord.Embed(title="Ping Pong is",
	                      description=f"`{int(ping)} ms`",
	                      color=0x00ff00)
	await message.edit(embed=embed)


Token = os.getenv('TOKEN')
client.run(Token)
