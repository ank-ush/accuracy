import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='+')

BOT_OWNER_ROLE = "fetch"


@bot.event
async def on_ready():
    print('Online')


@bot.command(name="send")
async def send(ctx,*,msg):
    await ctx.message.delete()
    author=ctx.message.author
    
    for member in ctx.guild.members:
        try:
            await member.send(msg)
            embed=discord.Embed(title="Mass DM",description=f"DM sent to {member.name}#{member.discriminator} \n✅",colour=0x142c9c)
            embed.set_image(url="https://cdn.discordapp.com/attachments/568829761531543582/573936305495605269/animated-line-image-0379.gif")
            embed.set_footer(text="Made By Steevo#3838",icon_url="")
            await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title='''Mass DM''',description=f'''DM Not sent to {member.name}#{member.discriminator}''' ''' ❌ ''',colour=0x142c9c)
            embed.set_image(url="https://cdn.discordapp.com/attachments/568829761531543582/573936305495605269/animated-line-image-0379.gif")
            embed.set_footer(text="Made By Steevo#3838",icon_url="")
            await ctx.send(embed=embed)
                
            embed=discord.Embed(title="DM sent to all",description=f" ✅ ",colour=0x142c9c)
            embed.set_image(url="https://cdn.discordapp.com/attachments/568829761531543582/573936305495605269/animated-line-image-0379.gif")
            embed.set_footer(text="Made by ANKUSH乛JAIN#0676",icon_url="")
            await ctx.send(embed=embed)

bot.run("NzIyNzU5OTYwOTM2NTc5MTYy.XunwtA.RDNiKbeV1RBxwZz9Il58t0ZUcSU")
