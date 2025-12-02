# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

with open("input.txt", "r") as f:
    input = f.read().strip().splitlines()
# input = ["R250", "L150", "R75", "L325", "R200", "L50", "L50", "R100"]
start_position = 50
old_position = start_position
current_position = start_position
password = 0

print(f"Starting at position: {current_position}")

for move in input:
    print(f"----- New move: {move} -----")
    turn_direction = move[0]
    step_count = int(move[1:])
    full_revolutions, step_count = divmod(step_count, 100)
    password += full_revolutions
    if full_revolutions > 0:
        print(
            f"Full revolutions: {full_revolutions}, added to password, new password: {password}, remaining steps: {step_count}"
        )

    if turn_direction == "L":
        if current_position == 0:
            current_position = 100 - step_count
            continue
        current_position -= step_count
        if current_position < 0:
            current_position = 100 - abs(current_position)
            if current_position != 0:
                password += 1
                print(f"Passed through 0 going left, new password: {password}")
    elif turn_direction == "R":
        if current_position == 0:
            current_position = 0 + step_count
            continue
        current_position += step_count
        if current_position > 99:
            current_position = current_position - 100
            if current_position != 0:
                password += 1
                print(f"Passed through 0 going right, new password: {password}")

    print(
        f"Direction {turn_direction}, old position: {old_position}, new position: {current_position}"
    )

    if current_position == 0 and old_position != 0:
        password += 1
        print(f"Stopped at zero, new password: {password}")

    old_position = current_position

print(f"Final position: {current_position}, Final password: {password}")
