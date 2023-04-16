class PieceSquareTable:
    """
    Piece-Square Tables are a simple way to assign values to specific pieces on specific squares.
    """
    piece_square_tables = [
        [ # Empty square
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
        ],
        [ # Elephant
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0, 25,  0,  0,  0, 25,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              20,  0,  0,  0, 35,  0,  0,  0, 20,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  30, 0,  0,  0, 30,  0,  0,
        ],
        [ # Advisor
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0, 25,  0, 25,  0,  0,  0,
              0,  0,  0,  0, 35,  0,  0,  0,  0,
              0,  0,  0, 25,  0, 25,  0,  0,  0,
        ],
        [ # Cannon
            100,100, 96, 91, 90, 91, 96,100,100,
             98, 98, 96, 92, 89, 92, 96, 98, 98,
             97, 97, 96, 91, 92, 91, 96, 97, 97,
             96, 99, 99, 98,100, 98, 99, 99, 96,
             96, 96, 96, 96,100, 96, 96, 96, 96,
             95, 96, 99, 96,100, 96, 99, 96, 95,
             96, 96, 96, 96, 96, 96, 96, 96, 96,
             97, 96,100, 99,101, 99,100, 96, 97,
             96, 97, 98, 98, 98, 98, 98, 97, 96,
             96, 96, 97, 99, 99, 99, 97, 96, 96,
        ],
        [ # Pawn
              9,  9,  9, 11, 13, 11,  9,  9,  9,
             19, 24, 34, 42, 44, 42, 34, 24, 19,
             19, 24, 32, 37, 37, 37, 32, 24, 19,
             19, 23, 27, 29, 30, 29, 27, 23, 19,
             14, 18, 20, 27, 29, 27, 20, 18, 14,
              7,  0, 13,  0, 16,  0, 13,  0,  7,
              7,  0,  7,  0, 15,  0,  7,  0,  7,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,  0,
        ],
        [ # Rook
            206,208,207,213,214,213,207,208,206,
            206,212,209,216,233,216,209,212,206,
            206,208,207,214,216,214,207,208,206,
            206,213,213,216,216,216,213,213,206,
            208,211,211,214,215,214,211,211,208,
            208,212,212,214,215,214,212,212,208,
            204,209,204,212,214,212,204,209,204,
            198,208,204,212,212,212,204,208,198,
            200,208,206,212,200,212,206,208,200,
            194,206,204,212,200,212,204,206,194,
        ],
        [ # Horse
             90, 90, 90, 96, 90, 96, 90, 90, 90,
             90, 96,103, 97, 94, 97,103, 96, 90,
             92, 98, 99,103, 99,103, 99, 98, 92,
             93,108,100,107,100,107,100,108, 93,
             90,100, 99,103,104,103, 99,100, 90,
             90, 98,101,102,103,102,101, 98, 90,
             92, 94, 98, 95, 98, 95, 98, 94, 92,
             93, 92, 94, 95, 92, 95, 94, 92, 93,
             85, 90, 92, 93, 78, 93, 92, 90, 85,
             88, 85, 90, 88, 90, 88, 90, 85, 88,
        ],
    ]
    max_value = 233 # Rook index 13

    @classmethod
    def get_pst_value(cls, piece_type, square, moving_side):
        """
        :return: Piece-square-table value of piece type on square relative
        to moving side's perspective
        """
        # The psts are viewed from below, meaning that the top-left corner of the pst would be the bottom right 
        # corner for the top-side player. This means we have to flip the board if top-side player is moving
        if not moving_side:
            # Tables are vertically symmetrical, so don't mirror square index along y-axis
            file = square % 9
            # flip the square index along x-axis
            rank = 9 - square // 9
            square = rank * 9 + file
        return cls.piece_square_tables[piece_type][square]