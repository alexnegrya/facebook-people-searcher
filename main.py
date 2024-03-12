from config import *
from async_funcs import get_facebook_users


if __name__ == "__main__":
    args = args_parser.parse_args()
    users = graph_api.get("search", {"q": "a", "limit": 10})
    print(users)
