# Sodoku game!
# create your own sodoku boards, generate them automatically, and play!
import csv
import tkinter as tk


class Sudoku:

    # file_location:
    # data: 2D array of tuples, with (given, correct) values
    def __init__(self, file_location="none", data=False):
        self.file_location = file_location
        self.data = data
        if (self.data == False):
            self.data = self.import_csv()

        self.spaces = []
        self.empty_board = self.create_empty_board(self.data)
        self.create_window()

    # could add a "create sodoku" function to create random games!
    # printing it to csv to save a nice board, wordle style

    def create_csv(self):
        file = open(self.file_location, 'w')
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
                print(temp)
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
        window = tk.Tk()

        # create the empty text boxes of grid

        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(tk.Text(window, height=1, width=2,
                            font=("Arial", 25)))
            self.spaces.append(temp)

        # insert values into the text boxes based on data array
        self.insert_values()

        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[row])):
                self.spaces[row][col].grid(row=row, column=col)

        save_game = tk.Button(window, text="Save", command=self.create_csv())
        check_game = tk.Button(window, text="Done", command=self.check_game())
        exit_game = tk.Button(window, text="Exit", command=window.destroy)

        save_game.grid(row=9, column=3)
        check_game.grid(row=9, column=4)
        exit_game.grid(row=9, column=5)

        window.mainloop()

    def insert_values(self):

        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[row])):
                if (self.data[row][col][0] == 0):
                    continue
                self.spaces[row][col].insert(
                    tk.END, str(self.data[row][col][0]))

        # a2.insert(tk.END, "asdasd")

    def get_space_input(self, row, col):
        input = self.spaces[0][0].get("1.0", END)
        return input

    def check_game(self):
        return 1


def main():

    # 0 in first part of tuple means empty space
    # 0 in second part of tuple means given uneditable number
    data = [[(0, 1), (9, 0), (3, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0)],
            [(1, 0), (0, 4), (4, 0), (1, 0), (1, 0),
             (1, 0), (1, 0), (1, 0), (1, 0)],
            [(6, 0), (5, 0), (0, 8), (1, 0), (1, 0),
             (1, 0), (1, 0), (1, 0), (1, 0)],
            [(0, 1), (9, 0), (3, 0), (1, 0), (1, 0),
             (1, 0), (1, 0), (1, 0), (1, 0)],
            [(1, 0), (0, 4), (4, 0), (1, 0), (1, 0),
             (1, 0), (1, 0), (1, 0), (1, 0)],
            [(6, 0), (5, 0), (0, 8), (1, 0), (1, 0),
             (1, 0), (1, 0), (1, 0), (1, 0)],
            [(0, 1), (9, 0), (3, 0), (1, 0), (1, 0),
             (1, 0), (1, 0), (1, 0), (1, 0)],
            [(1, 0), (0, 4), (4, 0), (1, 0), (1, 0),
             (1, 0), (1, 0), (1, 0), (1, 0)],
            [(6, 0), (5, 0), (0, 8), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0)]]

    obj = Sudoku('data.csv')

    obj.create_csv()
    # csv = obj.import_csv()

    print(obj.get_empty_board())


if __name__ == "__main__":
    main()
