from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# MNIST download is required on the first run. Use a fixed subset for speed.
X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False, parser="liac-arff")
X = X.astype("float32") / 255.0
X_small, _, y_small, _ = train_test_split(
    X, y, train_size=10000, stratify=y, random_state=1
)
X_dev, X_test, y_dev, y_test = train_test_split(
    X_small, y_small, test_size=0.2, stratify=y_small, random_state=1
)
X_train, X_val, y_train, y_val = train_test_split(
    X_dev, y_dev, test_size=0.2, stratify=y_dev, random_state=1
)

clf = MLPClassifier(
    hidden_layer_sizes=(50, 50),   # one hidden layer, 40 neurons
    max_iter=50,
    solver="sgd",
    learning_rate_init=0.01,
    random_state=1,
)
clf.fit(X_train, y_train)
print("Validation accuracy:", clf.score(X_val, y_val))
# After choosing a configuration using validation results only:
# print("Final test accuracy:", selected_clf.score(X_test, y_test))

# 1. 0.933125
# 2. at 10: 0.896875
# at 100, 50: 0.940625
# 3. 0.94125

# The highest accuracy score appeared when max liter was at 50
# or when hidden layer sizes were (100, 50).
# The score dropped when the hidden layer sizes number was changed to be lower, like (10, 0)
# Getting the first result took a long time, but after running the code more times it ran faster

# I chose 50 for both hidden layer sizes and max liter and received the highest accuracy so far:
# 0.941875
# Learning rate 0.8: Validation accuracy: 0.101875
# Learning rate 0.01: Validation accuracy: 0.93125