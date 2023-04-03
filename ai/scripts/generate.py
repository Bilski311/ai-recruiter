import json
import argparse

from chat_utils import generate_chat_output
from backend_client import save_topics
from config import output_types
from arguments import Arguments


def generate(output_type, subject_type, number, save_result, confirm_needed):
    output_type_config = output_types[output_type]
    system_template = output_type_config['system_template']
    human_template = output_type_config['human_template']

    output = generate_chat_output(system_template, human_template, subject=subject_type, number=number)
    print(output)

    if save_result:
        if confirm_needed:
            answer = input('Save the result?[Y/N]')
            if answer == 'N':
                return
        save_topics(json.loads(output))


if __name__ == "__main__":
    args = Arguments()

    if args.output_type not in output_types.keys():
        print("Available types: ")
        for key in output_types.keys():
            print(key)
    else:
        output_type = args.output_type
        subject_type = args.subject_type
        number = args.number
        generate(output_type, subject_type, number, args.save, args.confirm_needed)