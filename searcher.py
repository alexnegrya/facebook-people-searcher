import string
import mouse


_SUPPORTED_ARGS = ('min_age', 'max_age', 'gender', 'country')


class PeopleSearcher:
    def __init__(self):
        self.letters = list(string.ascii_lowercase) + list('бвгдёжзийклмнпртуфхцчшщъыьэюя')
        self.letter_index = 0
    
    def __update_users_by_current_letter(self):
        self.letter_index += 1

    def __is_user_duplicate(self):
        pass

    def __is_suitable_user(self):
        pass

    def search_users(self, **args):
        if any([c not in _SUPPORTED_ARGS for c in args]):
            raise ValueError('these args are not supported')
