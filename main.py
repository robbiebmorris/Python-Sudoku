# Sodoku game!
# create your own sodoku boards, generate them automatically, and play!
import csv
import tkinter as tk


class Sudoku:

    # file_location:
    # data: 2D array of tuples, with (given, correct) values,
    def __init__(self, file_location="none", data=False):

        self.file_location = file_location
        self.data = data
        self.errors = 0

        if (self.data == False):
            self.data = self.import_csv()

        self.empty_board = self.create_empty_board(self.data)

        self.rules_window()

    # export the sodoku game to keep for later!
    # standard documentation-given code for writing using csv module in Python: found online
    def export_csv(self):
        file = open(self.file_location, 'w', newline='')
        csvwriter = csv.writer(file)
        for row in self.data:
            csvwriter.writerow(row)

    # 3bi: A program code segment which constains a list being used to manage complexity in the program
    # imports a prewritten sudoku game from a csv file
    def import_csv(self):
        file = open(self.file_location)
        csvreader = csv.reader(file)

        arr = []
        for row in csvreader:
            try:
                temp = []
                for tup in row:
                    temp.append(
                        tuple(map(int, tup.replace('(', '').replace(')', '').split(', '))))
                arr.append(temp)
            except:
                print("Error with this part of the CSV: " + str(row))
                arr.append(row)
        file.close()
        return arr

    # little function to import a new game from csv and create a new game window to play it!
    def import_game(self):
        self.data = self.import_csv()
        self.create_game()

    # function to create an empty baord containing only first value of tuples
    # input_arr: 2D array of tuples. e.x: [[(x, y), (x, y), (x, y)...], [(x, y), (x, y),...]...]
    def create_empty_board(self, input_arr):
        empty_board = []
        for i in range(len(input_arr)):
            temp = []
            for j in range(len(input_arr[i])):
                temp.append(input_arr[i][j][0])
            empty_board.append(temp)

        return empty_board

    # function to check if val1 is equal to val2 in a tuple
    # tup: standard tuple: (val1, val2)
    def check_space(self, tup):
        if (tup[0] == tup[1] or tup[1] == 0):
            return True
        return False

    # main game gui driver function: uses tkinter, and calls all the necessary functions to get the game running
    def create_game(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.spaces = []

        # create the empty text boxes of the tkinter grid
        for i in range(9):
            temp = []
            for j in range(9):

                if (self.data[i][j][1] == 0):
                    temp.append(tk.Text(self.window, height=1, width=2,
                                        font=("Arial bold", 25)))
                else:
                    temp.append(tk.Text(self.window, height=1, width=2,
                                        font=("Arial", 25)))
            self.spaces.append(temp)

        # insert values into the text boxes based on data array
        self.insert_values()

        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[row])):
                self.spaces[row][col].tag_add("tag", "1.0")
                self.spaces[row][col].grid(row=row, column=col)

        save_game = tk.Button(self.window, text="Export",
                              command=self.export_csv)
        import_game = tk.Button(
            self.window, text="Import", command=self.import_game)
        check_game = tk.Button(self.window, text="Done",
                               command=self.check_game)
        exit_game = tk.Button(self.window, text="Exit",
                              command=self.window.destroy)

        save_game.grid(row=9, column=3)
        import_game.grid(row=9, column=5)
        check_game.grid(row=9, column=4)
        exit_game.grid(row=10, column=4)

        self.window.mainloop()

    # shows the rules and introduces the game to the user!
    def rules_window(self):
        self.window = tk.Tk()
        self.window.geometry("550x290")

        rules_text = tk.Text(self.window, height=14,
                             width=200)
        rules_text.insert(
            'end', "Welcome to Sodoku!\n\nFill in the empty boxes according to traditional Sodoku rules--rows, columns and 3x3 squares must contain unique numbers!\n\nA variety of buttons can be found below the board:\nDone: use this to check if your solution is correct!\nIf correct, the space will turn green!\nIf not, the space will turn red.\nInput: Use this to import new sodoku games from a CSV file!\nExport: Export the current sodoku game to a CSV file!\nExit: Leave the game :(\n\nClick Start to begin!")
        rules_text.config(state='disabled')
        start_game = tk.Button(self.window, text="Start!",
                               command=self.create_game)

        rules_text.pack(pady=10, padx=20)
        start_game.pack(pady=2)

        self.window.mainloop()

    # inserts values into the previously created text boxes based on data array
    def insert_values(self):
        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[row])):
                if (self.data[row][col][0] == 0):
                    continue
                self.spaces[row][col].insert(
                    tk.END, str(self.data[row][col][0]))
                self.spaces[row][col].config(
                    state='disabled')

    # gets user input from a specified space in the active game board
    # row: int between 0-8
    # col: int between 0-8
    def get_space_input(self, row, col):
        return self.spaces[row][col].get("1.0", "end")

    # evaluates a singular space to check if the user has inputted the currect value
    # row: int between 0-8
    # col: int between 0-8
    def evaluate_space(self, row, col):
        if (self.get_space_input(row, col) == "\n"):
            self.errors += 1
            return

        # turns background of textbox gray if the answer is given
        elif (self.data[row][col][1] == 0):
            self.spaces[row][col].tag_config(
                "tag", background="gray")

        # turns background green if answer is correct
        elif (int(self.get_space_input(row, col)) == self.data[row][col][1]):
            self.spaces[row][col].tag_config(
                "tag", background="green")
        # turns background red if answer is incorrect
        else:
            self.spaces[row][col].tag_config("tag", background="red")
            self.errors += 1

    # iterates over the 2d array of the board and evaluates each space
    def check_game(self):
        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[row])):
                self.evaluate_space(row, col)

        # creates a pop up window to indicate to the user how they did

        pop_up = tk.Toplevel(self.window)
        pop_up.geometry("250x150")

        # if they solved the whole board correctly, indicate they have won!
        if (self.errors == 0):
            mistakes = tk.Label(
                pop_up, text="You completed the game with no mistakes!")
            win = tk.Label(pop_up, text="You win!")
            mistakes.pack(pady=20)
            win.pack(pady=10)
        # indicate to the user how many mistakes they made if board is incorrect
        else:
            mistakes = tk.Label(
                pop_up, text="You have " + str(self.errors) + " incorrect spaces.")
            win = tk.Label(pop_up, text="Try again.")
            mistakes.pack(pady=20)
            win.pack(pady=10)

        self.errors = 0


def main():

    # 0 in first part of tuple means empty space
    # 0 in second part of tuple means given uneditable number
    data = [[(0, 3), (5, 0), (2, 0), (0, 4), (0, 7), (6, 0), (0, 1), (0, 8), (0, 9)],
            [(1, 0), (6, 0), (0, 8), (9, 0), (0, 5),
             (0, 2), (0, 7), (0, 3), (4, 0)],
            [(0, 7), (4, 0), (9, 0), (8, 0), (0, 1),
             (3, 0), (6, 0), (2, 0), (0, 5)],
            [(4, 0), (0, 2), (0, 5), (0, 6), (0, 9),
             (0, 7), (8, 0), (0, 1), (0, 3)],
            [(0, 6), (8, 0), (3, 0), (2, 0), (0, 4),
             (1, 0), (5, 0), (9, 0), (0, 7)],
            [(0, 9), (0, 7), (1, 0), (0, 5), (0, 3),
             (0, 8), (0, 4), (0, 6), (2, 0)],
            [(0, 8), (9, 0), (7, 0), (3, 0), (0, 6),
             (5, 0), (2, 0), (4, 0), (0, 1)],
            [(2, 0), (0, 1), (0, 4), (0, 7), (0, 8),
             (9, 0), (0, 3), (5, 0), (6, 0)],
            [(0, 5), (0, 3), (0, 6), (1, 0), (0, 2), (0, 4), (9, 0), (7, 0), (0, 8)]]

    obj = Sudoku('data.csv')


if __name__ == "__main__":
    main()
