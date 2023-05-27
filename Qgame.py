from qiskit import QuantumCircuit, execute, Aer

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1, 1)

# Game loop
while True:
    # Player's turn
    player_measurement = input("Choose measurement basis (X or Z): ").upper()

    if player_measurement == 'X':
        qc.h(0)  # Apply Hadamard gate for X-basis measurement
    elif player_measurement == 'Z':
        qc.i(0)  # Apply identity gate for Z-basis measurement
    else:
        print("Invalid input. Please choose X or Z.")
        continue

    qc.measure(0, 0)

    # Simulate the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator).result()
    counts = result.get_counts()
    coin_outcome = list(counts.keys())[0]

    print("Player's measurement outcome:", coin_outcome)

    # Computer's turn
    computer_measurement = 'X' if coin_outcome == '0' else 'Z'
    print("Computer's measurement basis:", computer_measurement)

    if computer_measurement == 'X':
        qc.h(0)  # Apply Hadamard gate for X-basis measurement
    elif computer_measurement == 'Z':
        qc.i(0)  # Apply identity gate for Z-basis measurement

    qc.measure(0, 0)

    # Simulate the quantum circuit
    result = execute(qc, simulator).result()
    counts = result.get_counts()
    coin_outcome = list(counts.keys())[0]

    print("Computer's measurement outcome:", coin_outcome)

    # Check for a winner
    if player_measurement == coin_outcome:
        print("Congratulations! You win!")
        break

    # Reset the circuit for the next round
    qc.reset(0)
