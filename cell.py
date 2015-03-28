# The Cell class holds a cell's value
# and is labeled by the value referenced
# by id (element's position in a list
# of all cells on the board). A cell is
# akin to a square on a Chess board.

import random

class Cell:

    # The _alive Boolean attribute is initialized
    # to False, the cell's id number is initialized
    # at zero, and the value referenced by the
    # cell is initialized to zero.
    def __init__(self, id):

        # Set up the alive/dead status
        # for the Cell object (once 'hit'
        # by the user it is considered
        # 'dead' and un-'hittable')
        #
        # All cells start out as happy
        # cells and are alive 'til hit!
        self._alive = True
        
        # Set up the flagged/unflagged
        # status for the Cell object
        # (incorrect hit (i.e. player
        # picked this cell and exceeded
        # the target weed count))
        self._flag = False

        # Set up the id number for the
        # Cell object.
        self._id = id

        # The x-ordinate of the Cell
        # object's center.
        self._x_center = 0

        # The y-ordinate of the Cell
        # object's center.
        self._y_center = 0

        # The number reference by the
        # Cell object.
        self._value = random.randint(0, 6)

    # The kill method sets the
    # value referenced by the
    # effectively Boolean attibute
    # _alive to False.

    def kill(self):
        self._alive = False
    
    # The flag method sets
    # the value referenced by
    # the effectively Boolean
    # attribute _flag to
    # True.
    def flag(self):
        self._flag = True

    # The set_id method sets the
    # cell's id number.

    def set_id(self, id):
        self._id = id

    # The set_x_center method sets
    # the _x_center attribute
    
    def set_x_center(self, x):
        self._x_center = x

    # The set_y_center method sets
    # the _y_center attribute.

    def set_y_center(self, y):
        self._y_center = y

    # The set_value method sets the
    # cell's value.

    def set_value(self, value):
        self._value = value

    # The is_alive method returns
    # the Boolean value True if
    # the cell is 'hittable'

    def is_alive(self):
        # Create and initialize a
        # 'signal flag,' raised
        # if the cell is 'hittable.'
        # *** State adjustor.
        status = False

        # Check the Boolean value
        # referenced by the _alive
        # attribute.
        if self._alive == True:
            status = True
        else:
            status = False

        return status

    # The is_flagged method
    # returns the Boolean
    # value True if the flag
    # has been incorrectly hit
    # previously. 
    # *** State adjustor.

    def is_flagged(self):
        # Create and initialize a
        # 'singal flag,' raised
        # if the flag is 'hittable'
        # on the basis of having
        # been mis-hit (would have
        # caused a 'weed count'
        # overage) previously.
        status = False

        # Check the Boolean value
        # reference by the _flag
        # attribute.
        if self._flag == True:
            status = True
        else:
            status = False

        return status

    # The get_id method returns
    # the value of the cell's
    # id_number attribute.

    def get_id(self):
        return self._id

    # The get_x_center method returns
    # the value referenced by the
    # attribute _x_center

    def get_x_center(self):
        return self._x_center

    # The get_y_center method returns
    # the value referenced by the
    # attribute _y_center

    def get_y_center(self):
        return self._y_center

    # The get_value method returns
    # the value referenced by the
    # cell.

    def get_value(self):
        return self._value
