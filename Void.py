import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = Bot(description="I am The local Guard in Void Sector", command_prefix="V", pm_help = True)
client.remove_command('help')

	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Created By Zenzoy')
    await client.change_presence(game=discord.Game(name="工𠘨  リ口工刀  丂乇匚丅口尺", type=1))

def is_owner(ctx):
    return ctx.message.author.id == "471988330335174667"
	

@client.command(pass_context = True)
@commands.check(is_owner)
async def restart():
    await client.logout()

@client.event
async def on_message(message):
	await client.process_commands(message)

@client.event
async def on_member_join(member):
     if member.server.id == "513758096011821078": 
        print("In our server" + member.name + "just joined")
        embed = discord.Embed(color = 0x5c0587)
        embed.set_author(name='Welcome to Void Flotilla')
        embed.add_field(name = 'Welcome to Our Server!',value ='**Please be active and read rules. ',inline = False)
        embed.set_image(url = 'https://i.imgur.com/F7Pc7x0.png')
        await client.send_message(member,embed=embed)
        print("Sent message to " + member.name)
        channel = discord.utils.get(client.get_all_channels(), server__name='Void Flotilla', name='welcome')
        embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules.', color = 0x5c0587)
        embed.add_field(name='Thanks for joining!', value='**Please be active here.**', inline=True)
        embed.add_field(name='Your join position is', value=member.joined_at)
        embed.set_image(url = 'https://i.imgur.com/F7Pc7x0.png')
        embed.set_thumbnail(url=member.avatar_url)
        await client.send_message(channel, embed=embed)


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)

async def unbanall(ctx):
    server=ctx.message.server
    ban_list=await client.get_bans(server)
    await client.say('Unbanning {} members'.format(len(ban_list)))
    for member in ban_list:
        await client.unban(server,member)

	


	

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def joinvoice(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = 0x5c0587)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
	
    
    
	

	
@client.command(pass_context = True)

@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("You haven't specified a role! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("{} role has been added to {}.".format(role, user))

        if role in user.roles:
            await client.remove_roles(user, role)
            return await client.say("{} role has been removed from {}.".format(role, user))
 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, ":warning: __**You have been warned:warning: Reason **{}** **__".format(message))
    await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
    pass

@client.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- Void", color=0x5c0587)
    embed.set_footer(text="Copyright")
    embed.set_author(name=" Bot Owner Name -Zenzoy#6460 -ID:471988330335174667")
    await client.say(embed=embed)
	
	
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="The ancient ones have Muted **{0}** #information, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
          
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="The ancient ones have Unmuted **{0}** #information, to see the rules!".format(member, ctx.message.author), color=0x6b009c)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)
        await client.say(embed=embed)
    
@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), color = 0x5c0587)
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
        

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0x5c0587)
    embed.set_author(name='Help')
    embed.set_image(url = 'https://i.imgur.com/F7Pc7x0.png')
    embed.add_field(name = 'Vguardhelp ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
    embed.add_field(name = 'Vvoidhelp ',value ='Explaines all the commands which are usable by everyone.',inline = False)
    await client.send_message(author,embed=embed)
    await client.say('📨 Check DMs For Information')

@client.command(pass_context = True)
async def guardhelp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0x5c0587)
    embed.set_author(name='Moderation Commands Help')
    embed.set_image(url = 'https://i.imgur.com/F7Pc7x0.png')
    embed.add_field(name = 'Vsay(Admin permission required) ',value ='Use it like ``Vsay <text>``',inline = False)
    embed.add_field(name = 'Vembed(Admin permission required) ',value ='Use it like ``Vembed <text>``',inline = False)
    embed.add_field(name = 'Vrole(Manage Roles Permission Required)',value ='Use it like ``Vrole @user <rolename>``.',inline = False)
    embed.add_field(name = 'Vsetnick(Manage nickname permission required)',value ='Use it like ``Vsetnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
    embed.add_field(name = 'Vserverinfo(Kick members Permission Required) ',value ='Use it like ``Vserverinfo`` to get server info',inline = False)
    embed.add_field(name = 'Vuserinfo(Kick members Permission Required) ',value ='Use it like ``Vuserinfo @user`` to get some basic info of tagged user',inline = False)
    embed.add_field(name = 'Vkick(Kick members Permission Required)',value ='Use it like ``Vkick @user`` to kick any user',inline = False)
    embed.add_field(name = 'Vroles(Kick members Permission Required) ',value ='Use it to check roles present in server',inline = False)
    embed.add_field(name = 'Vclear(Manage Messages Permission Required)',value ='Use it like ``Vclear <number>`` to clear any message',inline = False)
    embed.add_field(name = 'Vmute(Mute members Permission Required)',value ='Use it like ``Vmute @user <time>`` to mute any user',inline = False)
    embed.add_field(name = 'Vunmute(Mute members Permission Required) ',value ='Use it like ``Vunmute @user`` to unmute anyone',inline = False)
    embed.add_field(name = 'Vban(Ban members Permission Required) ',value ='Use it like ``Vban @user`` to ban any user',inline = False)
    embed.add_field(name = 'Vrules(Kick members Permission Required)',value ='Use it like ``Vrules @user <violation type>`` to warn user',inline = False)
    embed.add_field(name = 'Vwarn(Kick members Permission Required)',value ='Use it like ``Vwarn @user <violation type>`` to warn any user',inline = False)    
    await client.send_message(author,embed=embed)
    await client.say('📨 Check DMs For Information')

@client.command(pass_context = True)
async def voidhelp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0x5c0587)
    embed.add_field(name = 'Vpoll ',value ='Use it like ``Vpoll "Question" "Option1" "Option2" ..... "Option9"``.',inline = False)
    embed.add_field(name = 'For Information')

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await client.say('**He is mod/admin and i am unable to kick him/her**')
        return
    
    try:
        await client.kick(user)
        await client.say(user.name+' was kicked. Good bye '+user.name+'!')
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        await client.say('Permission denied.')
        return

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)      



    	 		


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await client.say('**He is mod/admin and i am unable to ban him/her**')
        return

    try:
        await client.ban(user)
        await client.say(user.name+' was banned. Good bye '+user.name+'!')

    except discord.Forbidden:

        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('ban failed.')
        return		 



@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await client.say('Ban list is empty.')
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('unban failed.')
        return		      	 		 		  
  
@client.command(pass_context = True)
@commands.has_permissions(send_messages=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Read Rules again and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);


@client.command(pass_context=True)
async def unverify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
async def verify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Verified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makeguard(ctx, user: discord.Member):
    nickname = '♏' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Guard Member')
    await client.add_roles(user, role)
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def removeguard(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Guard Member')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await client.say("Invalid number")
    else:
        await client.say('The correct answer is ' + str(arg))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await client.say(result)
    
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)
	
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    """
    Sending embeded messages with color (and maby later title, footer and fields)
    """
    argstr = " ".join(args)
    color = 0x5c0587
    text = argstr
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    await client.delete_message(ctx.message)


client.run(os.getenv('Token'))
