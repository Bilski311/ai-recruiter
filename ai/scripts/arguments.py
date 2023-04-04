import argparse


class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "output_type", help="Output type (e.g., TOPIC, SUBTOPIC, QUESTION)")
        parser.add_argument(
            "subject_type", help="Subject type (e.g., JavaScript)")
        parser.add_argument("number", help="Number of outputs")
        parser.add_argument("--save", action="store_true",
                            help="Save the result to MongoDB")
        parser.add_argument("--confirm-needed", action="store_true",
                            help="Save the result to MongoDB")
        self.args = parser.parse_args()

    @property
    def output_type(self):
        return self.args.output_type.upper()

    @property
    def subject_type(self):
        return self.args.subject_type

    @property
    def number(self):
        return self.args.number

    @property
    def save(self):
        return self.args.save

    @property
    def confirm_needed(self):
        return self.args.confirm_needed
