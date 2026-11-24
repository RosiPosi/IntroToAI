
import tensorflow as tf

# Load MNIST dataset
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='sigmoid'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# Compile the model
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Train the model
history = model.fit(x_train, y_train, epochs=10)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("Final test accuracy:", test_accuracy)

# relu: 0.979200005531311
# tahn: 0.9760000109672546
# sigmoid: 0.9761000275611877

# The accuracy jumps drastically up usually between epoch 1 and 2.
# After epoch 5-7 the accuracy increases slower.
# Epochs 8-10 have the slightest changes.

# The fastest activation was relu, then sigmoid and lastly tahn, thought the last though had a very small difference.
# Sigmoid stats: accuracy: 0.9761 - loss: 0.0810
# tahn: accuracy: 0.9760 - loss: 0.0756
# relu: accuracy: 0.9792 - loss: 0.0705
# Sigmoid suggered the most loss out of the three. This is due to its vanishing gradients,
# where its gradients become very small when neurons are saturated.
# Since this network only has one hidden layer, the effect isn't as strong or noticeable.