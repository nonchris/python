import discord
from discord.ext import commands

PREFIX = "b!"
# TODO: Paste your token here (don't ever do this in real code!)
# Normally you should read the token from a config file or the environment
I_DONT_PASTE_TOKENS_IN_MY_CODE = ""
intents = discord.Intents.all()

bot = commands.Bot(PREFIX, intents=intents)

# TODO: remember you can look up things in the documentation:
# the guild:
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=member#discord.Guild

# the member:
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=member#discord.Member

# the TextChannel:
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=member#discord.TextChannel

@bot.event
async def on_ready():
    """
    Function called when the bot is ready. Emits the '[Bot] has connected' message
    """

    # TODO: write a for-loop that prints the names all guilds the bot is on
    #  you can access a list of all guilds using bot.guilds
    #  replace the parts with the '[]' and '...'

    for guild in []:
        guild_name = ...
        print(guild_name)

        await __sync_commands_to_guild(guild)

    # TODO: add the guild id to the print in the loop. You can access the guild id with guild.id.
    #  the result shall be like f"{guild_name} - {guild_id}"

    # TODO: now add the member count:
    #  the result shall be like f"{guild_name} - {guild_id} - Members: {member_count}"

    # TODO: make the bot sum the members of the servers it is on and print the result after the loop
    #  hint: you need a variable to count over the for loop to save the result after each loops iteration


@bot.event
async def on_message(message: discord.Message):
    """All messages the bot received are passed to this function"""

    # TODO: print the content of each message the bot receives
    # print(message.

    # we're overwriting the message listener
    # calling command bots function to process commands from text
    await bot.process_commands(message)


# TODO: exchange the 'str'-typehint to describe the type of 'member' as a Member
#  remember the syntax for a typehint is: variable: type
@bot.tree.command(name="greet")
async def greet(interaction: discord.Interaction, member: str):
    """ Greet a user with the bot"""
    # TODO: complete the response by using the members name
    await interaction.response.send_message(f"Hello {member}")

# TODO: try out the command, does it give the correct recommendations for the first argument?


# TODO: the target is to write a command that greets a member
#  but the greeting message is sent to a specific server
#  start by fixing the the signature of the function by adding the correct typehints to the function instead of 'str'
#  the first argument shall be a member the second one a channel
@bot.tree.command(name="greet_in_channel")
async def add(interaction: discord.Interaction, member: str, channel: str):
    """ Greet a user with the bot"""
    # TODO: complete the response by sending the greeting message into the given channel
    # message = f"Hello "
    # await

    # in slash commands we always need to respond to the interaction so that won't be displayed as failed
    # we do it here
    await interaction.response.send_message(f'Done :)')


# TODO: try that command too


# You can ignore this function for now, just accept that you'll need it
async def __sync_commands_to_guild(guild: discord.Guild):
    """
    Function to push all slash-commands to a guild
    Doing this for all guilds on startup is is inefficient, but a fast way to push new commands to all guilds
    """
    try:
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
        print(f"Pushed commands to: {guild.name}")
    except discord.errors.Forbidden:
        print(f"Don't have the permissions to push slash commands to: '{guild.name}'")


bot.run(I_DONT_PASTE_TOKENS_IN_MY_CODE)
