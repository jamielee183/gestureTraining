# The full neural network code!
###############################
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from numpy import genfromtxt

import pandas as pd

df1 = pd.read_csv("movement1.csv")
data1 = df1.to_numpy()
#delete the nans
data1 = np.delete(data1, 220, 1)

df2 = pd.read_csv("movement2.csv")
data2 = df2.to_numpy()
#delete the nans
data2 = np.delete(data2, 220, 1)

df3 = pd.read_csv("movement3.csv")
data3 = df3.to_numpy()
#delete the nans
data3 = np.delete(data3, 220, 1)

df4 = pd.read_csv("movement4.csv")
data4 = df4.to_numpy()
#delete the nans
data4 = np.delete(data4, 220, 1)

data5 = np.append(data1, data2, 0)
data6 = np.append(data3, data4, 0)

training_data = np.append(data5, data6, 0)

training_data = (training_data/2**16) - 0.5

training_labels = np.zeros(76)
training_labels[0:19] = 1
training_labels[19:38] = 2
training_labels[38:57] = 3
training_labels[57:76] = 4


# Build the model.
model = Sequential([
  Dense(64, activation='relu', input_shape=(220,)),
  Dense(64, activation='relu'),
  Dense(5, activation='softmax'),
])

# Compile the model.
model.compile(
  optimizer='adam',
  loss='categorical_crossentropy',
  metrics=['accuracy'],
)

# Train the model.
model.fit(
  training_data,
  to_categorical(training_labels),
  epochs=20,
  batch_size=32,
)

df5 = pd.read_csv("verificationData.csv")
predict_data = df5.to_numpy()
#delete the nans
predict_data = np.delete(predict_data, 220, 1)


# Evaluate the model.
#model.evaluate(
#  test_images,
#  to_categorical(test_labels)
#)

# Save the model to disk.
#model.save_weights('model.h5')

# Load the model from disk later using:
# model.load_weights('model.h5')

# Predict on the first 5 test images.
predictions = model.predict(predict_data)

# Print our model's predictions.
print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

# Check our predictions against the ground truths.
#print(test_labels[:5]) # [7, 2, 1, 0, 4]
