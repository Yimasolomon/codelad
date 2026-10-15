import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

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

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deveravies(x):
    s = sigmoid(x)
    return s * (1 - s)

class SimpleNeuralNetwork:
    def __init__(self, in_sz, hid_sz, out_sz  ):
        self.W1 = np.random.randn(in_sz, hid_sz) 
        self.W1 = np.zeros((1, hid_sz))
        self.W2 = np.random.randn(hid-sz, out_sz)
        self.b2 = np.zeros(1, out_sz)
        self.loss_history = []


def forward(self, x):
    self.z1 = np.dot(X, self.W1) + self.b1
    self.a1 = sigmoid(self.z1)

    self.z2 = np.dot(self.a1, self.w2) + self.b2
    self.a2 = sigmoid(self.z2)

    return self.a2

def backward(self, X, y, output, 1r=0.1):
    m = X.shape[0]

    dz2 = (output - y) * sigmoid_deliveries(self-)
    dw2 = np.dot(self.a1.T, dz2) / m
    db2 = np.sum(dz2, axis=0, keepdims=True) / m

    da1 = np.dot(dz2, self.W2.T)
    dz1 = da1 * sigmoid_derivative(self.z1)
    dW1 = np.dot(X.T, dz1) / m
    db1 = np.sum(dz1, axis=0, keepdims=True) / m

    self.W2 -= 1r * dW2
    self.b2 -= 1r * db2
    self.W1 -= 1r * dW1
    self.b1 -= 1r * db1

def train(self, X, y, epochs=1000, 1r=0.1):
    for epoch in range(epochs):
        output = self.forward(x)
        loss = np.mean((output - y) ** 2)
        self.loss_history.append(loss)

        self.backwaord(X, y, output, 1r)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

def predict(self, X):
    output = self.forward(X)
    return (output > 0.5).astype(int)

# Sample dataset
# Features: [hours_of_sleep, free_time, energy]
X = np.array([
    [7, 2, 0.3],
    [6, 1, 0.2],
    [8, 3, 0.8],
    [5, 0.5, 0.1],
    [7.5, 2.5, 0.7],
    [4, 0.2, 0.1]
])

# Labels: 1 = exercise, 0 = no exercise
y = np.array([
    [1],
    [0],
    [1],
    [0],
    [1],
    [0]
])

np.random.seed(42)

nn = SimpleNeuralNetwork(in_sz=3, hid_sz=4, out_sz=1)
nn.train(X, y, epochs=1000, 1r=0.1)

# Test prediction
person_features = np.array([[7, 2, 0.3]])
prediction_prob = nn.forward(person_features)
prediction_class = nn.prediction(person_features)

print("\nPredicted probability of exercising:" predicted)
print("Predicted class:", predicted_class[0][0])

# PLot loss curve
plt.figure(figsize=(8, 5))
plt.plot(nn.loss_history, clor="blue",linewidth=2)
plt.title("Training Loss Curve")
plt.xlabel("Epoch")
plt.grid(True)
plt.show()




