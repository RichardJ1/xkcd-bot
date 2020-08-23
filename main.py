# imports the discord python library along with the random library
import discord
from discord.ext import commands
import random
from threading import Thread
from flask import Flask
from xkcd import *


 
# a prefix to all the commands for this bot (ex: /help, /hello, /cool)
bot = commands.Bot(command_prefix = '/', case_insensitive = True)
 
# removes the preset help command that comes with the discord library
bot.remove_command('help')
 
app = Flask('')
@app.route('/')
 
def home():
    return f'================================================================================= <br>Discord Bot Name: {bot.user.name} <br>Hosting Platform: Repl.it <br>Bot Developer: lil ricky#5937<br>================================================================================='
 
def run():
  app.run(host = '0.0.0.0', port = 8080)
 
def keepAlive():
    t = Thread(target=run)
    t.start()

# bot on initialization
@bot.event
async def on_ready():
 
    # prints the initialization message on the right-hand side (console)
    print(f'================================================================================= \nDiscord Bot Name: {bot.user.name} \nHosting Platform: Repl.it \nBot Developer: lil ricky#5937 \n================================================================================= \n\nBOT CONSOLE LOG BELOW: \n')
 
    # changes the discord status of the bot to 'Playing with Repl.i'
    await bot.change_presence(activity=discord.Game(name='with Repl.it [/help]'))
 
# responds to /hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello There!')
    print('HELLO Command Called')
 
# responds to /ping
@bot.command(aliases=['latency'])
async def ping(ctx):
    await ctx.send(f':ping_pong:  Pong! The latency is {round(bot.latency * 1000)} MS')
    print('PING Command Called')


#xkcd related commands

latest = getLatestComicNum()
#responds to /xkcd
@bot.command()
async def xkcd(ctx, *, query=None):
  com = None
  rand = None
  #return comics
  if not query:
    com = Comic(latest)

  elif query.isdigit():
    try:
      com = Comic(query)
    except:
      await ctx.send(f'I couldn\'t find that. Make sure you give a number between 1 and {latest}')

  elif query.lower().startswith('r'):
    rand = random.randint(1, latest)
    com = Comic(rand)

  else:
    await ctx.send('I don\'t understand. Type "/help" for a list of commands.')


  if com:
    await ctx.send(f'Number: {rand if rand else query if query else latest} \nTitle: {com.getTitle()} \nAlt Text: {com.getAltText()}')
    await ctx.send(com.getImageLink())

  print('XKCD Command Called')



# responds to /link
@bot.command(aliases=['url'])
async def link(ctx, *, query=None):

  #return links
  if not query:
    await ctx.send(f'Here is the link to the latest comic, {latest} - "{Comic(latest).getTitle()}". \nhttps://www.xkcd.com/{latest}')

  elif query.isdigit():
    try:
      await ctx.send(f'Here is the link to {query} - "{Comic(query).getTitle()}" \nhttps://www.xkcd.com/{query}')
    except:
      await ctx.send(f'I couldn\'t find that. Make sure you give a number between 1 and {latest}')

  elif query.lower().startswith('r'):
    rand = random.randint(1, latest)
    await ctx.send(f'Here is the link to a random comic, {rand} - "{Comic(rand).getTitle()}" \nhttps://www.xkcd.com/{rand}')


  else:
    await ctx.send('I don\'t understand. Type "/help" for a list of commands.')

  print('LINK Command Called')



  # responds to /explain
@bot.command(aliases=['explainxkcd'])
async def explain(ctx, *, query=None):

  if not query:
      await ctx.send(f'Here is the explaination for the latest comic, {latest} - "{Comic(latest).getTitle()}" \n{Comic(latest).getExplanation()}')

  elif query.isdigit():
    try:
      await ctx.send(f'Here is the explaination for {query} - "{Comic(query).getTitle()}" \n{Comic(query).getExplanation()}')
    except:
      await ctx.send(f'I couldn\'t find that. Make sure you give a number between 1 and {latest}')

  elif query.lower().startswith('r'):
    rand = random.randint(1, latest)
    await ctx.send(f'Here is the explanation for a random comic, {rand} - "{Comic(rand).getTitle()}" \n{Comic(rand).getExplanation()}')


  else:
    await ctx.send('I don\'t understand. Type "/help" for a list of commands.')

  print('EXPLAIN Command Called')


  # responds to /whatif
@bot.command(aliases=['WhatIf?'])
async def whatif(ctx, *, query=None):
  latest = getLatestWhatIfNum()

  if not query:
    await ctx.send(f'Here is the latest What If? post, {latest} - "{getWhatIf(latest).getTitle()}" \n{getWhatIf(latest).getLink()}')

  elif query.isdigit():
    try:
      await ctx.send(f'Here is What If? #{query} - "{getWhatIf(query).getTitle()}" \n{getWhatIf(query).getLink()}')
    except:
      await ctx.send(f'I couldn\'t find that. Make sure you give a number between 1 and {latest}')

  elif query.lower().startswith('r'):
    rand = random.randint(1, latest)
    await ctx.send(f'Here is a random What If? article, {rand} - "{getWhatIf(rand).getTitle()}" \n{getWhatIf(rand).getLink()}')


  else:
    await ctx.send('I don\'t understand. Type "/help" for a list of commands.')

  print('WHAT IF Command Called')

# responds to /help
@bot.command()
async def help(ctx):
    
# Currently undergoing rewrite

    await ctx.send(embed=embed)
    print('HELP Command Called')

keepAlive()
infile = open('bot_token.txt', 'r')
TOKEN = infile.readline()
 
bot.run(TOKEN)
