"""
Suppose you have some rectangle-shaped pieces of furniture, all the same height.
You want to build a larger rectangular table out of them by assembling them next
to one another into a tight grid, while minimizing any interior holes.

For example, suppose you have two 2' x 5' pieces L and two 2' x 2' pieces S.
You could form a nearly square structure as follows:

    LLLLL
    LLLLL
    SS SS
    SS SS
    LLLLL
    LLLLL

which forms a 5x6 structure with a single 1x2 interior hole. Such holes are OK
because you will cover the entire table area with a single cut-to-size tabletop
piece. But you would prefer to have no exterior holes -- i.e. you need an
unbroken perimeter around the outside edges of the final rectangular table.

Alternately, with the same pieces, you could form a very long skinny table:

    LLLLLSSLLLLLSS
    LLLLLSSLLLLLSS

This one has no interior holes, and an area of 14x2 = 28 sq ft.

When making the best structure, your top priority is to maximize the table
area, while maintaining an unbroken perimeter. So in the example above, the
first solution is better at 5x6 = 30 sq ft. However, if multiple structures
have the same area, the one with the least internal area missing is best.

You do not have to use all the available pieces of furniture.
"""


from typing import List, Optional, Tuple


class Piece:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h

class Table:
    def __init__(self, w: int, h: int):
        self.w: int = w
        self.h: int = h
        self.grid: List[List[Optional[int]]] = []
        for col in range(w):
            self.grid.append([None] * h)

    def add(self, piece: Piece, code: int, px: int, py: int) -> Optional["Table"]:
        """
        Place a piece at a particular location.

        :param piece: The piece to place.
        :param code: Integer code to use on the table.
        :param px: X coordinate of location to place.
        :param py: Y coordinate of location to place.
        :return: New table with the piece added, or None if it does not fit.
        """

        # Validate piece placement.
        if px + piece.w > self.w or py + piece.h > self.h:
            return None
        for x in range(px, px + piece.w):
            for y in range(py, py + piece.h):
                if self.grid[x][y] is not None:
                    return None

        # Actually place the piece.
        table = self.copy()
        for x in range(px, px + piece.w):
            for y in range(py, py + piece.h):
                table.grid[x][y] = code

        return table

    def copy(self) -> "Table":
        """
        Make a copy of the current table.
        """
        table = Table(self.w, self.h)
        for x in range(table.w):
            for y in range(table.h):
                table.grid[x][y] = self.grid[x][y]
        return table

    def max_code(self) -> int:
        return max(
            max(
                0 if cell is None else cell
                for cell in col
            )
            for col in table.grid
        )

    def score(self) -> Tuple[int, int]:
        """
        A table's score has two components:

        1) total rectangular area, and
        2) internally missing area.

        Tables that are not well-formed rectangles have a score of (0, 0).
        """

        # Find rectangle bounds.
        x_min = None
        x_max = None
        y_min = None
        y_max = None
        for x in range(self.w):
            for y in range(self.h):
                if self.grid[x][y] is not None:
                    if x_min is None or x < x_min: x_min = x
                    if x_max is None or x > x_max: x_max = x
                    if y_min is None or y < y_min: y_min = y
                    if y_max is None or y > y_max: y_max = y

        if x_min is None or x_max is None or y_min is None or y_max is None:
            # Only happens when table is completely empty.
            return (0, 0)

        # Compute rectangle integrity.
        exterior_missing = 0
        if self.grid[x_min][y_min] is None: exterior_missing += 1  # Top-left corner.
        if self.grid[x_max][y_min] is None: exterior_missing += 1  # Top-right corner.
        if self.grid[x_min][y_max] is None: exterior_missing += 1  # Bottom-left corner.
        if self.grid[x_max][y_max] is None: exterior_missing += 1  # Bottom-right corner.
        for x in range(x_min + 1, x_max):
            if self.grid[x][y_min] is None: exterior_missing += 1  # Top edge.
            if self.grid[x][y_max] is None: exterior_missing += 1  # Bottom edge.
        for y in range(y_min + 1, y_max):
            if self.grid[x_min][y] is None: exterior_missing += 1  # Left edge.
            if self.grid[x_max][y] is None: exterior_missing += 1  # Right edge.

        #if exterior_missing > 0: return (0, 0)  # Enclosed rectangles only!

        # Count interior holes.
        interior_missing = 0
        for x in range(x_min + 1, x_max):
            for y in range(y_min + 1, y_max):
                if self.grid[x][y] is None:
                    interior_missing += 1

        # Compute area.
        width = x_max - x_min + 1
        height = y_max - y_min + 1
        squareness = min(width, height) / max(width, height)
        area = squareness**0.5 * width * height - (exterior_missing + interior_missing)**3

        return (area, interior_missing)


    def show(self) -> None:
        """
        Print an ASCII representation of the table.
        """
        cell_width = len(str(self.max_code())) + 1
        for y in range(self.h):
            for x in range(self.w):
                v = "_" * cell_width if self.grid[x][y] is None else f"{self.grid[x][y]:{cell_width}}"
                print(v, end="")
            print()


def solve(table: Table, pieces: List[Piece]):
    solution = table

    if len(pieces) == 0:
        return solution

    # Try to slot in the first piece anywhere it fits.
    code = len(pieces)
    piece = pieces.pop()
    for x in range(table.w):
        for y in range(table.h):
            new_table = table.add(piece, code, x, y)
            if new_table is None: continue  # Does not fit.
            #new_table.show()
            best = solve(new_table, pieces)
            if best.score() > solution.score():
                print(f"Found better solution: {solution.score()} -> {best.score()}")
                solution = best

    # Try also without slotting in the current piece,
    # in case that ends up with a better configuration.
    best = solve(table, pieces)
    if best.score() > solution.score():
        solution = best

    return solution


cabinet_drawer_1 = Piece(18, 25)
cabinet_drawer_2 = Piece(18, 25)
cube_shelf_3x3 = Piece(12, 36)
cube_shelf_1x3_1 = Piece(12, 12)
cube_shelf_1x3_2 = Piece(12, 12)
cube_shelf_1x3_3 = Piece(12, 12)
workshop_drawers = Piece(75, 22)
workshop_table = Piece(24, 36)

pieces = [
    cabinet_drawer_1,
    cabinet_drawer_2,
    cube_shelf_3x3,
    cube_shelf_1x3_1,
    cube_shelf_1x3_2,
    cube_shelf_1x3_3,
#    workshop_drawers,
    workshop_table,
]

table = Table(75, 75)

print("Solving...")
solution = solve(table, pieces)
print("Got it!")
solution.show()
