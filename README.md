# DFA Simulator (Python)

This project implements a **Deterministic Finite Automaton (DFA) Simulator** in Python with both **CLI (console)** and **GUI (Tkinter)** versions.
The user defines the **alphabets, states, transition table, start state, and final states**, then enters a **test string**.

The simulator processes the string **symbol by symbol** and moves between states according to the transition table.
The **transition path** is also displayed to show how the DFA moves through states.

If the final state reached is an **accepting state**, the program outputs **"String Accepted"**; otherwise **"String Rejected"**.

The **GUI version** provides an interactive interface where users can create the transition table dynamically and visualize the result.

### How to Run

1. Install **Python 3.x**
2. Run the file using: `python dfa_simulator.py`
3. Enter DFA details and test a string.
