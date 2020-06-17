import discord
from discord.ext import commands
import datetime
import time

bot=commands.Bot(command_prefix="+")
BOT_OWNER_ROLE="Accuracy"

@bot.event
async def on_ready():
    print('online')
    
@bot.command()
async def qp(ctx,game_time:str,accuracy:str,prize_won:str,last_question:str,result:str):
    await ctx.message.delete()
    author=ctx.message.author
    if last_question== 'correct':
        check="white_check_mark"
    else:
        check="x"
    if result=='won':
        emoji="tada"
    else:
        emoji="sob"
    if BOT_OWNER_ROLE in [role.name for role in author.roles]:
        embed=discord.Embed(title="Game Result", descriptions=f"{ctx.guild.name}", colour=0x142c9c)
        embed.add_field(name="Quipp", value=f"Game Time: {game_time} alarm_clock\nAccuracy: {accuracy}{check}\nPrize Won:{prize_won} moneybag\nLast Question status: {last_question}{check}\nGame Status: {result} {emoji}")
        embed.set_footer(text="Made By ANKUSH乛JAIN#0676 ")
        await ctx.send(content="@everyone white_check_mark", embed=embed)
        
        
bot.run("NzIyNzU3NTU4OTgwMzEzMTM4.Xunudg.j38fYyawxrpM74r5POFLEttdNb8")
