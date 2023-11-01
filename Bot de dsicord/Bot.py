import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    channel_id = 1152369673573244999
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''Hola, soy Milo y sirvo para ayudarte a escoger entre nuestar lista de juegos.
                    Para poder llamarme deberas usar el prefix ?, e introducir alguno de los siguientes comandos.
                    1- choose: Te ayudara a escoger entre dos juegos
                    2 lista : Te mostrara nuestra lista de juegos''')





juegos = ["Tonto", "perro"]
@bot.command()
async def lista(ctx):
    mensaje = '\n'.join(juegos)
    await ctx.send(mensaje)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx):
    """Chooses between multiple choices."""
    a = random.choice(juegos)
    await ctx.send(a)


bot.run('MTE1OTk2ODU2ODA5NjYwNDIwMA.GwMY5n.p8qa093A2JALE5Xr5wgBDPIVVU0sXGnL3alKtI')