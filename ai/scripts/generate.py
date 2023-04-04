from generators.topic_generator import TopicGenerator
from generators.subtopic_generator import SubtopicGenerator
from generators.question_generator import QuestionGenerator


def get_generator(output_type):
    if output_type == 'TOPIC':
        return TopicGenerator()
    elif output_type == 'SUBTOPIC':
        return SubtopicGenerator()
    elif output_type == 'QUESTION':
        return QuestionGenerator()
    else:
        return None


def generate(output_type, subject_type, number):
    generator = get_generator(output_type)
    output = None
    if generator:
        output = generator.generate(subject_type, number)
        print(output)
    else:
        print(f"Invalid output type: {output_type}")
        return

    if input("Save the result to MongoDB? (Y/N) ").upper() == 'Y':
        generator.save_all(output)


def main():
    available_types = ['TOPIC', 'SUBTOPIC', 'QUESTION']

    while True:
        print("\nAvailable types: ")
        for key in available_types:
            print(key)

        output_type = input(
            "\nEnter the output type or 'EXIT' to quit: ").upper()
        if output_type == 'EXIT':
            break

        subject_type = input("Enter the subject type: ")
        number = int(input("Enter the number of outputs: "))

        generate(output_type, subject_type, number)


if __name__ == "__main__":
    main()
