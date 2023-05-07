class UserInput:
    def get_app_mode(self):
        print("\nSelect mode:")
        print("1. Recursive")
        print("2. Single")
        print("Q. Quit")
        choice = input("Enter your choice: ").upper()
        return choice

    def get_job_position(self):
        return input("Enter the job position: ")

    def get_number_of_topics(self):
        return int(input("Enter the number of topics: "))

    def get_number_of_subtopics(self):
        return int(input("Enter the number of subtopics: "))

    def get_number_of_flashcards(self):
        return int(input("Enter the number of flashcards: "))

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

    def get_generation_mode(self):
        print("\nSelect generation mode:")
        print("1. Generate from scratch")
        print("2. Continue with existing content")
        choice = int(input("Enter your choice: "))
        return choice
