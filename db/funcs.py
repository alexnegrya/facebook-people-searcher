import sqlite3
from models import ALL_MODELS


def is_all_models_exist(*models_names: tuple[str]):
	con =sqlite3.connect('base.db')
	cur = con.cursor()
	names = ["'" + name + "'" for name in models_names]
	cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' \
		AND name IN ({', '.join(names)})")
	is_exist = len(cur.fetchall()) == len(models_names)
	con.close()
	return is_exist
