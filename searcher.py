import string
import mouse
from db.models import BrowserElementPositions, ElementPositions, SearchCriteria
from pyautogui import press as press_keys
import pyperclip
from config import SEARCH_CRITERIA
from users import User


_SUPPORTED_ARGS = ('min_age', 'max_age', 'gender', 'country')


class PeopleSearcher:
    def __init__(self):
        self.letters = list(string.ascii_lowercase) + list('бвгдёжзийклмнпртуфхцчшщъыьэюя')
        self.letter_index = 0
        self.previous_user_url = None

    def __click_elem(self, model, name: str):
        elem = model.get(name=name)
        mouse.move(elem.x_pos, elem.y_pos)
        mouse.press()

    def __enter_text(self, text: str, with_choices=True):
        text_spl = text.split()
        for char in text_spl:
            if char.isupper():
                press_keys(('shift', char))
            elif char.isspace():
                press_keys('backspace')
            else:
                press_keys(char)
        if with_choices:
            press_keys('down')
        press_keys('enter')

    def __set_criteria(self):
        criteria = {m.name: m.value for m in [
            SearchCriteria.get(name=name) for name in SEARCH_CRITERIA]}
        if any([v is not None for v in criteria.values()]):
            self.__click_elem(ElementPositions, 'people')
            if criteria['friends']:
                self.__click_elem(ElementPositions, 'friends')
                if criteria['friends'] == 'my friends':
                    press_keys('down', 2)
                elif criteria['friends'] == 'friends of friends':
                    press_keys('down', 3)
                else:
                    self.__enter_text(criteria['friends'])
            for c in SEARCH_CRITERIA[1:]:
                if c:
                    self.__click_elem(ElementPositions, c)
                    self.__enter_text(criteria[c])
    
    def __update_users_by_current_letter(self):
        # search users by current letter
        self.letter_index += 1

    def __get_user_url(self):
        self.__click_elem(BrowserElementPositions, 'address_bar')
        press_keys(('ctrl', 'c'))
        return pyperclip.paste()

    def __scroll_results_list(self):
        pass
    
    def __get_user_age(self):
        pass

    def __get_user_gender(self):
        pass

    def __get_user_country(self):
        pass

    def __is_suitable_user(self, args: dict[str, str], age, gender, country):
        pass

    def __is_user_possible_duplicate(self, args: dict[str, str], age, gender, country):
        pass

    def search_users(self, **args):
        if any([c not in _SUPPORTED_ARGS for c in args]):
            raise ValueError('these args are not supported')
        is_first_func_iteration = True
        users = []
        while self.letter_index < len(self.letters):
            # get all by current letter
            self.__set_criteria()
            if not is_first_func_iteration:
                self.__update_users_by_current_letter()
            while True:
                # work with users one by one
                url = self.__get_user_url()
                if url != self.previous_user_url:
                    self.__click_elem(ElementPositions, 'person_name')
                    age = self.__get_user_age()
                    gender = self.__get_user_gender()
                    country = self.__get_user_country()
                    if self.__is_suitable_user(args, age, gender, country):
                        pass
                    if self.__is_user_possible_duplicate(args, age, gender, country):
                        pass
                else:
                    pass
