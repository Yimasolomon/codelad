# import numpy as np
# import matplotlib.pyplot as plt
# from collections import Counter
# import pandas as pd

# np.random.seed(42)

from collections import Counter

# Activities: 0=Sleep, 1=Work,
# 2=Exercise, 3=Social, 4=Leisure

historical_activities = [
    0, 1, 2, 1, 3, 1, 4,
    0, 1, 2, 1, 3, 1, 4, 0
]

def calculate_probabilities(sequence):
    counts = Counter(sequence)
    total = len(sequence)
    probabilities = {
        activity: count / total
        for activity, count in counts.items()
    }
    return probabilities

probs = calculate_probabilities(historical_activities)
activity_names = {
    0: 'Sleep',
    1: 'Work',
    2: 'Exercise',
    3: 'Social',
    4: 'Leisure'
}

for activity, prob in sorted(probs.items()):
    print(f'{activity_names[activity]}: {prob:.2%}')

# CONDITIONAL PROBABLITIY

def calculate_conditional_probabilities(sequence):
    transitions = {}

    for i in range(len(sequence) - 1):
        current = sequence[i]
        next_act = sequence[i + 1]
    
    if current not in transitions:
        transitions[current] = []

    transitions[current].append(next_act)

conditional_probs = {}

for current, next_list in transitions.items():
    counts = Counter(next_list)
    total = len(next_list)

    conditional_probs[current] = {
        a: c / total
        for a, c in counts.items()
    }

return conditional_probs

def predict_next_activity(current_activity, conditional_probs):
    if current_actvity not in conditional_probs:
        return None
    
    next_probs = conditional_probs[current_activity]
    most_likely_next = max(next_probs.items(), key=lambda item: item[1])[0]
    return most_likely_next

# Overall probabilities
probs = calculate_probabilities(historical_activities)

print("overall activity probabilities:")
for activity, prob in sorted(probs.items()):
    print(f"{activity_names[activity]}: {prob:.2%}")

# Conditional probabilities

cond_probs = calculate_conditional_probabilities(historical_activities)

print("\nCondiitional probabilities:")
for curretnt, next_probs in cond_probs.items():
    print(f"\nIf current activity is {activity_names[current]}")
    for next_act, prob in sorted(next_probs.items()):
        print(f" Next likely activity {activity_names[next_activity]}")

# Predict next activity from work
start_activity = 1 # Work
predict = predict_next_activity(start_activity, conditional_probs)
print(f"\nMost likely activity after {activity_names[start_activity]}")

# Predict next activity from work
start_activity = 1 #Work
predictted = predict_next_activity(start_activity, cond_probs)
print(f"\nMost likely activity after {activity_names[start_activity]}")

# Challenge: predict a sequence of 5 activities starting from
current = 1 #Work
predicted_sequence = [current]

for _ in range(5):
    if next_activity is None:
        break
    predicted_sequence.append(next_activity)
    current = next_activity


# PERCEPTRON - BASIC UNIT OF NEURAL NETWORK