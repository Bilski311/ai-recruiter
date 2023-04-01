import sys

from chat_utils import generate_chat_output
from config import output_types


def generate(type, subject):
    output_type = output_types[type]
    output = generate_chat_output(
        subject, output_type['system_template'], output_type['human_template'])
    print(output)


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Proper usage: python3 generate.py <output_type> <subject_type>")
    elif sys.argv[1] not in output_types.keys():
        print("Available types: ")
        for key in output_types.keys():
            print(key)
    else:
        type = sys.argv[1]
        subject = sys.argv[2]
        generate(type, subject)
