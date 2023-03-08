class Screen:
    def prompt_message(self, msg: str):
        result = input(msg)
        if result is None:
            return None
        else:
            return result

    def show_message(self, msg: str):
        print(msg)