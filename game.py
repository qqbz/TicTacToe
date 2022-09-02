import settings
import ai_opponent
import sys
import cell


class Game:

    def __init__(self, frame, difficulty_level):
        self.cells = []
        self.current_turn = settings.PLAYER1_SIGN
        if not settings.TWO_PLAYER_MODE:
            self.ai_opponent = ai_opponent.AiOpponent(difficulty_level)
        for x in range(3):
            for y in range(3):
                one_cell = cell.Cell(x, y, self)
                one_cell.create_connected_button(frame)
                self.cells.append(one_cell)

    def cell_clicked(self, cell):
        pass

    def unplayed_cells(self):
        cells = [cell for cell in self.cells if cell.cell_played is False]
        return cells

    def end_players_turn(self):
        self.change_player()
        if not settings.TWO_PLAYER_MODE:
            ai_cell = self.ai_opponent.choose_cell(self.unplayed_cells())
            ai_cell.mark_as_played(self.current_turn)
            self.check_game_end()
            self.change_player()

    def change_player(self):
        if self.current_turn == settings.PLAYER1_SIGN:
            self.current_turn = settings.PLAYER2_SIGN
        else:
            self.current_turn = settings.PLAYER1_SIGN

    def check_game_end(self):
        winner = self.check_winner()
        if winner is not None:
            if settings.TWO_PLAYER_MODE:
                print(f"Player {winner} won!")
            elif winner == settings.PLAYER1_SIGN:
                print("You won!")
            else:
                print("You lost!")
            # TODO: show proper message and delete print statement
            sys.exit()
        stalemate = self.check_stalement()
        if stalemate:
            print("We have a stalemate.")
            sys.exit()

    def check_winner(self):
        if (self.cells[0].text == self.cells[1].text == self.cells[2].text == self.current_turn) or \
                (self.cells[0].text == self.cells[3].text == self.cells[6].text == self.current_turn) or \
                (self.cells[8].text == self.cells[7].text == self.cells[6].text == self.current_turn) or \
                (self.cells[8].text == self.cells[5].text == self.cells[2].text == self.current_turn) or \
                (self.cells[1].text == self.cells[4].text == self.cells[7].text == self.current_turn) or \
                (self.cells[3].text == self.cells[4].text == self.cells[5].text == self.current_turn) or \
                (self.cells[0].text == self.cells[4].text == self.cells[8].text == self.current_turn) or \
                (self.cells[2].text == self.cells[4].text == self.cells[6].text == self.current_turn):
            return self.current_turn

    def check_stalement(self):
        available_cells = self.unplayed_cells()
        if len(available_cells) == 0:
            return True
        return False
