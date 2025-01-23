import pyshorteners

shortener = pyshorteners.Shortener()

long_url = "http://example.com"
short_url = shortener.tinyurl.short(long_url)

print("Shortened URL:", short_url)
