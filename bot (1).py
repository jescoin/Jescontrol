from colorama import init
init()
from colorama import Fore, Back, Style
#my github - https://github.com/jescoin
a = Fore.BLACK+Back.CYAN+'                                                                                 [v 1.0] '
import time
from time import *

import berserk

print(Fore.CYAN+'''                        
                                                                                 
                                                                     
     ██╗███████╗███████╗ ██████╗ ██████╗ ██╗███╗   ██╗
     ██║██╔════╝██╔════╝██╔════╝██╔═══██╗██║████╗  ██║
     ██║█████╗  ███████╗██║     ██║   ██║██║██╔██╗ ██║
██   ██║██╔══╝  ╚════██║██║     ██║   ██║██║██║╚██╗██║
╚█████╔╝███████╗███████║╚██████╗╚██████╔╝██║██║ ╚████║
 ╚════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
   ''',Fore.CYAN+Back.BLACK +'                           [v 1.0]',Style.RESET_ALL
)
token = input('Token:')
print('')
print(Fore.BLACK+Back.RED+"Lichess account' control. if you know the Token, you can easily use this program. ")
print(Style.RESET_ALL)

print('')
print('')
print(Fore.RED+'---------------------------------------------------------------------------------')
print(Fore.MAGENTA+'[1]kick member           [2]join team               [3] leave team')
print(Fore.YELLOW+'[4]get email             [5]set kid mode            [6]upgrade to bot ')
print(Fore.RED+'[7]offer draw            [8]make move               [9]resign game')
print(Fore.CYAN+'[10]post message         [11] get kid mode         [12]get members')
print(Fore.GREEN+'[13]get all top 10       [14]get rating history     [15]get activity ')
print(Fore.MAGENTA+'[16]get leaderboard      [17]get tv channels                                        [99]exit')
print(Fore.RED+'---------------------------------------------------------------------------------')

session = berserk.TokenSession(token)
client = berserk.Client(session=session)
c = int(input('[?] Choose an action:'))

#MAKE A LOT OF FUNCS
def n1():
    team = input('Team id:')
    user = input('User id:')
    client.teams.kick_member(team, user)
    print('The user', user, 'was kicked!')

def n2():
    team= input('Team id:')
    message = input('Optional requires message:')
    password = input('Not necessary. Just if the team requires. ')
    client.teams.join(team, message, password)
    print('You join this team!')

def n3():
    team = input('Team id:')
    client.teams.leave(team)
    print('You leave from this team!')

def n4():
    a = client.account.get_email()
    print(a)

def n5():
    client.account.set_lid_mode()
    print('You set kid mode!')

def n6():
    client.account.upgrade_to_bot()
    print('Success!')

def n7():
    game_id = input('Game id:')
    accept=True
    client.board.handle_draw_offer(game_id, accept)
    print('You offer the draw!')

def n8():
    game_id = input('Game id:')
    move = input('Move:')
    client.board.make_move(game_id,move)
    print(f'You move:{move}')

def n9():
    game_id=input('Game id:')
    client.board.resign_game(game_id)
    print('You resign..')

def n10():
    game_id=input('Game id:')
    text = input('What is the text?: ')
    client.board.post_message(game_id, text, spectator=False)

def n11():
    client.account.get_kid_mode()

def n12():
    team_id = input('Team id:')
    client.teams.get_members(team_id)

def n13():
    client.users.get_all_top_10()

def n14():
    username = input('Username:')
    client.users.get_rating_history(username)

def n15():
    username = input('Username:')
    client.users.get_activity_feed(username)

def n16():
    perf_type = input('What is the speed or variant:')
    a = int(input('Number of players to get: '))
    client.users.get_leaderboard(perf_type, count=a)

def n17():
    client.games.get_tv_channels()

def n99():
    print('The program will exit during 5 secs')
    time.sleep(5)
    exit()


# A LOT OF "IF":

if c ==1:
    n1()

if c ==2:
    n2()

if c ==3:
    n3()

if c ==4:
    n4()

if c ==5:
    n5()

if c ==6:
    n6()

if c ==7:
    n7()

if c ==8:
    n8()

if c ==9:
    n9()
if c ==10:
    n10()
if c ==11:
    n11()
if c ==12:
    n12()
if c ==13:
    n13()
if c ==13:
    n14()
if c ==15:
    n15()
if c ==16:
    n16()
if c ==17:
    n17()
if c==99:
    n99()








