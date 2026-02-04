student_scores = {}
i = 1

while True:
    try:
        score = int(input(f"Enter score for child {i} (or -1 to stop): "))
        if score == -1:
            break  # exit loop
        elif score > 100 or score < 0:
            print("Enter a score that is greater than 0 and less than 100")
            continue # goes back to the top
        name = input(f"Enter name for child {i}: ")
        student_scores[name] = score
        i += 1
    except ValueError:
        print("Please enter an integer score")

sorted_scores = sorted(student_scores, key=student_scores.get, reverse=True)

# this line above gives us the scores sorted by highest to lowest

for student in sorted_scores:
    print(student, student_scores[student])

# we then iterate through this list and we print the student's name, and their score which will be found when we go back to our starting array and find the score of the student that we are currently looking at.

