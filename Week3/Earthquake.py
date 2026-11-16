import random

def generate_data(n):
    data = []

    for _ in range(n):

        # Earthquake: average once every 111 days
        E = int(random.random() < 1/111)

        # Burglar: average once every 365 days
        B = int(random.random() < 1/365)

        # Alarm depends on E and B
        if E == 1 and B == 1:
            A = int(random.random() < 0.97)

        elif E == 1:
            A = int(random.random() < 0.81)

        elif B == 1:
            A = int(random.random() < 0.92)

        else:
            A = int(random.random() < 0.0095)

        data.append([E, B, A])

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


# Column indices: E=0, B=1, A=2

# 1. P(B=1 | A=1)
p1 = conditional_probability(data, 1, {2: 1})

# 2. P(B=1 | A=1, E=1)
p2 = conditional_probability(data, 1, {2: 1, 0: 1})


print("P(B=1 | A=1):", p1)
print("P(B=1 | A=1, E=1):", p2)

# P(B=1 | A=1): 0.12676794133053956
# P(B=1 | A=1, E=1): 0.0051813471502590676

# First result is the probability that a burglary has occured given that the alarm went off. It is slightly higher than I expected, not sure if I did it right.
# second result is the probability that burglary has occured given that the alarm has gone off and an earthquake has occured. It makes sense why this digit is so small.

# When the sample size increases, the results become more stable and generally approach the true probabilities. 
# This is because a larger sample reduces the influence of random variation and provides a more accurate Monte Carlo approximation.