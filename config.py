# from aiofb import GraphAPI
from dotenv import load_dotenv
import argparse


load_dotenv()
# graph_api = GraphAPI(access_token=os.environ.get("FACEBOOK_GRAPH_API_ACCESS_TOKEN"))
args_parser = argparse.ArgumentParser()
args_parser.add_argument("--min-age", type=int, required=False)
args_parser.add_argument("--max-age", type=int, required=False)
args_parser.add_argument(
    "--gender", type=str, choices=("male", "female"), required=False
)
args_parser.add_argument("--country", type=str, required=False)
# add relationship criteria argument and functional
# add languages criteria argument and functional
# add reset app database argument and functional


SEARCH_CRITERIA = ('friends', 'city', 'education', 'work')
