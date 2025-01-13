import sys

number_of_names = input("Number of names: ")


bibliography = [item + "," for item in sys.argv[1].split(",")]




for i in range(0, int(number_of_names)):
    name = bibliography[i].split()

    name = name[1:] + [name[0]]
    result = ' '.join(name)
    bibliography[i] = result + ', '


complete_bibliography = ''.join(bibliography)

print(f" \x1B[3m{complete_bibliography}")

# comma between names
