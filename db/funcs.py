import sqlite3
import re


def get_class_name_in_snake_case(cls):
	s = cls.__class__.__name__
	return '_'.join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1',
		s.replace('-', ' '))).split()).lower()

def is_all_models_exist(models: tuple):
	con = sqlite3.connect('./base.db')
	cur = con.cursor()
	names = ["'" + get_class_name_in_snake_case(m) + "'" for m in models]
	cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' \
AND name IN ({', '.join(names)})")
	is_exist = len(cur.fetchall()) == len(models)
	con.close()
	return is_exist
