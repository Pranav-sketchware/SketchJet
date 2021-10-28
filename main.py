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
	executable = sys.executable
	os.execl(executable, executable, *sys.argv)


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


#Economy


@client.command(aliases=['bal'])
async def balance(ctx, user=''):
	with open('wallet.json') as f:
		wallet = json.load(f)
	with open('bank.json') as f:
		bank = json.load(f)
	user = str(ctx.author)
	if user in wallet and user in bank:
	  em = discord.Embed(title=str(ctx.author.name) + "'s balance")
	  em.add_field(name='Wallet', value="{:,}".format(int(wallet[user])))
	  em.add_field(name='Bank', value="{:,}".format(int(bank[user])))
	  await ctx.send(embed=em)
	else:
		await ctx.send("Your balance is not stored. Start one by typing [.new]")


@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def beg(ctx):

	with open('wallet.json') as f:
		wallet = json.load(f)
	user = str(ctx.author)
	begged = random.randrange(0, 900)
	newbal = int(wallet[user]) + int(begged)
	wallet[user] = newbal
	msg = f"Someone gave you {'{:,}'.format(begged)} coins"
	choice = str(msg)
	if "I would pay my taxes rather than giving you anything." not in msg:
	  updateWallet(wallet);
	  em = discord.Embed(title=choice, description=f'Your new wallet balance is {newbal}')
	  await ctx.send(embed=em)
	else:
		em = discord.Embed(title=choice, description='You got nothing')
		await ctx.send(embed=em)


@client.command(aliases=['dep'])
async def deposit(ctx, amount):
	with open("wallet.json") as f:
		wallet = json.load(f)
	with open("bank.json") as f:
		bank = json.load(f)
	user = str(ctx.author)
	if amount == 'max' or 'all':
		bank[user] = bank[user] + wallet[user]
		with open('bank.json', 'w') as jso:
			json.dump(bank, jso)
		await ctx.send(f'Deposited {wallet[user]} to bank. \n Current bank balance is {bank[user]} coins')
		wallet[user] = 0
		updateWallet(wallet)
	else:
		if int(amount) > wallet[user]:
			await ctx.send("Hey Idiot, you cannot deposit more than ∆" +
			               f"{'{:,}'.format(wallet[user])} from your wallet")
		else:
			bank[user] = bank[user] + int(amount)
			wallet[user] = wallet[user] - int(amount)
			await ctx.send(f"Successfully deposited {'{:,}'.format(amount)} to bank")
			with open('bank.json', 'w') as jso:
				json.dump(bank, jso)
			updateWallet(wallet)


@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
	with open("wallet.json") as f:
		wallet = json.load(f)
	with open("bank.json") as f:
		bank = json.load(f)
	user = str(ctx.author)
	daily = [5000, 7500, 10000, 12500]
	choice = int(random.choice(daily))
	wallet[user] = wallet[user] + choice
	await ctx.send(f"You recieved {'{:,}'.format(choice)} from daily command")

	updateWallet(wallet)


@client.command(aliases=[('wd')])
async def withdraw(ctx, amt):
	user = str(ctx.author)
	with open('wallet.json') as f:
		wallet = json.load(f)
	with open('bank.json') as f:
		bank = json.load(f)
	if int(amt) == None:
		await ctx.send("You didn't provide the value to withdraw")
	else:
		wallet[user] = wallet[user] + int(amt)
		bank[user] = bank[user] - int(amt)
		updateWallet(wallet)
		with open('bank.json', 'w') as jso:
			json.dump(bank, jso)
			await ctx.send('Withdrew {"{:,}".format(amt)}')


@client.command()
async def bet(ctx, amt=''):
	user = str(ctx.author)
	with open('wallet.json') as f:
	  wallet = json.load(f)
	  choice = random.choice(['yes', 'no'])
	if amt == 'max' or amt == 'all':
	    resultCoins = int(wallet[user])/2
	    if choice == 'yes':
	      wallet[user] = wallet[user] + resultCoins
	      await ctx.send(f"You won {'{:,}'.format(int(resultCoins))} coins :seizure:")
	    else:
	      wallet[user] = int(wallet[user]) - int(resultCoins)
	      await ctx.send(f"You lost {'{:,}'.format(int(resultCoins))} coins :pensive:")
	else:
	  resultCoins = int(amt)/2
	  try:
	    if float(amt).is_integer:
	      if choice == 'yes':
	        wallet[user] = int(wallet[user]) + int(resultCoins)
	        await ctx.send(f"You won {'{:,}'.format(int(resultCoins))} coins :seizure:")
	      else:
	        wallet[user] = int((wallet[user]) - (resultCoins))
	        await ctx.send(f"You lost {'{:,}'.format(int(resultCoins))} :pensive:")
	  except:
	      await ctx.send(f"{ctx.author} You have to give a valid amount of coins to bet")
	updateWallet(wallet)



############NEW##########


@client.command(aliases=[('make')])
async def new(ctx):
	user = str(ctx.author)
	with open('wallet.json') as f:
		wallet = json.load(f)
	with open('bank.json') as f:
		bank = json.load(f)
	if user in wallet and bank:
		await ctx.send('You already have an account, stupid.')
	else:
		wallet[user] = 250
		bank[user] = 500
		updateWallet(wallet)
		with open('bank.json', 'w') as jso:
			json.dump(bank, jso)
		await ctx.send("Created your account")

Token = os.getenv('TOKEN')
client.run(Token)
