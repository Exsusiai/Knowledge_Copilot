import os
from notion_client import Client
from pprint import pprint

os.environ["NOTION_TOKEN"] = "secret_B69MDsqd8DGJ7DJSOStNQZKPTxykXEcE98588W8Or8F"

notion = Client(auth=os.environ["NOTION_TOKEN"])

list_users_response = notion.users.list()
pprint(list_users_response)