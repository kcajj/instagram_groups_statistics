# instagram_groups_statistics
get the statistics of the messages and likes of your friends' group on Instagram

Have you ever wondered who sends the best memes on the Instagram group you have with your friends? No? Well it doesn't matter.
Here's how to obtain the statistics of the likes exchanged within an Instagram group. Enjoy.

I'll add the detailed instructions sooner or later

**Disclaimer**: you will work on your private data, do not share your data with anyone and work only on your local machine.

Overview:
- download the lastest release of the script
- install the requirements
- [download your instagram inbox data](#How-to-download-the-instagram-data)
- [set the nickname decodification](#how-to-set-the-nickname-decodification)
- share the output with your friends

### How to download the instagram data
Instagram has stored all of your interactions with whatever element of the platform since you created your account. I know it sounds creepy, but it's pretty usefull for this project.

Fortunatly it's very easy to retrieve all of that data, you just go on your profile.........

Open the directory, go in the messages folder and select for the folder having the name of the instagram group you want to analyse. Extract the message_1.html file into the project directory.

### How to set the nickname decodification

some instagram user names may contain non-unicode characters and they become unreadable in the output, a quick solution to this problem is to fill the decode function.
Set the unreadable user name in the if statement and the chosen nickname in the return statement.