import re


class FieldExtractor:

    def __init__(self, text):
        self.text = text
        self.lines = text.splitlines()

    def extract_name(self):

        match = re.search(
            r"Name of the Deceased Group Member\s*[-:]\s*([A-Za-z ]+)",
            self.text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

        match = re.search(
            r"Name of the Member\s*[:]\s*([A-Za-z ]+)",
            self.text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

        return "NOT FOUND"

    def extract_dob(self):

        match = re.search(
            r"Date of Birth\s*[-:]\s*([0-9]{1,2}[-/][A-Za-z]{3}[-/][0-9]{2,4})",
            self.text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

        return "NOT FOUND"

    def extract_gender(self):

        for line in self.lines:

            if "male" in line.lower():
                return "Male"

            if "female" in line.lower():
                return "Female"

        return "NOT FOUND"

    def extract_certificate_number(self):

        match = re.search(
            r"Certificate\s*No\s*[: ]*\s*(\d+)",
            self.text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

        return "NOT FOUND"

    def extract_policy_number(self):

        match = re.search(
            r"MN\d+",
            self.text
        )

        if match:
            return match.group()

        return "NOT FOUND"

    def extract_all(self):

        return {
            "Name": self.extract_name(),
            "DOB": self.extract_dob(),
            "Gender": self.extract_gender(),
            "Certificate Number":
                self.extract_certificate_number(),
            "Policy Number":
                self.extract_policy_number()
        }