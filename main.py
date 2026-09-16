import discord
from discord.ext import commands
import os
from threading import Thread
from flask import Flask

app = Flask('')
@app.route('/')
def home():
    return "Verity online!"
def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
Thread(target=run_flask).start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Verity conectado como {bot.user}")

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Verity - NoobHaven", description="¡Estoy online! 🟢", color=0x2b2d31)
    embed.add_field(name="Comandos", value="`?ayuda` - Muestra esto", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if bot.user in message.mentions and not message.author.bot:
        await message.channel.send(f"Hola {message.author.mention} usa `?ayuda`")
    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
