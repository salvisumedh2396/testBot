import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

#we have created a client here
client = commands.Bot(command_prefix='.', intents=intents)

#we have given the client an event to look forward to
@client.event
async def on_ready():
    print('Bot is ready.')

#gets triggered when a new member joins the server
#here member is an object
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#gets triggered when a member leaves the server/ gets kicked from the server
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all arguments.')

#ctx - represents the context of the command
#when user types .ping it will print pong with latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#we are taking the context and accessing the channel
#ctx.channel gets the channel on which we are runing the command
#amount indicates how many message are going to be purged
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#an error that is specific to clear command
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete')

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discrimiator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discrimiator}')
            return

# * - allows to take multiple arguments as one argument (stacks them all up instead of consdering them seperate
#  aliases - any input given by user from aliases list will generate desired o/p
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *,question):
    responses = ['It is certain',
                 'definitely',
                 'impossible']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#and then, we need to run the client
#within the parenthesis we need to add the token - it links the code to the
#application so that the code can manipulate the appln
client.run('ODg4MjUyNjA5MDU0NTA3MDE4.YUP_tA.ZkRi9PcX5zFLKk4c8XCFJTZZ76w')

