import tkinter as tk
import datetime

class TICTACTOE(tk.Tk):
    def __init__(self):
        super().__init__()

        self.settings()
        self.statistics_labels()
        self.menu()
        self.start_new_game()

    def settings(self):
        self.title('Крестики-нолики')

        self.current_player = 'X'
        self.buttons = []
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def menu(self):
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

    def statistics_labels(self):
        self.player_1_label = tk.Label(self, text='Игрок X: 0')
        self.player_1_label.grid(row=0, column=0)

        self.player_2_label = tk.Label(self, text='Игрок O: 0')
        self.player_2_label.grid(row=0, column=1)

    def update_scores(self):
        player_1_score = self.get_player_score('X')
        player_2_score = self.get_player_score('O')

        self.player_1_label.config(text=f'Игрок X: {player_1_score}')
        self.player_2_label.config(text=f'Игрок O: {player_2_score}')

    def start_new_game(self):
        self.buttons.clear()
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        for row in range(3):
            button_row = list()
            for col in range(3):
                button = tk.Button(self, text='', width=10, height=4,
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row + 1, column=col, sticky='nsew')
                button_row.append(button)

            self.buttons.append(button_row)
            self.update_scores()

    def on_button_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win():
                self.disable_buttons()
            elif self.check_draw():
                self.disable_buttons()
            else:
                self.toggle_player()

    def toggle_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def highlight_winner(self, row1, col1, row2, col2, row3, col3):
        self.buttons[row1][col1].config(bg='green')
        self.buttons[row2][col2].config(bg='green')
        self.buttons[row3][col3].config(bg='green')

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] is not None:
                self.highlight_winner(
                    row1=i, col1=0,
                    row2=i, col2=1,
                    row3=i, col3=2,
                )

                winner = self.current_player
                self.write_results_to_file(player_1='X', player_2='O', winner=winner)

                return True

            elif self.board[0][i] == self.board[1][i] == self.board[2][i] is not None:
                self.highlight_winner(
                    row1=0, col1=i,
                    row2=1, col2=i,
                    row3=2, col3=i,
                )
                winner = self.current_player
                self.write_results_to_file(player_1='X', player_2='O', winner=winner)
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:
            self.highlight_winner(
                    row1=0, col1=0,
                    row2=1, col2=1,
                    row3=2, col3=2,
            )
            winner = self.current_player
            self.write_results_to_file(player_1='X', player_2='O', winner=winner)
            return True

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            self.highlight_winner(
                    row1=0, col1=2,
                    row2=1, col2=1,
                    row3=2, col3=0,
            )
            winner = self.current_player
            self.write_results_to_file(player_1='X', player_2='O', winner=winner)
            return True

    def write_results_to_file(self, player_1, player_2, winner):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        with open('results.txt', 'a', encoding='utf-8') as file:
            file.write(f'{current_time} {player_1} vs {player_2} Победил: {winner}\n')

        self.update_scores()

    @staticmethod
    def get_player_score(player_name):
        with open('results.txt', 'r', encoding='utf-8') as file:
            player_wins = 0
            for line in file:
                if f'Победил {player_name}' in line:
                    player_wins += 1
            return player_wins


if __name__ == '__main__':
    app = TICTACTOE()
    app.mainloop()
