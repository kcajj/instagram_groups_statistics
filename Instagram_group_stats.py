from bs4 import BeautifulSoup

def decode(string):
    if string=="instagram_user_name_partecipant_1":
        return "nickname_1"
    elif string=="instagram_user_name_partecipant_2":
        return "nickname_2"
    else:
        return string
    
with open('message_1.html', encoding="cp437") as data:
    soup = BeautifulSoup(data, 'html.parser')

sent_messages = {}
got_likes = {}
given_likes = {}
like_couples_received = {}
like_couples_given = {}

partecipants = soup.find(class_="pam _3-95 _2ph- _a6-g uiBoxWhite noborder").find(class_="_a6-h").string
partecipants_names= partecipants.split(": ")[1].split(", ")

for c in range(len(partecipants_names)):
    partecipants_names[c]=decode(partecipants_names[c])

for name in partecipants_names:
    sent_messages[name]=0
    got_likes[name]=0
    given_likes[name]=0
    like_couples_received[name]={}
    like_couples_given[name]={}

for name in partecipants_names:
    for coupled_name in partecipants_names:
        like_couples_received[name][coupled_name]=0
        like_couples_given[name][coupled_name]=0

names_soup = soup.find_all(class_ = '_3-95 _2pim _a6-h _a6-i')

for i in names_soup:
    sender=decode(i.string)
    sent_messages[sender]+=1

    parent=i.parent
    likes_list=parent.find_all(class_='_a6-q')

    for j in likes_list:
        likes=j.find_all("li")
        for liker in likes:
            liker_name=decode(liker.string[6:])
            got_likes[sender]+=1
            given_likes[liker_name]+=1
            like_couples_received[sender][liker_name]+=1
            like_couples_given[liker_name][sender]+=1

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
