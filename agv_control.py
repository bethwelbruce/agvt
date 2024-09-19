
def execute_order(order):
    if order["type"] == "turn":
        turn(order["value"])
    elif order["type"] == "go_straight":
        go_straight(order["distance"])

def execute_instant_action(action):
    if action == "Load":
        load()
    elif action == "Unload":
        unload()
    # Add more actions as needed

def turn(angle):
    # Implement turn logic
    pass

def go_straight(distance):
    # Implement go straight logic
    pass

def load():
    # Implement load logic
    pass

def unload():
    # Implement unload logic
    pass
