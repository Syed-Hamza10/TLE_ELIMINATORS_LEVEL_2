from itertools import permutations

def print_all_permutations(string):
    perm_set = set()  # To store unique permutations
    for perm in permutations(string):
        perm_set.add(''.join(perm))  # Convert tuple to string and add to set
    print(len(perm_set))  # Print the count of permutations
    for perm in sorted(perm_set):  # Sort and print each permutation
        print(perm)

# Example usage:
string_to_permute = input()
print_all_permutations(string_to_permute)
