class ContentSaver:
    def send_to_backend(self, generator, output, ask_before_saving=True):
        if output is not None:
            if ask_before_saving is False:
                generator.save_all(output)
                return
            elif input("Send the result to backend? (Y/N) ").upper() == 'Y':
                generator.save_all(output)
