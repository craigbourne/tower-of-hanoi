def move_disk(n, source, destination, auxiliary):
    global move_count
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        move_count += 1
        return
    move_disk(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    move_count += 1
    move_disk(n - 1, auxiliary, destination, source)

def print_tower(n):
    for i in range(1, n + 1):
        print('*' * i)

def towers_of_hanoi(n):
    global move_count
    move_count = 0
    
    print("Initial state:")
    print("Tower A:")
    print_tower(n)
    print("Tower B:")
    print("Tower C:")

    move_disk(n, 'A', 'C', 'B')

    print("\nFinal state:")
    print("Tower A:")
    print("Tower B:")
    print("Tower C:")
    print_tower(n)

    print(f"Total number of moves: {move_count}")

num_disks = int(input("Enter the number of disks: ")) # Get user input for number of disks
towers_of_hanoi(num_disks)
