
import random

def generate_data(n):
    data = []

    for _ in range(n):

        # B: Battery
        B = int(random.random() < 0.9)

        # R: Radio (depends on B)
        if B == 0:
            R = 0
        else:
            R = int(random.random() < 0.9)

        # I: Ignition (depends on B)
        if B == 0:
            I = 0
        else:
            I = int(random.random() < 0.95)

        # G: Gas
        G = int(random.random() < 0.95)

        # S: Starts (depends on I and G)
        if I == 1 and G == 1:
            S = int(random.random() < 0.99)
        else:
            S = 0

        # M: Moves (depends on S)
        if S == 1:
            M = int(random.random() < 0.99)
        else:
            M = 0

        data.append([B, R, I, G, S, M])

    return data


# Generate 100,000 samples
random.seed(42)
data = generate_data(100000)


# Calculate conditional probabilities
def conditional_probability(data, target, conditions):

    selected = []

    for row in data:
        match = True

        for column, value in conditions.items():
            if row[column] != value:
                match = False
                break

        if match:
            selected.append(row)

    if len(selected) == 0:
        return None

    count = sum(row[target] for row in selected)

    return count / len(selected)


# Column indices: B=0, R=1, I=2, G=3, S=4, M=5

# 1. P(B=1 | R=1, G=1, S=0)
p1 = conditional_probability(data, 0, {1: 1, 3: 1, 4: 0})

# 2. P(S=1 | R=1, I=1, G=1)
p2 = conditional_probability(data, 4, {1: 1, 2: 1, 3: 1})

# 3. P(S=1 | R=0, I=1, G=1)
p3 = conditional_probability(data, 4, {1: 0, 2: 1, 3: 1})


print("P(B=1 | R=1, G=1, S=0):", p1)
print("P(S=1 | R=1, I=1, G=1):", p2)
print("P(S=1 | R=0, I=1, G=1):", p3)

# P(B=1 | R=1, G=1, S=0): 1.0
# P(S=1 | R=1, I=1, G=1): 0.9897108050266147
# P(S=1 | R=0, I=1, G=1): 0.9910242223041928

# Give an interpretation to the above probabilities. 
# Are they in line with your intuition? In other words, do they make sense?
