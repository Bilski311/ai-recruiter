from user_input import UserInput
from modes import RecursiveMode, SingleMode
from dotenv import load_dotenv


class ContentGeneratorApp:
    def __init__(self):
        self.user_input = UserInput()

    def main_loop(self):
        while True:
            app_mode = self.user_input.get_app_mode()
            if app_mode == 'Q':
                break
            if app_mode == '1':
                recursive_mode = RecursiveMode(self.user_input)
                recursive_mode.run()
            elif app_mode == '2':
                single_mode = SingleMode(self.user_input)
                single_mode.run()


if __name__ == "__main__":
    load_dotenv()
    content_generator_app = ContentGeneratorApp()
    content_generator_app.main_loop()
