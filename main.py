#Sodoku game!
#create your own sodoku boards, generate them automatically, and play!
import csv
import tkinter as tk


class Sudoku:

    #file_location:
    #data: 2D array of tuples, with (given, correct) values
    def __init__(self, file_location="none", data=0):
        self.file_location = file_location
        self.data = data
        
        self.empty_board = self.create_empty_board(data)
        self.create_window()

   
    #could add a "create sodoku" function to create random games! 
    # printing it to csv to save a nice board, wordle style  
    def create_csv(self):
        file = open(self.file_location, 'w')
        csvwriter = csv.writer(file)
        for row in self.data:
            csvwriter.writerow(row)

    #3bi
    #imports a prewritten sudoku game from a csv file
    def import_csv(self):
        file = open(self.file_location)
        csvreader = csv.reader(file)
        
        arr = []
        for row in csvreader:
            try:
                temp = []
                for tup in row:
                    temp.append(tuple(map(int, tup.replace('(', '').replace(')', '').split(', '))))
                arr.append(temp)
            except:
                print("Not a tuple: " + str(row))
                arr.append(row)
        file.close()
        self.data = arr

    def set_data(self, data):
        self.data = data

    #input_arr
    def create_empty_board(self, input_arr):
        empty_board = []
        for i in range(len(input_arr)):
            temp = []
            for j in range(len(input_arr[i])):
                temp.append(input_arr[i][j][0])
            empty_board.append(temp)
        
        return empty_board

    def check_space(self, tup):
        if (tup[0] == tup[1] or tup[1] == 'X'):
            return True
        return False

    def update_space(self, new):
        return True

    def get_empty_board(self):
        return self.empty_board

    def create_window(self):
        window = tk.Tk()


#sodoku analytics!

#arr: [(x, y), (x, y), (x, y)...]
def analyze_one(arr):
    val = 0
    for tup in arr:
        val += tup[0] * tup[1]
    return val

#3c
#arr: [[(x, y), (x, y)...], [(x, y), (x, y)...], ...]
def get_weighted_scores(arr):
    weighted_arr = [] 
    for tup in arr:
        if (type(tup[0][0]) != int):
            continue
        analyzed_tup = analyze_one(tup)
        weighted_arr.append(analyzed_tup)

    return weighted_arr

#weighted_scores: [x, y, z, ...]
#direction: True or False
# if true, list is from smallest to highest
# if false, list is from highest to smallest
def sort_scores(weighted_scores, direction):
    arr = weighted_scores
    for i in range(0, len(arr) - 1):
        for j in range (0, len(arr) - 1 - i):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    if (direction):
        return arr
    elif (direction == False):
        return arr[::-1]
    else:
        return -1

def search(arr, target):
    return 1

def main():  
    
    #'-' means empty space
    #'X' means given uneditable number
    data = [[('-',1), (9,'X'), (3,'X')],
            [(1, 'X'), ('-',4), (4,'X')], 
            [(6,'X'), (5,'X'), ('-',8)]]
    
    obj = Sudoku('data.csv', data)
    
    obj.create_csv()
    csv = obj.import_csv()
    
    print(obj.get_empty_board())
    
    #print(csv)
    # scores = get_weighted_scores(csv)
    # print(scores)
    # x = sort_scores(scores, True)
    # print(scores)
    # print(x)

if __name__ == "__main__":
    main()