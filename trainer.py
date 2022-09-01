import tensorflow as tf
from preparingdata import finaldata
import json
import numpy as np
from preparingdata import converter

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

x_test = np.array(finaldata.x_test(jsonfagtest, jsonbitest))
y_test = np.array(finaldata.y_test(jsonbitest))

model1 = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(6, 200)),
    tf.keras.layers.Dense(600, activation='relu'),
    tf.keras.layers.Dense(600, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(2)
])

loss_fn = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
opt = tf.keras.optimizers.Adam(learning_rate=40)
model1.compile(optimizer=opt,
               loss='MeanAbsoluteError')
print("model compiled")

# tf.nn.softmax(predictions).numpy()
# loss_fn(y_train[], predictions).nu8mpy()
sus = np.array(x_test[-1])
x=model1(sus.reshape(1, 6, 200)).numpy()
print(x)
model1.fit(x_train, y_train, epochs=100, batch_size=32)

sus = np.array(x_train[-1])
print( (y_train[-1])[0])
x=(model1(sus.reshape(1, 6, 200)).numpy())[0]
print(x)


