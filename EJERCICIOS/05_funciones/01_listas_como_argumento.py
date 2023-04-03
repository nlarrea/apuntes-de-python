print("01 - MENSAJES\n")
"""
Crea una lista que contenga mensajes cortos. Pasa la lista a una función que se
llame 'show_messages()' para que imprima cada mensaje.
"""

messages = [
    "Hello World!",
    "I like learning Python",
    "Today is Monday"
]

def show_messages(msg_list):
    print("These are the messages from the given list:")
    for (idx, msg) in enumerate(msg_list):
        print(f"{idx}. {msg}")


show_messages(messages)
""" imprime:
0. Hello World!
1. I like learning Python
2. Today is Monday
"""



print("\n\n02 - ENVIANDO MENSAJES\n")
"""
Partiendo del código del ejercicio anterior, crea una función llamada
'send_messages()' que imprima cada texto y mueva cada mensaje a una nueva lista
llamada 'sent_messages'. Cuando acabes, imprime las dos listas para comprobar
que se han cambiado de una a otra correctamente.
"""

messages = [
    "Hello World!",
    "I like learning Python",
    "Today is Monday"
]

def send_messages(msg_list):
    sent_messages = []

    while msg_list:
        current_msg = msg_list.pop()
        print(current_msg)
        sent_messages.append(current_msg)
    
    return sent_messages


sent_messages = send_messages(messages)


# check if the messages are moved from one list to the other one

print(f"\nmessages list: {messages}")
# messages list: []

print(f"sent_messages list: {sent_messages}")
# sent_messages list: ['Today is Monday', 'I like learning Python', 'Hello World!']



print("\n\n03 - MENSAJES ARCHIVADOS\n")
"""
Partiendo del código del ejercicio anterior, llama a la función 'send_messages'
usando una copia de la lista 'messages'. Tras llamar a la función, imprime las
dos listas para asegurarte de que la original no se ha visto afectada.
"""

messages = [
    "Hello World!",
    "I like learning Python",
    "Today is Monday"
]

sent_messages = send_messages(messages[:])


# check if the original has been modified

print(f"\nmessages list: {messages}")
# messages list: ['Hello World!', 'I like learning Python', 'Today is Monday']

print(f"sent_messages list: {sent_messages}")
# sent_messages list: ['Today is Monday', 'I like learning Python', 'Hello World!']