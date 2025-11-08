from .circle import area as circle_area, perimeter as circle_perimeter
from .rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from .square import area as square_area, perimeter as square_perimeter
from .triangle import area as triangle_area, perimeter as triangle_perimeter

__all__ = [
    "circle_area", "circle_perimeter",
    "rectangle_area", "rectangle_perimeter",
    "square_area", "square_perimeter",
    "triangle_area", "triangle_perimeter",
]

__version__ = "0.1.0"