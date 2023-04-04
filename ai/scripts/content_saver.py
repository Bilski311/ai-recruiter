class ContentSaver:
    def send_to_backend(self, generator, output):
        if output is not None:
            if input("Send the result to backend? (Y/N) ").upper() == 'Y':
                generator.save_all(output)
