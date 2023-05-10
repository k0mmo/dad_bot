''' Discord Dad bot
    Developed in Unbuntu Mate, linux Mint
    Python 3.6.8
    Tested in discord private server on Linux, Windows, Adndroid platforms
    Author: k0mmo
    Last updated Sept.30.19
'''

import discord
import requests
import random
import lists

ver = ("1.02c")

ask_Mom = random.randint(1, 20) # number range for the random ask your mom response
ask_Mom_number = 12 # number that activates the Go ask your mother commands

activity = discord.Game(random.choice(lists.activities)) # changes the playing status from a list in lists.py

class MyClient(discord.Client): # connects to discord
    async def on_ready(self):
        print('######## Dad Bot 2000 is online ##########\n')
        print('Logged in to discord as ', self.user) # displays logged in as the bots name in console
        print('\n')
        print("Ver: " + ver)
        await client.change_presence(status=discord.Status.idle, activity=activity) # sets playing activy to a custom message

        async def on_message(self, message):
            if message.author == self.user: # checks to see if its the bot useing the command so it doesnt just loop its self with commands
                return


### Dad bot commands ###
    async def on_message(self, message):


        channels = ['Channels for dad bot to talk in goes here'] #channels the bot will work in



        if str(message.channel) in channels:
             
            if message.content in ["Hey dad bot if i say ping?", 'hey dad bot if i say ping?']:  # get ponged commands
                if ask_Mom == ask_Mom_number:
                    await message.channel.send("Go ask your Mother")
                else:
                    await message.channel.send('I say pong!')

            elif message.content in ['Hey dad bot insult me', 'hey dad bot insult me']: # insult command gives a random insult
                if ask_Mom == ask_Mom_number:
                    await message.channel.send("Go ask your Mother")
                else:
                    await message.channel.send('Hey {0.author.mention} '.format(message) + str(random.choice(lists.insult_list)))

            elif message.content in ['Hey dad bot tell me a joke', 'hey dad bot tell me a joke']: # /joke command pulls random joke from website
                if ask_Mom == ask_Mom_number:
                    await message.channel.send("Go ask your Mother")
                else:
                    joke = requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"}).text
                    await message.channel.send(joke)

            elif message.content in ['Hey dad bot how do i cook on the grill?', 'hey dad bot how do i cook on the grill?']: #/girllmaster command gives random grilling advice
                if ask_Mom == ask_Mom_number:
                    await message.channel.send("Go ask your Mother")
                else:
                    await message.channel.send("GRILL MASTER TIPS:\n\n" + str(random.choice(lists.grillMaster_Tips)))

            elif message.content in ['Hey dad bot tell me a fishing tip', 'hey dad bot tell me a fishing tip']: #/girllmaster command gives random grilling advice
                if ask_Mom == ask_Mom_number:
                    await message.channel.send("Go ask your Mother")
                else:
                    await message.channel.send("Fishing Tips:\n\n" + str(random.choice(lists.fishing_Tips)))

            elif message.content in ['Hey dad bot tell me a knock knock joke', 'hey dad bot tell me a knock knock joke']: # /knock command pulls a random knock knock joke from list
                if ask_Mom == ask_Mom_number:
                    await message.channel.send("Go ask your Mother")
                else:
                    await message.channel.send("Knock Knock\nWho's there\n" + str(random.choice(lists.knock_Jokes)))

            elif message.content in ['Hey dad bot tell me a sports fact', 'hey dad bot tell me a sports fact']: # /sports command gives random sports info from list
                if ask_Mom == ask_Mom_number:
                    await message.channel.send("Go ask your Mother")
                else:
                    await message.channel.send("Sports Facts:\n\n" + str(random.choice(lists.sports_facts)))

            elif message.content in ["Hi dad bot", 'hi dad bot']:# semi Interactive command says hello + random name from list
                await message.channel.send("Hey there " + str(random.choice(lists.son_Names) + "!"))

            elif message.content == "Ping me daddy!":
                await message.channel.send('{0.author.mention}'.format(message) + str(' I love it when you call me Ping Daddy!'))

            elif message.content == "I love you dad bot": # semi Interactive command looks for exact phrasing
                banned_users = [" banned names go here"]  # lists of useres command will look for
                if str(message.author) in banned_users:  # looks to see if user that is giving the command is in the users list
                    await message.channel.send(random.choice(lists.love_response)) # uses this command if user is in valid_users
                else:
                    if message.content == "I love you dad bot":
                        await message.channel.send("Oh Dad Bot loves you too " + str(random.choice(lists.son_Names) + "!")) # uses this command if use is not in valid_users
            else:
            #does the i'm dad joke (eg: im gay, hello gay im dad!)
                for pronoun in pronouns:
                    if len(message.content) > 80:
                      return
                    if message.content.lower().startswith(pronoun):
                      msg = message.content.lower().replace('im', '',1)
                      msg = msg.lower().replace("i'm",'',1)
                      msg = msg.lower().replace('i am', '',1)
                      msg = msg.lower().replace('@','')
                      await message.channel.send('Hello'+ msg + ", I'm Dad!")
                      return

####### help commands #######
            elif message.content in ['Hey dad bot show me your commands', 'hey dad bot show me your commands']: # /dad_commands bring up a commited message with the commands used in bot
                await message.channel.send(lists.help)
            elif message.content == "/ver":
                await message.channel.send("My current Version is: " + str(ver))

####### Response's #######
            elif message.content in (lists.potty_mouth):
                await message.channel.send("You better watch your mouth or im taking off the belt")
            elif message.content in ["How are you dad bot?", "how are you dad bot?"]:
                await message.channel.send("Oh wonderful thanks for asking")

client = MyClient()
client.run('Token goes here') # bot token
