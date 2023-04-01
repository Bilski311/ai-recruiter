import sys

from chat_utils import generate_chat_output
from config import output_types


def generate(output_type, subject_type):
    output_type_config = output_types[output_type]
    system_template = output_type_config['system_template']
    human_template = output_type_config['human_template']

    output = generate_chat_output(
        subject_type, system_template, human_template)
    print(output)


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Proper usage: python3 generate.py <output_type> <subject_type>")
    elif sys.argv[1].upper() not in output_types.keys():
        print("Available types: ")
        for key in output_types.keys():
            print(key)
    else:
        output_type = sys.argv[1].upper()
        subject_type = sys.argv[2]
        generate(output_type, subject_type)
