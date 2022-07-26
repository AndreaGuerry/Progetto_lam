import tensorflow as tf
from preparingdata import finaldata
import json
import numpy as np

print("TensorFlow version:", tf.__version__)
rawdatafagt = open("data/fearandgreed.json", "r")
rfagt = rawdatafagt.read()
jsonfagt = json.loads(rfagt)

rawdatafagtest = open("data/fearandgreedtest.json", "r")
rfagtest = rawdatafagtest.read()
jsonfagtest = json.loads(rfagtest)

rawdatabit = open("data/bitcoininfo.json", "r")
rbit = rawdatabit.read()
jsonbit = json.loads(rbit)

rawdatabitest = open("data/bitcoininfotest.json", "r")
rbitest = rawdatabitest.read()
jsonbitest = json.loads(rbitest)

x_train = np.array(finaldata.x_train(jsonfagt, jsonbit))
y_train = np.array(finaldata.y_train(jsonbit))


print(np.shape(x_train))
x_train.reshape(1,1421,6,200)
print(np.shape(x_train))
x_test = finaldata.x_test(jsonfagtest, jsonbitest)
y_test = finaldata.y_test(jsonbitest)

model1 = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(6,200)),
    tf.keras.layers.Dense(600, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(600, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(2)
])

loss_fn = tf.keras.losses.CategoricalCrossentropy(from_logits=True)

model1.compile(optimizer='adam',
               loss=loss_fn,
               metrics=['accuracy'])
print("model compiled")

predictions = model1((x_train[0]).reshape(1,6,200)).numpy()
print(predictions)
# tf.nn.softmax(predictions).numpy()
# loss_fn(y_train[:1], predictions).nu8mpy()


model1.fit(x_train, y_train, epochs=40, batch_size=1)
model1.evaluate(x_test, y_test, verbose=2)
