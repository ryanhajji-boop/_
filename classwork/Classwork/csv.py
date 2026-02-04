name = ['A', 'B', 'C']
score = [10,20,30]
age = [20,21,22]

file = "data.csv"

with open(file, 'w') as csv_file:
    for i in range(3):
        toAdd = f"{name[i]}, {score[i]}, {age[i]}\n"
        csv_file.write(toAdd)


    