import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print ("bot is ready.")

@bot.command()
async def ping(ctx):
    latency = round (bot.latency, 1)
    await ctx.send(f"Pong! {latency}")

@bot.command()
async def hi(ctx, member):
    await ctx.send(f"Hello! {member}")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member :  discord.Member, *,reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "Thla azin!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await member.ban(reason=reason)
    await ctx.send(f"{member} is banned!")

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason="Thla azin"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 50): # Change amount
  if ctx.message.author.id == (453206040562106400):
    await ctx.channel.purge(limit=amount)
  else:
    await ctx.channel.send(f"{ctx.author.mention} you are not allowed")



@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


bot.run("ODI4OTk1MzUzODgwODIxNzgz.YGxsFg.mANHJagCwzmPyvRTFEJAK6Nl_6w")
