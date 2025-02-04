import lab_chat as lc

def get_user_input(message, to_upper=True):
    if to_upper:
        response = input(message).strip().upper()
    else:
        response = input(message).strip()
    return response

def get_username():
    return get_user_input("Type your username: ")

def get_group():
    return get_user_input("Type your group to join: ")

def get_message():
    return get_user_input("What's your message: ", False)

def initialize_chat():
    user = get_username()
    group = get_group()
    node = lc.get_peer_node(user)
    lc.join_group(node, group)
    channel = lc.get_channel(node, group)
    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()