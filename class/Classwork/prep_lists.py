name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']

def main():
    for i in range(3):
        name = input("Type in a name: ")
        name_list.append(name)

    print(name_list)

    print("The third name is ", name_list[2])

    print("The last seven names are ", name_list[-7:])


    numbers=[]
    for i in range(5):
        number = int(input(f"Enter a number {i+1}/5 "))
        numbers.append(number)

    print("Total is", sum(numbers))
    print("Mean is", sum(numbers) / len(numbers))
    print("Largest is", max(numbers))
    print("Smallest is", min(numbers))

main()