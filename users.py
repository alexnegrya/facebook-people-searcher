class User:
    def __init__(self, url: str, full_name: str, age: int, gender: str, country: str, possible_duplicate=False):
        self.url = url
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.country = country
        
        self.possible_duplicate = possible_duplicate

    def __str__(self):
        pass

    def __repr__(self):
        return self.__str__()
