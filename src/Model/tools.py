class MessageHandler:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages


if __name__ == "__main__":
    print("tests of tools...")
