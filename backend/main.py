from text_parsing import client


url = "https://www.reddit.com/r/AmItheAsshole/comments/1bm4ecq/aita_not_paying_for_fathers_funeral/"

output = client.get_audio(url)
print(output)