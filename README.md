# YouTube-RSS-Scraper
A small Python script which allows you to get the RSS link to any YouTube channel.

# How to use?
Before using the script please install **requests_html** with pip.
`pip install requets_html`

OPTIONAL: If using the GUI please install **pyqt5** with pip.
`pip install pyqt5`

***The GUI was created with pyqt5 version 5.15.2***

Once that is done, you can use the script!

1. Get the channel's handle.
The "handle" is the name that has an "**@**" in front of it, **NOT the channel name**. You can find this by going to the main page of the YouTube channel, and looking under the channel name. You can also paste in the channel URL.

2. Run the Python script and enter that handle / channel URL.

3. It will return the link to that channel's RSS Feed, which you can input into any RSS Feed client. 

# GUI
Created a GUI for those who preffer this over the terminal. This is optional and can still use the terminal if preffered.

Note: If using the GUI please install **pyqt5** with pip.

![rss-getter-gui](https://github.com/dontna/YouTube-RSS-Scraper/assets/85905830/29f37d3f-c4ff-4111-8550-05de57c311dc)


# Terminal Example
For anyone who needs it, here's a quick example using the terminal. In the following example we will be using the YouTube channel [LEMMiNO](https://www.youtube.com/@LEMMiNO)

Find the channel's handle
![lemmino-edit](https://github.com/dontna/YouTube-RSS-Scraper/assets/85905830/9d090578-d172-4441-ab75-9a8879079a41)


here we can see that it is **@LEMMiNO** (the case doesn't matter)

Once you run the script you will be met with a prompt "Enter YouTube username or channel link:", enter the handle here.

Press enter, and give it a couple of seconds. You'll see something like this once it is done:
![python-srrrr](https://github.com/dontna/YouTube-RSS-Scraper/assets/85905830/0eeee6ba-4d1f-4e9f-8cba-85b2bcd1836b)

In this example our RSS link is: https://www.youtube.com/feeds/videos.xml?channel_id=UCRcgy6GzDeccI7dkbbBna3Q

That is your RSS link that you can put in any RSS Feed client, to see the latest uploads!

# Issues
If you come across any issues, bugs or problems while using this script please let me know so I can fix it.

# Fixed Issues
~~1. Sometimes the script may throw an "error", but it still shows the RSS Link. I'll get round to fixing that soon!~~ ***[Confirmed Fix]***
