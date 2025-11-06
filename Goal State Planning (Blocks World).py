initial_state = ['A on B', 'B on Table', 'C on Table']
goal_state = ['B on C', 'A on B', 'C on Table']

plan = []

def move(block, from_pos, to_pos):
    return f"Move {block} from {from_pos} to {to_pos}"

# Simple goal stack planning simulation
for goal in goal_state:
    if goal not in initial_state:
        block, rest = goal.split(' on ')
        from_pos = 'Table'
        to_pos = rest
        plan.append(move(block, from_pos, to_pos))
        initial_state.append(goal)

print("Plan to reach goal state:")
for step in plan:
    print(step)
