import json

def get_credentials(file_path):
    
    with open(file_path) as f:
        creds = json.load(f)
        
    return creds["Access key ID"], creds["Secret access key"]

def get_bot_details(bot_name):
    
    with open(f"resources/{bot_name}_bot.json") as f:
        bot_det = json.load(f)
        
    return bot_det["bot_id"], bot_det["bot_alias"], bot_det["bot_alias_id"], bot_det["bot_locale"], bot_det["bot_version"]