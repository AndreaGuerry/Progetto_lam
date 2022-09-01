from gym import Env
from gym.spaces import Discrete, Box
from preparingdata import finaldata
import json
import numpy as np
import tensorflow as tf
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

log = open("data/Rl.log", "w")
log.write=("")
log.close()

logw = open("data/wallet.log", "w")
logw.write=("")
logw.close()

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

x_train = finaldata.x_train(jsonfagt, jsonbit)


class bitEnv(Env):
    def __init__(self):
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

        x_train = finaldata.x_train(jsonfagt, jsonbit)
        # Actions we can take, down, stay, up
        self.action_space = Discrete(3)
        # Temperature array
        self.observation_space = Box(low=0, high=21000000, shape=(6, 200))
        # Set start temp
        initialstate = np.array((x_train)[0])
        arraystate = initialstate.reshape(1, 6, 200)
        self.state = arraystate
        # Set shower length
        self.bit_length = (len(x_train) - 200)
        self.wallet = [100, 0]

    def step(self, action):

        if action == 0:
            logw=open("data/wallet.log","a")
            logw.write(str((self.wallet)[0]))
            logw.write("---")
            logw.write(str((self.wallet)[1]))
            logw.write("\n")

            logw.close()
            pass

        elif action == 1:
            log=open("data/Rl.log","a")
            quantity = ((self.wallet[0]) / 5)
            price = ((self.state[0])[2])[-1]
            quant = quantity / price
            self.wallet[0] = self.wallet[0] - quantity
            self.wallet[1] = self.wallet[1] + quant
            log.write("BUY ORDER: {} bitcoin for {}$ at {}\n".format(quant,quantity, price))
            log.close()
            logw=open("data/wallet.log","a")
            logw.write(str((self.wallet)[0]))
            logw.write("---")
            logw.write(str((self.wallet)[1]))
            logw.write("\n")
            logw.close()
        elif action == 2:
            log=open("data/Rl.log","a")
            price = ((self.state[0])[2])[-1]
            quant = self.wallet[1]
            money = price * quant
            self.wallet[0] = self.wallet[0] + money
            self.wallet[1] = 0
            log.write("SELL ORDER: {} bitcoin for {}$ at {} \n".format(quant,money, price))
            log.close()
            logw=open("data/wallet.log","a")
            logw.write(str((self.wallet)[0]))
            logw.write("---")
            logw.write(str((self.wallet)[1]))
            logw.write("\n")

            logw.close()
        else:
            x = 1000 / 0

        # Reduce shower length by 1 second
        self.bit_length -= 1

        # Calculate reward$
        price = ((self.state[0])[2])[-1]
        reward = (self.wallet[0] + self.wallet[1] * price)-100

        # Check if shower is done
        if self.bit_length <= 0:
            logw=open("data/reslut.log","a")
            logw.write("$ in the account=  ")
            logw.write(str((self.wallet)[0]))
            logw.write("\n")
            logw.write("B in the account=  ")
            logw.write(str((self.wallet)[1]))
            logw.write("\n")
            logw.write("Value in the account=  ")
            logw.write(str(self.wallet[0] + self.wallet[1] * price))
            logw.write("\n")
            logw.write("\n")
            done = True
        else:
            done = False

        # Apply temperature noise
        # self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}
        initialstate = np.array((x_train)[-((self.bit_length) - 1)])
        arraystate = initialstate.reshape(1, 6, 200)
        self.state = arraystate

        # Return step information
        return self.state, reward, done, info

    def render(self):
        # Implement viz
        pass

    def reset(self):
        self.bit_length = (len(x_train) - 200)

        rawdatabit = open("data/bitcoininfo.json", "r")
        rbit = rawdatabit.read()
        jsonbit = json.loads(rbit)

        rawdatafagt = open("data/fearandgreed.json", "r")
        rfagt = rawdatafagt.read()
        jsonfagt = json.loads(rfagt)

        initialstate = np.array((x_train)[0])
        arraystate = initialstate.reshape(1, 6, 200)
        self.state = arraystate
        self.wallet = [100, 0]

        return self.state


env = bitEnv()

env.observation_space.sample()

episodes = 10
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while done == True:
        # env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score = reward
    print('Episode:{} Score:{}'.format(episode, score))

import numpy as np

states = env.observation_space.shape
actions = env.action_space.n


def build_model(states, actions):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(1, 1, 6, 200)),
        tf.keras.layers.Dense(1000, activation='relu'),
        tf.keras.layers.Dense(600, activation='relu'),
        tf.keras.layers.Dense(300, activation='relu'),
        tf.keras.layers.Dense(3)
    ])
    return model


model = build_model(states, actions)

model = build_model(states, actions)
model.build(input_shape=(6, 200))
model.summary()
print("la je warm up ")

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions, nb_steps_warmup=50,
                   target_model_update=1e-2)
    return dqn
print("wesh faut s'entraier frerot")

opt = tf.keras.optimizers.Adam(learning_rate=0.01)
dqn = build_agent(model, actions)
dqn.compile(optimizer=opt, metrics=['mae'])
dqn.fit(env, nb_steps=40000, visualize=False, verbose=1)
