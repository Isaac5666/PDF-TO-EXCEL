import re


class AadhaarExtractor:

    def __init__(self, pages):

        self.text = "\n".join(pages)

    def extract_name(self):

        lines = self.text.split("\n")

        for line in lines:

            line = line.strip()

            if len(line) < 3:
                continue

            if any(char.isdigit() for char in line):
                continue

            if "government" in line.lower():
                continue

            if len(line.split()) >= 2:
                return line

        return ""

    def extract_dob(self):

        patterns = [
            r"\d{2}/\d{2}/\d{4}",
            r"\d{2}-\d{2}-\d{4}",
            r"\d{2}/[A-Za-z]{3}/\d{4}"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                self.text
            )

            if match:
                return match.group()

        return ""

    def extract_aadhaar(self):

        match = re.search(
            r"\d{4}\s*\d{4}\s*\d{4}",
            self.text
        )

        if match:

            aadhaar = re.sub(
                r"\D",
                "",
                match.group()
            )

            return (
                aadhaar[0:]
            )

        return ""

    def extract(self):

        return {

            "Aadhar Name 1":
                self.extract_name(),

            "Aadhar Number 1":
                self.extract_aadhaar(),

            "Aadhar DOB 1":
                self.extract_dob()
        }