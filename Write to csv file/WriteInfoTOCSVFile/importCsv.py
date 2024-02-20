import csv

row_list = [["SNo", "Name", "Subject"],
              [1, "Ash Ketchum", "English"],
              [2, "Gary Oak", "Mathematics"],
              [3, "Brock Lesner", "Physics"]]

with open('studentsq.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(row_list)
