import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
print(f"Verity conectado como {bot.user}")

@bot.command()
async def ping(ctx):
await ctx.send("¡Estoy online! 🏓")

Aqui va tu token de Render
bot.run(os.getenv("TOKEN"))