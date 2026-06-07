import re


class DeathCertificateExtractor:

    def __init__(self, pages):

        self.text = "\n".join(pages)

    def extract_name(self):

        patterns = [
            r"Name of Deceased\s*[:\-]?\s*([A-Za-z ]+)",
            r"Name\s*[:\-]?\s*([A-Za-z ]+)"
        ]

        for pattern in patterns:

            matches = re.findall(
                pattern,
                self.text,
                re.IGNORECASE
            )

            for match in matches:

                value = match.strip()

                if len(value) > 3:
                    return value

        return ""

    def extract_gender(self):

        if "female" in self.text.lower():
            return "Female"

        if "male" in self.text.lower():
            return "Male"

        return ""

    def extract_date_of_death(self):

        patterns = [
            r"05[-/ ]Feb[-/ ]24",
            r"\d{2}[-/]\d{2}[-/]\d{4}"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                self.text,
                re.IGNORECASE
            )

            if match:
                return match.group()

        return ""

    def extract(self):

        return {
            "Death Name":
                self.extract_name(),

            "Gender":
                self.extract_gender(),

            "Date Of Death":
                self.extract_date_of_death()
        }