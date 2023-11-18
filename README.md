# YouTube-RSS-Scraper
A small Python script which allows you to get the RSS link to any YouTube channel.

# How to use?
Before using the script please install **requests_html** with pip.
`pip install requets_html`

Once that is done, you can use the script!

1. Get the channel's handle.
The "handle" is the name that has an "**@**" in front of it, **NOT the channel name**. You can find this by going to the main page of the YouTube channel, and looking under the channel name.

2. Run the Python script and enter that handle.

3. It will return the link to that channel's RSS Feed, which you can input into any RSS Feed client.

# Example
For anyone who needs it, here's a quick example. In the following example we will be using the YouTube channel [LEMMiNO](https://www.youtube.com/@LEMMiNO)

Find the channel's handle
![lemmino](https://github.com/dontna/YouTube-RSS-Scraper/assets/85905830/ab396afe-cd5e-4758-8410-348560b7a7b6)

here we can see that it is **@LEMMiNO** (the case doesn't matter)

Once you run the script you will be met with a prompt "Enter YouTube username:", enter the handle here.
![python-sccc](https://github.com/dontna/YouTube-RSS-Scraper/assets/85905830/1896997a-e905-47d2-895f-ae314cefa5ab)

Press enter, and give it a couple of seconds. You'll see something like this once it is done:
![python-srrrr](https://github.com/dontna/YouTube-RSS-Scraper/assets/85905830/0eeee6ba-4d1f-4e9f-8cba-85b2bcd1836b)

In this example our RSS link is: https://www.youtube.com/feeds/videos.xml?channel_id=UCRcgy6GzDeccI7dkbbBna3Q

That is your RSS link that you can put in any RSS Feed client, to see the latest uploads!

# Issues
~~1. Sometimes the script may throw an "error", but it still shows the RSS Link. I'll get round to fixing that soon!~~ ***[Potentially Fixed]***
