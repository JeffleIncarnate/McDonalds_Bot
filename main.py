# Imports
import discord
import random
from Keep_Alive import Keep_Alive
import time

# Variables
client = discord.Client()
a = "Here is your "
b = " enjoy!"
Last = ["Enjoy your food!", "WHERE IS THE LAMB SAUCE", "Thank you for coming", "Now take your food and take a seat!", "Go AWAY", 'Gordon Ramsey']


# Event 1
@client.event
async def on_ready():
    print("We have logged as user {0.user}".format(client))

# Event 2
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Local Variables
    send = message.channel.send
    msg = message.content

    # Commands
    if msg.startswith("#Commands"):
        await send("Here is a list of our commands!")
        await send("#Menu")
        await send("#Burger")
        await send("#Fries")
        await send("#Chicken Nuggets")
        await send("#Coke")
        await send("#Muffin")

    elif msg.startswith("#commands"):
        await send("Here is a list of our commands!")
        await send("#Menu")
        await send("#Burger")
        await send("#Fries")
        await send("#Chicken Nuggets")
        await send("#Coke")
        await send("#Muffin")

    # Menu
    elif msg.startswith("#Menu"):
        await send("Here is our Menu, Fries, Burger, Chicken Nuggets, Coffee, Coke")

    elif msg.startswith("#menu"):
        await send("Here is our Menu, Fries, Burger, Chicken Nuggets, Coffee, Coke")

    # Fries
    elif msg.startswith("Gimmie Fries"):
        await send(a + "Fries" + b)
        await send(random.choice(Last))

    elif msg.startswith("#gimmie fries"):
        await send(a + "Fries" + b)
        await send(random.choice(Last))

    # Burger
    elif msg.startswith("Gimmie Burger"):
        await send(a + "Burger" + b)
        await send(random.choice(Last))

    elif msg.startswith("gimmie burger"):
        await send(a + "Burger" + b)
        await send(random.choice(Last))

    # Chicken Nuggets
    elif msg.startswith("Gimmie Nuggets"):
        await send(a + "Chicken Nuggets" + b)
        await send(random.choice(Last))

    elif msg.startswith("gimmie nuggets"):
        await send(a + "Chicken Nuggets" + b)
        await send(random.choice(Last))

    # Coffee
    elif msg.startswith("Gimmie Coffee"):
        await send(a + "Coffee" + b)
        await send(random.choice(Last))

    elif msg.startswith("gimmie coffee"):
        await send(a + "Coffee" + b)
        await send(random.choice(Last))

    # Coke
    elif msg.startswith("Gimmie Coke"):
        await send(a + "Coke" + b)
        await send(random.choice(Last))

    elif msg.startswith("gimmie coke"):
        await send(a + "Coke" + b)
        await send(random.choice(Last))

    # Muffin
    elif msg.startswith("Gimmie Muffin"):
        await send(a + "Muffin" + b)
        await send(random.choice(Last))

    elif msg.startswith("gimmie muffin"):
        await send(a + "Muffin" + b)
        await send(random.choice(Last))

# Keep Alive
Keep_Alive()

# Client Key
client.run('ODY0MDIxNDUwMDg3MDcxNzY2.YOvYrg.a0ljedw6FEPoaYkIhRIHx4JorgI')
