# Trying to read the rss feed at: https://status.webex.com/history.rss #
import feedparser
import ssl

url = "https://status.webex.com/history.rss"

# feed is ssl #
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# parse the feed #
webex = feedparser.parse(url)

for e in webex.entries:
    print(e.published + ": " + e.title)
