texts = ["Hey, there", "Wow is the weather nice", "What are your plans?"]

def print_messages(message_list):
    for text in message_list:
        print(text)

sent_messages = []

def send_messages(unsent, sent):
    while unsent:
        current_msg = unsent.pop()
        print(current_msg)
        sent_messages.append(current_msg)

send_messages(texts[:], sent_messages)
print("\ntexts to send")
print_messages(texts)
print("\ntexts sent")
print_messages(sent_messages)
