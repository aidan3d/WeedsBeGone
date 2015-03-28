# The Board class tracks where
# the mouse is clicked on screen.

import cell

class Board:

    # The __init__ method sets up
    # the board's size and cell
    # population.

    def __init__(self, width, height, num_cells_wide,
                 num_cells_high, x_origin, y_origin):

        # Create an attribute to refer
        # to the board's width.
        self._width = width

        # Create an attribute to refer
        # to the board's height.
        self._height = height

        # Set the x-ordinate of the
        # board's origin in the game
        # window.
        self._x_origin = x_origin

        # Set they y-ordinate of the
        # board's origin in the game
        # window.
        self._y_origin = y_origin

        self._num_cells_wide = num_cells_wide

        self._num_cells_high = num_cells_high

        # Set the number of cells
        # the board has horizontally.
        self._cell_width = self._width / self._num_cells_wide

        # Set the number of cells
        # the board has vertically.
        self._cell_height = self._height / self._num_cells_high

        # Create an interal list cells,
        # each has an _id attribute referencing
        # the element's subscript referenced by
        # the _cells sequence variable.
        self._cells = self._create_cell_list()

        # Initialize the 'center' coordinates
        # for all cells
        self._initialize_cell_centers()

    # The identify_cell method/
    # returns the cell id:
    # 0 through (self.num_cells_wide *
    # self._num_cells_high)
    # (i.e. 0 through 15 for a
    #4 x 4 game board.

    def identify_cell(self, x, y):

        # Create a variable to act
        # as a 'signal flag,' raised
        # when the correct cell has
        # been identified.
        found = False

        # Create and initialize a
        # variable to refer
        # to the cell identifier
        # ( 0 - 16 for a 4 x 4 board)
        cell_id = 0

        # The outer loop traverses
        # the rows
        for row in range(self._num_cells_high):
            
            # Break out of the outer for loop
            # if the correct cell has already
            # been identified.
            if found:
                break

            else:

                # The inner loop runs traverses
                # the columns
                for column in range(self._num_cells_wide):


                    if y >= self._y_origin + (self._cell_height * row) and y < self._y_origin + self._cell_height + (self._cell_height * row):

                        # Run through each column in the current row.
                        if x >= self._x_origin + (self._cell_width * column) and x < self._x_origin + self._cell_width + (self._cell_width * column):    

                            # Programmer's stub - will be removed
                            # at run time.
                            print('Garden parcel: [', column+1, ', ', row+1, ']', sep='')

                            # Set the position identifier.
                            cell_id = column + (row * self._num_cells_wide)

                            # Raise the 'found' flag
                            found = True

                            # break out of the
                            # inner for loop
                            break

        return cell_id

    # The method _create_cells create an
    # internal list of Cell objects
    # (one to represent each position
    # on the game board).

    def _create_cell_list(self):

        # Create a sequence variable
        # to hold the cells on the
        # game board.
        cells = list()

        # Run through the entire board,
        # creating a reference to a 'bucket'
        # for each of the board's positions
        # (0 - 15 for a 4 x 4 board).
        for index in range(self._num_cells_wide * self._num_cells_high):

            # Create a Cell object to
            # reference the value 'contained'
            # in each position on the board.
            cells.append(cell.Cell(index))

        return cells


    # The get_cell_width method returns
    # the typical cell width value.

    def get_cell_width(self):
        return self._cell_width

    # The get_cell_height method returns
    # the typical cell height value.

    def get_cell_height(self):
        return self._cell_height

    # The get_cell_value method return
    # a specific cell's value by index.

    def get_cell_value(self, index):

        # Retrive the value referenced
        # by the cell at the location
        # on the board referenced by
        # index.
        current_value = self._cells[index].get_value()

        return current_value
    
    # The function cell_position sets
    # the cell's center coordinates for
    # all cells on the board
    def _initialize_cell_centers(self):

        # Initialize the counter for the
        # while loop traversing throught
        # the list _cells ( a post-text
        # repetition structure)
        index = 0

        # Run through all cells on the board
        # (0-19 for a 5 x 4 board)
        while index < self._num_cells_wide * self._num_cells_high:

            # First run through the rows
            for row in range(self._num_cells_high):

                # Then run through each column
                # for each row.
                for column in range(self._num_cells_wide):

                    self._cells[index].set_x_center(
                        self._x_origin +
                        (0.5 * self._cell_width) +
                        (self._cell_width * column)
                    )

                    self._cells[index].set_y_center(
                        self._y_origin +
                        (0.5 * self._cell_height) +
                        (self._cell_height * row)
                    )

                    # Move the cell traverser to the
                    # next 'slot' in the _cells list.
                    index += 1

    # Get a specific cell / 'spot on the board'
    # by accepting the elements subscript
    # as an argument.
    def get_cell_by_index(self, index):
        return self._cells[index]
