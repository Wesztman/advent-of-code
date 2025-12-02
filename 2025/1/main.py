# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Read in input.txt into an array of strings
with open("input.txt", "r") as f:
    input = f.read().strip().splitlines()
start_position = 50
old_position = start_position
current_position = start_position
password = 0

print(f"Starting at position: {current_position}")

for move in input:
    turn_direction = move[0]
    step_count = int(move[1:])
    step_count = step_count % 100  # Normalize steps to within 0-99

    if turn_direction == "L":
        current_position -= step_count
        if current_position < 0:
            current_position = 100 - abs(current_position)
    elif turn_direction == "R":
        current_position += step_count
        if current_position > 99:
            current_position = current_position - 100

    print(
        f"Processed move: {move}, old position: {old_position}, new position: {current_position}"
    )

    if current_position == 0:
        password += 1
        print(f"Password hit at position {current_position}, new password: {password}")

    old_position = current_position

print(f"Final position: {current_position}, Final password: {password}")
