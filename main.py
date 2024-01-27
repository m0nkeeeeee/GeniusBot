import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bad_words = [
  "fuck", "ass", "bitch", "cunt", "pussy"
  "dick", "piss", "bastard ", "asshole", "shit", "stfu"
]
sad_words = [
  "sad", "depressed", "unhappy", "angry", "miserable", ":(", "sadge", "sucks"
]
badword_remedy = [
  "sir that is not a nice thing to say ",
  "you just said a bad word , that is cringe bro",
  "you are being very elvis rn using words like that ",
  "mam he is saying a bad word", "LANGUAGE BUDDY",
  "dei bad words pesaadu da please da", "YOU CAN BE KINDER OKAY",
  "can't hear you say bad words from the bottom of the leaderboard bro"
]
starter_encouragements = [
  "cheer up dawg", "it do be like that sometimes", "you are the goat",
  "dont be sad, sad is bad, i am down bad", "you are the goat",
  "Every day, in every way, you are getting better",
  "You are worthy of great things", "I'm here for you", "I love you",
  "everything is going to be okay"
]

image_urls_nsfw = [
  "https://api.waifu.pics/nsfw/waifu", "https://api.waifu.pics/nsfw/neko",
  "https://api.waifu.pics/nsfw/trap", "https://api.waifu.pics/nsfw/blowjob"
]

image_urls_sfw = [
  "https://api.waifu.pics/sfw/waifu", "https://api.waifu.pics/sfw/neko",
  "https://api.waifu.pics/sfw/cringe", "https://api.waifu.pics/sfw/hug",
  "https://api.waifu.pics/sfw/happy", "https://api.waifu.pics/sfw/wink",
  "https://api.waifu.pics/sfw/dance", "https://api.waifu.pics/sfw/poke",
  "https://api.waifu.pics/sfw/awoo", "https://api.waifu.pics/sfw/lick",
  "https://api.waifu.pics/sfw/pat", "https://api.waifu.pics/sfw/smug",
  "https://api.waifu.pics/sfw/bonk", "https://api.waifu.pics/sfw/yeet",
  "https://api.waifu.pics/sfw/blush", "https://api.waifu.pics/sfw/smile",
  "https://api.waifu.pics/sfw/handhold", "https://api.waifu.pics/sfw/kill",
  "https://api.waifu.pics/sfw/slap", "https://api.waifu.pics/sfw/glomp"
]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n -" + json_data[0]['a']
  return (quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send('Hello! my name gener i have small wiener')

  if msg.startswith('$help'):
    await message.channel.send(
      "Here are the working features of me aka genius bot \n\n (use $ before each command) \n\n hello: bot introduction \n\n sigma: gives you an epic sigma quote to never stop that grindset \n\n kys : NUH UH \n\n jaker: shows jaker stuff \n\n jakeroff: shows even more downbad jaker stuff \n\n plumbum: plumbum \n\n clear: clears messages (add a number after it indicating number of messages to be cleared)\n\n the bot also detects if you sad or say bad and says jokes like a dad.\n Created by monke "
    )

  if msg.startswith('$sigma'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith("$kys"):
    await message.channel.send("dont say that bro :(")

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if any(word in msg for word in bad_words):
    await message.channel.send(random.choice(badword_remedy))

  if any(word in msg for word in ["i'm", "im ", "i am"]):
    dad_joke_content = msg.split("i'm", 1)[-1].strip()
    dad_joke_content = dad_joke_content.split("im", 1)[-1].strip()
    dad_joke_content = dad_joke_content.split("i am", 1)[-1].strip()

    if dad_joke_content:
      response = f"Hello {dad_joke_content}, I'm genius."
      await message.channel.send(response)

  if message.content == '$jaker':
    response = requests.get(random.choice(image_urls_sfw))
    data = response.json()
    image = data['url'] if 'url' in data else None

    if not image:
      await message.channel.send(
        "Something went wrong, unable to get the image.")
    else:
      embed = discord.Embed(color=0xffc0cb)
      embed.set_image(url=image)
      await message.channel.send(embed=embed)

  if message.content == '$jakeroff':
    response = requests.get(random.choice(image_urls_nsfw))
    data = response.json()
    image = response.json()
    image = data['url'] if 'url' in data else None
    if not image:
      await message.channel.send("Somethig went wrong, unable to get the image"
                                 )
    else:
      embed = discord.Embed(color=0x00FFFF)
      embed.set_image(url=image)
    await message.channel.send(embed=embed)

  if message.content == '$plumbum':
    ye = 'https://i.ytimg.com/vi/lNMY1f676Fc/maxresdefault.jpg'
    embed = discord.Embed(color=0x00FFFF)
    embed.set_image(url=ye)
    await message.channel.send(embed=embed)

  msg = message.content

  if msg.startswith('$clear'):
    # Check if the user has the necessary permissions to manage messages
    if message.author.guild_permissions.manage_messages:
      # Split the message content into command and argument
      command, arg = message.content.split(' ', 1)

      # Convert the argument to an integer
      try:
        num_messages = int(arg)
      except ValueError:
        await message.channel.send(
          'Please provide a valid number of messages to delete.')
        return

      # Delete the specified number of messages
      deleted = await message.channel.purge(limit=num_messages + 1)
      await message.channel.send(
        f'Successfully deleted {len(deleted) - 1} messages.')
    else:
      await message.channel.send(
        'You do not have permission to manage messages.')

keep_alive()
client.run(os.getenv('TOKEN'))
