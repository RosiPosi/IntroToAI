import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),   # ← change just this word
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

import tensorflow as tf

print(tf.__version__)