import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # ← Add this

from sklearn.tree import DecisionTreeClassifier

import sys
import warnings
warnings.filterwarnings('ignore')          # ← Add this

# Suppress stderr
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')         # ← Add this

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# rule_base
def rule_based_drive(traffic_light, obstacle):
    if traffic_light == "red" or obstacle == "yes":
        return "Stop"
    elif traffic_light == "yellow":
        return "Slow"
    else:
        return "Go"


# search_base
def search_based_drive(traffic_light, obstacle):
    scores = {"Stop": 0, "Slow": 0, "Go": 0}

    if traffic_light == "red": # traffic_light condition
        scores["Stop"] += 3
    elif traffic_light == "yellow":
        scores["Slow"] += 2
    elif traffic_light == "green":
        scores["Go"] += 2

    if obstacle == "yes": # obstacle condition
        scores["Stop"] += 2
        scores["Slow"] += 1

    return max(scores, key=scores.get)


# machine learning
def machine_learning(traffic_light, obstacle):
    # red=0, yellow=1, green=2
    # obstacle: no=0, yes=1
    X = [
        [0, 0],
        [1, 0],
        [2, 0],
        [2, 1],
        [1, 1]
    ]
    y = ["Stop", "Slow", "Go", "Stop", "Stop"]

    # Model: create and train model
    model = DecisionTreeClassifier() # Create Model
    model.fit(X, y) # Train Model


    # output
    new_input = [traffic_light, obstacle]
    return model.predict([new_input])
    
    
# deep learning
def deep_learning(traffic_light, obstacle):
    X = np.array([ # Dataset of input (signal + obstacle)
        [0, 0],
        [1, 0],
        [2, 0],
        [2, 1],
        [1, 1]
    ], dtype=float)

    # Stop=[1,0,0], Slow=[0,1,0], Go=[0,0,1]
    y = np.array([ # Dataset of decisions (labels)
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [1, 0, 0]
    ], dtype=float)
    # ==========================================================================
    # neural network layers
    model = Sequential() # Create model
    model.add(Dense(8, activation="relu", input_shape=(2,))) # Hidden layer
    model.add(Dense(3, activation="softmax")) # Output layer

    # teach
    model.compile(optimizer="adam", loss="categorical_crossentropy")
    model.fit(X, y, epochs=150, verbose=0) # teach model

    # predict
    new_input = [traffic_light, obstacle]
    pred = model.predict(np.array([new_input], dtype=float), verbose=0)
    labels = ["Stop", "Slow", "Go"]
    return labels[np.argmax(pred)]
    # ==========================================================================
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # 'cls'   → Windows
    # 'clear' → Linux / Mac


while(True):
    print('\t*** Self-Driving Cars ***')
    print("[1].Rule base")
    print("[2].Search base")
    print('[3].Machine learning')
    print('[4].Deep learning')
    print('[5].Clear Screen')
    print('[0].Exit')
    number = int(input("choose number: "))
    match number:
        case 0: # exit
            print('\nExit program...\n')
            exit(0)
            
            
        case 1: # rule base
            print('\nRule base\nInput:')
            traffic_light = input('Traffic_light(red/yellow/green): ')
            obstacle = input('Obstacle(yes/no):')
            print('\n *** Result *** ')
            print(f'Traffic Light = {traffic_light}')
            print(f'Obstacle = {obstacle}')
            print(f'Action = {rule_based_drive(traffic_light, obstacle)}')
            print()
            
            
        case 2: # Search base
            print('\nSearch base\nInput:')
            traffic_light = input('Traffic_light(red/yellow/green): ')
            obstacle = input('Obstacle(yes/no):')
            print('\n *** Result *** ')
            print(f'Traffic Light = {traffic_light}')
            print(f'Obstacle = {obstacle}')
            print(f'Action = {search_based_drive(traffic_light, obstacle)}')
            print()
            
            
        case 3: # machine learning
            print('\nMachine Learning\nTraffic Rules(!)')
            print('- red = 0, yellow = 1, green = 2')
            print('- obstacle: no = 0, yes = 1')
            print('[0,0] = Stop')
            print('[1,0] = Slow')
            print('[2,0] = Go')
            print('[2,1] = Stop')
            print('[1,1] = Stop\n')
            traffic_light = int(input('Traffic Light(0/1/2): '))
            obstacle = int(input('Obstacle(0/1): '))
            print('\n *** Result *** ')
            print(f'[{traffic_light}, {obstacle}]')
            print(f'Action = {machine_learning(traffic_light, obstacle)}')
            print()
        
        
        case 4: # deep learning
            print('\nDeep Learning\nTraffic Rules(!)')
            print('- red = 0, yellow = 1, green = 2')
            print('- obstacle: no = 0, yes = 1')
            print('[0, 0] = red light, no obstacle')
            print('[1, 0] = yellow light, no obstacle')
            print('[2, 0] = green light, no obstacle')
            print('[2, 1] = green light, obstacle')
            print('[1, 1] = yellow light, obstacle')
            traffic_light = int(input('Traffic Light(0/1/2): '))
            obstacle = int(input('Obstacle(0/1): '))
            print('\n *** Result *** ')
            print(f'[{traffic_light}, {obstacle}]')
            print(f'Action = {deep_learning(traffic_light, obstacle)}')
            print()
        
        case 5: # clear screen
            clear_screen()
            
        case _: # Default case
            print('\nError: Wrong number input again\n')
            

