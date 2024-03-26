from peewee import *
from funcs import is_all_models_exist


_DB = SqliteDatabase('base.db')


class _BaseModel(Model):
    class Meta:
        database = _DB
        legacy_table_names = False


class BrowserElementPositions(_BaseModel):
    name = CharField(unique=True, null=False)
    x_pos = IntegerField(null=True, constraints=[Check('x_pos >= 0')])
    y_pos = IntegerField(null=True, constraints=[Check('y_pos >= 0')])


class SidePosition(_BaseModel):
    name = CharField(unique=True, null=False)
    y_pos = IntegerField(null=True, constraints=[Check('y_pos >= 0')])


class ElementPositions(_BaseModel):
    name = CharField(unique=True, null=False)
    x_pos = IntegerField(null=True, constraints=[Check('x_pos >= 0')])
    y_pos = IntegerField(null=True, constraints=[Check('y_pos >= 0')])


class SearchCriteria(_BaseModel):
    name = CharField(unique=True, null=False)
    value = CharField(null=True)


ALL_MODELS = (BrowserElementPositions, SidePosition, ElementPositions, SearchCriteria)


_models_existance_checked = False
if not _models_existance_checked:
    if not is_all_models_exist('side_positions', 'element_position'):
        with _DB.connect():
            _DB.create_tables(ALL_MODELS)
    _models_existance_checked = True
