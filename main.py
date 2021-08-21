import os
import discord
from Data import Data
from Decider import Decider
from Reply import Reply
from keep_alive import keep_alive
intents = discord.Intents.default()
intents.members = True


 # Somewhere else:
 # 
 # or
 # from discord.ext import commands
 # bot = commands.Bot(command_prefix='!', intents=intents)

my_secret = os.environ['TOKEN']

dmonk=os.environ['DMONK']

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('ready')

@client.event
async def on_message(message):
    decider=Decider(message,client)
    if not decider.for_me():
      return
    requirements=decider.requirements()

    if message.reference:
      print("mension=",message.reference,"\nmessage=",message.reference.message_id)
      refid=message.reference.message_id
      m1=await message.channel.fetch_message(refid)
      author=m1.author.name
      if m1.author == client.user:
        return 
      to=[author]

      #print(m1.author.name,message.mentions)

      # await m1.reply(f'Hello! {author} ,{type(author)}<@{m1.author.id}>', mention_author=False)
      

    else:
      to=decider.to()

    data_obj=Data(requirements)
    data=data_obj.data()
    reply=Reply(data,to)
    send=reply.reply()
    
    await message.channel.send(send)



keep_alive()
client.run(dmonk)
