from config import *
from searcher import PeopleSearcher


if __name__ == "__main__":
    args = args_parser.parse_args()
    searcher = PeopleSearcher()
    users = searcher.search_users(**args)
    print(users)
