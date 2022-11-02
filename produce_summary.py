
def produce_summary():

    print("Day 1")
    the_file = open("um-deliveries-day-1.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        amount = float(words[2])
        count = int(words[1])
        melon = words[0]
        print(f'Delivered {count} {melon} for total of ${amount}')

    print("Day 2")
    the_file = open("um-deliveries-day-2.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        amount = float(words[2])
        count = int(words[1])
        melon = words[0]
        print(f'Delivered {count} {melon} for total of ${amount}')

    print("Day 3")
    the_file = open("um-deliveries-day-3.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        amount = float(words[2])
        count = int(words[1])
        melon = words[0]
        print(f'Delivered {count} {melon} for total of ${amount}')

print(produce_summary())

# def produce_summary_2(num_of_day, path):

#     print(f"Day {num_of_day}")

#     delivery_history = open(path)
#     for line in delivery_history:
#         line = line.rstrip()
#         words = line.split('|')

#         amount = float(words[2])
#         count = int(words[1])
#         melon = words[0]

#         print(f'Delivered {count} {melon} for total of ${amount}')

# print(produce_summary_2(1,"um-deliveries-day-3.txt"))

