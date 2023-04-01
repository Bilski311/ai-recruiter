import json
import argparse

from chat_utils import generate_chat_output
from mongo_utils import save_to_mongo
from config import output_types


def generate(output_type, subject_type, save_result):
    output_type_config = output_types[output_type]
    system_template = output_type_config['system_template']
    human_template = output_type_config['human_template']

    output = generate_chat_output(
        subject_type, system_template, human_template)
    print(output)

    if save_result:
        collection = output_type_config['collection']
        save_to_mongo(json.loads(output), collection)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_type", help="Output type (e.g., TOPIC, SUBTOPIC, QUESTION)")
    parser.add_argument("subject_type", help="Subject type (e.g., JavaScript)")
    parser.add_argument("--save", action="store_true",
                        help="Save the result to MongoDB")

    args = parser.parse_args()

    if args.output_type.upper() not in output_types.keys():
        print("Available types: ")
        for key in output_types.keys():
            print(key)
    else:
        output_type = args.output_type.upper()
        subject_type = args.subject_type
        generate(output_type, subject_type, args.save)
