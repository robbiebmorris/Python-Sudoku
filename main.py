# Sodoku game!
# create your own sodoku boards, generate them automatically, and play!
import csv
import tkinter as tk
import time


class Sudoku:

    # file_location:
    # data: 2D array of tuples, with (given, correct) values
    def __init__(self, file_location="none", data=False):
        self.file_location = file_location
        self.data = data
        if (self.data == False):
            self.data = self.import_csv()
        self.errors = 0

        self.spaces = []
        self.empty_board = self.create_empty_board(self.data)
        self.create_window()

    # could add a "create sodoku" function to create random games!
    # printing it to csv to save a nice board, wordle style

    def create_csv(self):
        file = open(self.file_location, 'w', newline='')
        csvwriter = csv.writer(file)
        for row in self.data:
            csvwriter.writerow(row)

    # 3bi
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

    def set_data(self, data):
        self.data = data

    # input_arr
    def create_empty_board(self, input_arr):
        empty_board = []
        for i in range(len(input_arr)):
            temp = []
            for j in range(len(input_arr[i])):
                temp.append(input_arr[i][j][0])
            empty_board.append(temp)

        return empty_board

    def check_space(self, tup):
        if (tup[0] == tup[1] or tup[1] == 0):
            return True
        return False

    def update_space(self, new):
        return True

    def get_empty_board(self):
        return self.empty_board

    # gui stuff!

    def create_window(self):
        self.window = tk.Tk()

        # create the empty text boxes of grid
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
                              command=self.create_csv)
        import_game = tk.Button(
            self.window, text="Import", command=self.import_csv)
        check_game = tk.Button(self.window, text="Done",
                               command=self.check_game)
        exit_game = tk.Button(self.window, text="Exit",
                              command=self.window.destroy)

        save_game.grid(row=9, column=3)
        import_game.grid(row=9, column=5)
        check_game.grid(row=9, column=4)
        exit_game.grid(row=10, column=4)

        self.window.mainloop()

    def insert_values(self):
        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[row])):
                # if ((row == 3 or 4 or 5) and (col == 0 or 1 or 2 or 6 or 7 or 8)):
                #     self.spaces[row][col].tag_config("tag", background="gray")

                if (self.data[row][col][0] == 0):
                    continue
                self.spaces[row][col].insert(
                    tk.END, str(self.data[row][col][0]))
                self.spaces[row][col].config(
                    state='disabled')

    def get_space_input(self, row, col):
        return self.spaces[row][col].get("1.0", "end")

    def evaluate_space(self, row, col):
        if (self.get_space_input(row, col) == "\n"):
            self.errors += 1
            return

        elif (self.data[row][col][1] == 0):
            self.spaces[row][col].tag_config(
                "tag", background="gray")

        elif (int(self.get_space_input(row, col)) == self.data[row][col][1]):
            self.spaces[row][col].tag_config(
                "tag", background="green")
        else:
            self.spaces[row][col].tag_config("tag", background="red")
            self.errors += 1

    def check_game(self):
        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[row])):
                self.evaluate_space(row, col)

        pop_up = tk.Toplevel(self.window)
        pop_up.geometry("250x170")

        if (self.errors == 0):
            mistakes = tk.Label(pop_up, text="You have 0 incorrect spaces!")
            win = tk.Label(pop_up, text="You win!")
            mistakes.pack(pady=20)
            win.pack(pady=20)
        else:
            mistakes = tk.Label(
                pop_up, text="You have " + str(self.errors) + " incorrect spaces.")
            win = tk.Label(pop_up, text="Try again")
            mistakes.pack(pady=20)
            win.pack(pady=20)

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

    obj.create_csv()
    # csv = obj.import_csv()

    # print(obj.get_empty_board())


if __name__ == "__main__":
    main()
