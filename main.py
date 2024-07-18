from config import *
from searcher import PeopleSearcher
from db.models import (BrowserElementPositions, SearchCriteria, SidePosition,
    ElementPositions)
from positions import save_side_position, save_element_positions


def set_criteria(name: str, msg: str):
    criteria = SearchCriteria.get_or_create(name=name)[0]
    value = input(f'{msg} > ')
    if len(value) != 0:
        criteria.value = value
        criteria.save()


def set_button_positions(name: str):
    input(f'Put your cursor in the center of the Facebook`s \
"{name[0].upper()}{name[1:]}" button > ')
    save_element_positions(ElementPositions, name)


if __name__ == "__main__":
    if len(BrowserElementPositions.select()) == 0:
        input('Put your cursor on the address bar in your browser > ')
        save_element_positions(BrowserElementPositions, 'address_bar')
        input('Put your cursor on the back to previous web page button in your \
browser > ')
        save_element_positions(BrowserElementPositions, 'back')
    
    while True:
        answer = input('Do you want to set/change search criteria? (y/n) > ')
        if answer == 'y':
            print('Note: For these criteria will be used values which will appear \
first in the Facebook`s input of criteria.')
            print('Hint: Leave blank answers for criteria to do not set values.')
            set_criteria('friends', 'Which friends must have people you \
searching (my friends/friends of friends/{exact full name of \
your friend})')
            set_criteria('city', 'In which city you want to search people \
({city name}, {country name})')
            set_criteria('education', 'Exact name of educational institution \
in which people you searching were learned')
            set_criteria('work', 'Exact company name in which work people you searching')
            break
        elif answer == 'n':
            if len(SearchCriteria.select()) == 0:
                [SearchCriteria.create(name=name) for name in SEARCH_CRITERIA]
            break

    input('Open following link from browser in which you are logged in to your \
Facebook account - https://www.facebook.com/search/people/?q=a > ')

    if len(SidePosition.select()) == 0:
        input('Put your cursor on the up side of the Facebook website in tab with \
opened link in your browser > ')
        save_side_position('upper')
        input('Put your cursor on the down side of the same Facebook website page > ')
        save_side_position('bottom')
    
    args = args_parser.parse_args()
    searcher = PeopleSearcher()

    if len(ElementPositions.select()) == 0:
        input('Put your cursor on the center of the Facebook`s search input > ')
        save_element_positions(ElementPositions, 'search')
        [set_button_positions(name) for name in (
            'people', 'friends', 'city', 'education', 'work')]
        input('Put your cursor on the name of the first person who appeared in \
the Facebook`s search result > ')
        save_element_positions(ElementPositions, 'person_name')


        # open first user page and save user data elements positions like in previous block of code
        searcher.click_elem(ElementPositions, 'person_name')
        user_page_url = searcher.get_current_url()

        # save positions of elements in the user page for args

    users = searcher.search_users(**args)
    # print(users)
