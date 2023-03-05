"""
Copyright (C) 2022-2023 Simon Ma <https://github.com/Simuschlatz> - All Rights Reserved. 
You may use, distribute and modify this code under the terms of the GNU General Public License
"""
def main():
    play_as_red = True
    red_moves_first = True
    fen = INITIAL_FEN_RED_DOWN if play_as_red else INITIAL_FEN_BLACK_DOWN 
    fen += (" w " if red_moves_first else " b ") + "- - 0 1"
    Clock.init(600)
    # If you play as red, red pieces are gonna be at the bottom, else they're at the top
    board = Board(fen, play_as_red)
    # Set up move generator
    LegalMoveGenerator.init_board(board)
    LegalMoveGenerator.load_moves()

    # m = CNN()
    # m.load_checkpoint()
    # sp = SelfPlay(m, board)
    # sp.load_training_data()
    # sp.train()
    
    # ------To run perft search------
    start_search(board)
    # -------------------------------#

    if len(sys.argv) > 1:
        agent = sys.argv[1]
    else: agent = "ab"

    if agent not in {"ab", "az", "abz"}:
        logger.error(f"Unknown agent '{agent}'. Selected Agent must be in 'ab', 'az', 'abz'.")
        logger.info("Using Alpha-Beta agent as default.")
        agent = "ab"
    logger.info(f"You selected agent '{agent}'.")

    ui = UI(board, agent=agent)
    ui.run()


if __name__ == "__main__":
    import pygame
    pygame.init()
    import sys
    from core.engine import Board, LegalMoveGenerator, Clock
    from core.engine.UI import UI
    from core.utils import start_search
    from core.engine.AI.AlphaZero import CNN, MCTS, SelfPlay
    from core.visualizations.move_ordering_analysis import run_benchmarks
    import logging
    logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(__name__)

    INITIAL_FEN_BLACK_DOWN = "RHEAKAEHR/9/1C5C/P1P1P1P1P/9/9/p1p1p1p1p/1c5c/9/rheakaehr"
    INITIAL_FEN_RED_DOWN = "rheakaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAKAEHR"
    main()
