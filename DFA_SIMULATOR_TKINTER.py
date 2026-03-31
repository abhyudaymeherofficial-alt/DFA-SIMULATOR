import tkinter as tk
from tkinter import messagebox

def simulate_dfa():
    alphabets = alphabet_entry.get().split(',')
    states = states_entry.get().split(',')
    start_state = start_entry.get()
    final_states = final_entry.get().split(',')
    test_string = string_entry.get()

    transition_table = []
    for i in range(len(states)):
        row = []
        for j in range(len(alphabets)):
            value = transition_entries[i][j].get()
            row.append(value)
        transition_table.append(row)

    current_state = start_state
    path = [current_state]

    try:
        for char in test_string:
            alphabet_index = alphabets.index(char)
            state_index = states.index(current_state)

            next_state = transition_table[state_index][alphabet_index]

            path.append(next_state)
            current_state = next_state

        transition_path = " → ".join(path)

        if current_state in final_states:
            result_label.config(
                text=f"String Accepted\nPath: {transition_path}",
                fg="green"
            )
        else:
            result_label.config(
                text=f"String Rejected\nPath: {transition_path}",
                fg="red"
            )

    except:
        messagebox.showerror("Error", "Invalid input or transition")


def create_transition_table():
    global transition_entries
    alphabets = alphabet_entry.get().split(',')
    states = states_entry.get().split(',')

    transition_entries = []

    for widget in table_frame.winfo_children():
        widget.destroy()

    for i in range(len(states)):
        row_entries = []
        for j in range(len(alphabets)):
            entry = tk.Entry(table_frame, width=8)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        transition_entries.append(row_entries)


root = tk.Tk()
root.title("DFA Simulator")
root.geometry("600x500")

tk.Label(root, text="Alphabets (comma separated)").pack()
alphabet_entry = tk.Entry(root)
alphabet_entry.pack()

tk.Label(root, text="States (comma separated)").pack()
states_entry = tk.Entry(root)
states_entry.pack()

tk.Button(root, text="Create Transition Table", command=create_transition_table).pack()

table_frame = tk.Frame(root)
table_frame.pack()

tk.Label(root, text="Start State").pack()
start_entry = tk.Entry(root)
start_entry.pack()

tk.Label(root, text="Final States (comma separated)").pack()
final_entry = tk.Entry(root)
final_entry.pack()

tk.Label(root, text="Test String").pack()
string_entry = tk.Entry(root)
string_entry.pack()

tk.Button(root, text="Simulate DFA", command=simulate_dfa).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()