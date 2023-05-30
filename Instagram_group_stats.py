#import beautiful soup
from bs4 import BeautifulSoup

#set the user name decodification
def decode(string):
    if string=="instagram_user_name_partecipant_1":
        return "nickname_1"
    elif string=="instagram_user_name_partecipant_2":
        return "nickname_2"
    #...
    else:
        return string

#open the group chat file using cp437 decodification, in this way any strange character coming from any message
#won't generate an error
with open('message_1.html', encoding="cp437") as data:
    #create a beautiful soup object
    soup = BeautifulSoup(data, 'html.parser')

#initialise all of the dictionaries that will contain the statistics
sent_messages = {}
got_likes = {}
given_likes = {}
like_couples_received = {}
like_couples_given = {}

#list the partecipants
partecipants = soup.find(class_="pam _3-95 _2ph- _a6-g uiBoxWhite noborder").find(class_="_a6-h").string
partecipants_names= partecipants.split(": ")[1].split(", ")
for c in range(len(partecipants_names)):
    #decode the user names of the partecipants accordingly to the nicknames
    partecipants_names[c]=decode(partecipants_names[c])

#add each partecipant as a key to each dictionary
for name in partecipants_names:
    sent_messages[name]=0
    got_likes[name]=0
    given_likes[name]=0
    like_couples_received[name]={}
    like_couples_given[name]={}

#initialise the dictionaries that report the interaction statistics of the group members, thanks to this
#data you will know which users have a similar sense of humor (they exchange more likes between each other)
for name in partecipants_names:
    for coupled_name in partecipants_names:
        like_couples_received[name][coupled_name]=0
        like_couples_given[name][coupled_name]=0

#find all of the name of the sender of each message in the group
names_soup = soup.find_all(class_ = '_3-95 _2pim _a6-h _a6-i')

#loop for each message
for i in names_soup:
    #add the nickname of who sent the message to the "sent_messages" statistics dictionary
    sender=decode(i.string)
    sent_messages[sender]+=1

    #consider the whole message data with .parent, and go to the likes section by searching for the class "_a6-q"
    likes_list=i.parent.find_all(class_='_a6-q')
    #loop for all the likes that the message received
    for j in likes_list:
        #find all the users that gave a like to the message
        likes=j.find_all("li")
        #loop though all the user names of who liked the message
        for liker in likes:
            #add the like to the "got_likes" dictionary statistics of who sent the message
            got_likes[sender]+=1
            #retrieve the nickname of who gave the like: we slice the user name excluding the first six characters
            #because the name is stored after a heart emojy that in the cp437 decodification takes up six characters
            liker_name=decode(liker.string[6:])
            #add the like to the "given_likes" dictionary statistics of who gave the like
            given_likes[liker_name]+=1
            #add the reciprocal interactions to the other dictionaries
            like_couples_received[sender][liker_name]+=1
            like_couples_given[liker_name][sender]+=1

#print the statistics (a lot more can be added)
for name in partecipants_names:
    print(name.upper())
    print("sent messages:", sent_messages[name])
    print("received likes:", got_likes[name])
    print("likes percentage:", round(got_likes[name]/sent_messages[name]*100),"%")
    print("given likes:", given_likes[name])
    print()
    print(name, "gave:")
    for i in like_couples_given[name].items():
        print(i[1], "likes to", i[0])
    print()
    print(name, "received:")
    for j in like_couples_received[name].items():
        print(j[1], "likes from", j[0])
    print()
    print()
    print()
