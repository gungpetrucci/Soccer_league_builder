import csv
import random

dragons_member = []
sharks_member = []
raptors_member = []
dragons_newbie_member = []
sharks_newbie_member = []
raptors_newbie_member = []
dragons_exp_member = []
sharks_exp_member = []
raptors_exp_member = []
dragons_guardian = []
sharks_guardian = []
raptors_guardian = []
player_list = []
PRACTICE_TIME = ('March 17, 1pm', 'March 17, 3pm', 'March 18, 1pm')

#function call for import data from csv into list name "player_list"
def csv_to_list():
    global player_list
    with open('soccer_players.csv', 'r') as soccer_players:
        soccer_reader = csv.reader(soccer_players, delimiter=',')
        player_list = []
        for row in soccer_reader:
            player_list.append(row)
    del player_list[0]



#function call when the player is experience player, check the team whether is there is too many experiance player in the team?
def random_insert_exp_player(player):
    player_team = random.randrange(1,4)
    if player_team == 1:
        if len(dragons_exp_member) >= 3:
            random_insert_exp_player(player)
        else:
            dragons_exp_member.append(player[0])
            dragons_member.append(player[0])
            dragons_guardian.append(player[3])
    elif player_team == 2:
        if len(sharks_exp_member) >= 3:
            random_insert_exp_player(player)
        else:
            sharks_exp_member.append(player[0])
            sharks_member.append(player[0])
            sharks_guardian.append(player[3])
    elif player_team == 3:
        if len(raptors_exp_member) >= 3:
            random_insert_exp_player(player)
        else:
            raptors_exp_member.append(player[0])
            raptors_member.append(player[0])
            raptors_guardian.append(player[3])
    else:
        print('ERROR RANDOM exp TEAM')

#function call when the player is newbie player, also check if the team has too many newbie player.
def random_insert_newbie_player(player):
    player_team = random.randrange(1,4)
    if player_team == 1:
        if len(dragons_newbie_member) >= 3:
            random_insert_newbie_player(player)
        else:
            dragons_newbie_member.append(player[0])
            dragons_member.append(player[0])
            dragons_guardian.append(player[3])
    elif player_team == 2:
        if len(sharks_newbie_member) >= 3:
            random_insert_newbie_player(player)
        else:
            sharks_newbie_member.append(player[0])
            sharks_member.append(player[0])
            sharks_guardian.append(player[3])
    elif player_team == 3:
        if len(raptors_newbie_member) >= 3:
            random_insert_newbie_player(player)
        else:
            raptors_newbie_member.append(player[0])
            raptors_member.append(player[0])
            raptors_guardian.append(player[3])
    else:
        print('ERROR RANDOM newbie TEAM')

#open file is 'w' and generate file name of player's name, write the letter and save&close.
def letter_writer(player_list, guardian_list):
    for player in player_list:
        with open(str(player).replace(' ','_') + ".txt", 'w') as letter:
            letter.write('Dear {},'.format(guardian_list[player_list.index(player)]))
            letter.write('\n\n')
            if player in dragons_member:
                player_team = 'Dragons'
                player_time = PRACTICE_TIME[0]
            elif player in sharks_member:
                player_team = 'Sharks'
                player_time = PRACTICE_TIME[1]
            elif player in raptors_member:
                player_team = 'Raptors'
                player_time = PRACTICE_TIME[2]
            else:
                print('ERROR cant find team')
                exit()
            letter.write("""
    I'am glad to tell you that your child, {}, has been selected to join the soccer league as a player for {} soccer team.\n
    We are looking forward to see you in our first field practice at school on {}.\n\nRegards,\nHarin Yu.
""".format(player, player_team, player_time))
            



if __name__ == '__main__':
    csv_to_list()
    player_list
    for player in player_list:
        if player[2] == 'YES':
            random_insert_exp_player(player)
        else:
            random_insert_newbie_player(player)

    player_list = dragons_member + sharks_member + raptors_member
    guardian_list = dragons_guardian + sharks_guardian + raptors_guardian

    letter_writer(player_list, guardian_list)

