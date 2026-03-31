def Simulate_DFA():
    alphabets = []
    num_of_alphabet = int(input("Enter number of alphabets: "))
    for x in range(num_of_alphabet):
        alphabets.append(input(f"Enter symbol {x + 1}: "))

    states = []
    num_of_states = int(input("Enter number of states: "))
    for x in range(num_of_states):
        states.append(input(f"Enter state {x + 1}: "))

    transition_table = []

    for i in range(num_of_states):
        row = []
        for j in range(num_of_alphabet):
            connection = input(f"Enter transition from {states[i]} with {alphabets[j]}: ")
            row.append(connection)
        transition_table.append(row)

    start_state = input("Enter start state:")
    final_states=[]
    num_of_finalstates = int(input("Enter number of final states: "))
    for x in range(num_of_finalstates):
        final_states.append(input(f"Enter final_state {x + 1}: "))

    test_string = input("Enter testing string: ")

    current_state = start_state

    for char in test_string:
        alphabet_index = alphabets.index(char)
        state_index = states.index(current_state)

        current_state = transition_table[state_index][alphabet_index]

    if current_state in final_states:
        print("String Accepted")
    else:
        print("String Rejected")

Simulate_DFA()