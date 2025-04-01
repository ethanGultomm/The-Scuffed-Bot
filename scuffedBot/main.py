import discord
import xlwings as xw

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

## load osmond's dogshit stats
osmondStat = xw.Book("osmonds stats.xlsx").sheets['Sheet1']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print ('message received= {}'.format(message.content))  ## prints out the messages if its not from the bot

    if message.content.startswith('scuffed!'):
        

    if message.content.startswith(']xiangling'):
        print('sending reply')
        await message.channel.send('I can\'t take it anymore. I\'m sick of Xiangling. I try to play Diluc. My Xiangling deals more damage. I try to play Yoimiya. My Xiangling deals more damage. I try to play Cyno. My Xiangling deals more damage. I want to play Klee. Her best team has Xiangling. I want to play Raiden, Childe - they both want Xiangling. She grabs me by the throat. I fish for her. I cook for her. I give her the Catch. She isn\'t satisfied. I pull Engulfing Lightning. "I don\'t need this much er" She tells me. "Give me more field time." She grabs Bennett and forces him to throw himself off enemies. "You just need to funnel me more. I can deal more damage with Homa." I can\'t pull for Homa, I don\'t have enough primogems. She grabs my credit card. It declines. "Guess this is the end." She grabs Gouba. She says "Gouba, get them." There is no hint of sadness in his eyes. Nothing but pure, no icd pyro application. What a cruel world.')

    if message.content.startswith(']osmond'):
        print('sending osmond\'s dumbass stats')
        hitRate = osmondStat.range("K29").value
        print('sending osmond\'s dumbass stats')
        await message.channel.send('Osmond\'s raze ult currently hits around {} of the time, it is dogshit'.format(hitRate))

client.run() # Fill these with tokens bruh