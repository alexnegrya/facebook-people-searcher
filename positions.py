import mouse
from db.models import SidePosition, ElementPositions
from peewee import Model


def save_side_position(side_name: str):
    side_pos = SidePosition.get_or_create(name=side_name)[0]
    side_pos.y_pos = mouse.get_position()[1]
    side_pos.save()

def save_element_positions(model: Model, elem_name: str):
    elem_positions = model.get_or_create(name=elem_name)[0]
    elem_positions.x_pos, elem_positions.y_pos = mouse.get_position()
    elem_positions.save()
