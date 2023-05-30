# instagram_groups_statistics
get the statistics of the messages and likes of your friends' group on Instagram

Have you ever wondered who sends the best memes on the Instagram group you have with your friends? No? Well it doesn't matter.
Here's how to obtain the statistics of the likes exchanged within an Instagram group. Enjoy.

**!!!Watch out!!!**: you will work on your private data, do not share your data with anyone and work only on your local machine.

**Overview**:
- Download the [lastest release](https://github.com/kcajj/instagram_groups_statistics/releases) of the script
- Install the [requirements](#requirements)
- [Download your instagram inbox data](#How-to-download-the-instagram-data)
- [Set the nickname decodification](#how-to-set-the-nickname-decodification)
- Share the output with your friends

### How to download the instagram data
Instagram has stored all of your interactions with whatever element of the platform since you created your account. I know it sounds creepy, but it's pretty usefull for this project.

Fortunatly it's very easy to retrieve all of that data. If you're on browser you can select the three lines in the bottom left corner and click on your activity. Then you press on "Download your information", at this point instagram will ask you to insert an email address and the desidered file format, select HTML and click next. Instert your passowrd and after a while you should recieve an email containing a zipped folder with all of your data.

See the [official instagram guide](https://help.instagram.com/181231772500920/?cms_platform=iphone-app&helpref=platform_switcher) to download the data.

Download the folder and explore it a little, by opening the file "index.html" you will have a broad view of whhich data Instagram usually collects.
Now go in the messages folder and select for the folder having the name of the instagram group you want to analyse. Extract the message_1.html file and copy it in the project directory.

### How to set the nickname decodification

some instagram user names may contain non-unicode characters and they become unreadable in the output, a quick solution to this problem is to fill the decode function.
Set the unreadable user name in the if statement and the chosen nickname in the return statement.

### How to read the output

- sent messages: ...
- given likes: ...
- likes percentage: ...
- received likes: ...
- interactions with other users: ...

A ton of other statistics could be implemented, if you have any idea do not hesitate to let me know.

### Requirements

- Python (version 3.10.2)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) (version 4.11.1)