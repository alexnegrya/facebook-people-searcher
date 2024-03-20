import asyncio
import aiohttp
# from aiofb import GraphAPI
import string


_SUPPORTED_CRITERIA = ('min_age', 'max_age', 'gender', 'country', 'city')


class PeopleSearcher:
    def __init__(self):
        # self.graph_api = graph_api
        self.loop = asyncio.get_event_loop()
        self.letters = tuple(string.ascii_lowercase)
        self.letter_index = 0
    
    def __is_user_duplicate(self, user):
        pass
    
    def __get_users_by_current_letter(self):
        # users = self.loop.run_until_complete(self.graph_api.get("/search", {
        #     "q": self.letters[self.letter_index], "limit": 10}))
        self.letter_index += 1
    
    def __filter_users_by_criteria(self, users, criteria):
        pass

    def search_users(self, **criteria):
        if any([c not in _SUPPORTED_CRITERIA for c in criteria]):
            raise ValueError('these criteria are not supported')
