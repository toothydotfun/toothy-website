import sys 
from discord_webhook import DiscordWebhook

username = sys.argv[1]
message = sys.argv[2]
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/696002952284078100/K9EtqkPtS94k4VL7D-dqAN6bg2Nf2H5kgu-OrbkeQMCMR2H6jKpQy9RGvsPrFbBEduXm', content="<`"+username+"`> "+message)
webhook.execute()
