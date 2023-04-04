class UserInput:
    def get_app_mode(self):
        print("\nSelect mode:")
        print("1. Recursive")
        print("2. Single")
        print("Q. Quit")
        choice = input("Enter your choice: ").upper()
        return choice

    def get_output_type(self):
        available_types = ['TOPIC', 'SUBTOPIC', 'FLASHCARD']

        print("\nCreate a: \n")
        for key in available_types:
            print(key)

        output_type = input(
            "\nEnter the output type(q to quit): ").upper()

        return output_type

    def get_subject_type(self):
        return input("Enter the subject type: ")

    def get_number_of_outputs(self):
        return int(input("Enter the number of outputs: "))
