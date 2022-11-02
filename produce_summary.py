# def produce_summary():

#     print("Day 1")
#     the_file = open("um-deliveries-day-1.txt")
#     for line in the_file:
#         line = line.rstrip()
#         words = line.split('|')
#         amount = float(words[2])
#         count = int(words[1])
#         melon = words[0]
#         print(f'Delivered {count} {melon} for total of ${amount}')

#     print("Day 2")
#     the_file = open("um-deliveries-day-2.txt")
#     for line in the_file:
#         line = line.rstrip()
#         words = line.split('|')
#         amount = float(words[2])
#         count = int(words[1])
#         melon = words[0]
#         print(f'Delivered {count} {melon} for total of ${amount}')

#     print("Day 3")
#     the_file = open("um-deliveries-day-3.txt")
#     for line in the_file:
#         line = line.rstrip()
#         words = line.split('|')
#         amount = float(words[2])
#         count = int(words[1])
#         melon = words[0]
#         print(f'Delivered {count} {melon} for total of ${amount}')

# print(produce_summary())

def produce_summary_2(num_of_day, path):
    '''Gives the total count, amount, and type of Melon sold'''

    print(f"Day {num_of_day}") 

    delivery_history = open(path) ## creates file with melon data
    for line in delivery_history: ## iterates over the file history line by line
        line = line.rstrip() ## removes extra whitespace to the R
        words = line.split('|') ## creates list of data points

        amount = float(words[2]) ## pinpoints cost of melons
        count = int(words[1]) ## pinpoints count of melons
        melon = words[0] ## pinpoints type of melon 

        print(f'Delivered {count} {melon} for total of ${amount}')

print(produce_summary_2(3,"um-deliveries-day-3.txt")) ## passes in which day and the cooresponding melon data file for that day 

