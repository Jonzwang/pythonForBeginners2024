states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut']

# add Massachusetts tp the states
states.append('Massachusetts')
states.append('Maryland')
states.append('New Hampshire')

states.insert(7,  'South Carolina')

states_10_to_13 = ['virginia', 'New York', 'North Carolina', 'Rhode Island']

states.extend(states_10_to_13)

def print_state_one_by_one():
    for state in states:
        print(state)


print_state_one_by_one()