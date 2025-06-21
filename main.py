import discord
import random
from discord.ext import commands
from genpass import gen_pass
from flip import flip_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

quotes = [
    "Semangat! Hari ini milikmu",
    "Gagal itu biasa, bangkit itu luar biasa!",
    "Teruslah belajar, karena dunia tak pernah berhenti berubah",
    "Kamu hebat, dan kamu pasti bisa!",
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, panjang = 5):
    await ctx.send(gen_pass(panjang))

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def tebak(ctx):
    global jawaban
    jawaban = random.randint(0, 11)
    await ctx.send("tebak dari satu sampai 12")

@bot.command()
async def answear(ctx):
    if answear == int(jawaban):
        await ctx.send("jawaban mu benar")
    else:
        await ctx.send("salah")

@bot.command()
async def katakatahariini(ctx):
    await ctx.send(random.choice(quotes))
        
bot.run("token")
