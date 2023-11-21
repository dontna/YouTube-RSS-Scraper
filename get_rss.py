from requests_html import HTMLSession

def GenerateChannelLink(creator_tag: str):
    if creator_tag.__contains__("@"):
        return f"https://www.youtube.com/{creator_tag}"
    else:
        return f"https://www.youtube.com/@{creator_tag}"

def GetRSSLink(creator_link: str):
    with HTMLSession() as s:
        r = s.get(creator_link, cookies={"SOCS": "CAESEwgDEgk0ODE3Nzk3MjQaAmVuIAEaBgiA_LyaBg"})

        if r.status_code == 404:
            return 1

        try:
            RSS_link = r.html.xpath("/html/body/link[4]", first=True).attrs['href']
        except:
            return 1
            
    return RSS_link

if __name__ == "__main__":
    username = input("Enter YouTube username: ")

    print("Generating Channel Link...")
    channel_link = GenerateChannelLink(username)

    print(f"Getting RSS Link for \"{username}\", this may take a moment...")
    RSS_link = GetRSSLink(channel_link)

    print(username, "RSS Link:", RSS_link)
