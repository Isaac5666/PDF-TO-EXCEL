import re


class InsuranceExtractor:

    def __init__(self, insurance_pages):
        self.text = "\n".join(insurance_pages)

    def get_member_policy_no(self):

        match = re.search(
            r"MN\d+",
            self.text,
            re.IGNORECASE
        )

        if match:
            return match.group()

        return ""

    def get_certificate_no(self):

        match = re.search(
            r"Certificate\s*No\s*[:\-]?\s*(\d+)",
            self.text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

        return ""

    def get_dla_name(self):

        import re

        matches = re.findall(
            r"Name of the Member\s*:\s*(.+)",
            self.text,
            re.IGNORECASE
        )

        valid_names = []

        for match in matches:

            candidate = match.strip()

            if "=" in candidate:
                continue

            if "[" in candidate:
                continue

            if len(candidate) < 3:
                continue

            if "policy" in candidate.lower():
                continue

            valid_names.append(candidate)

        if valid_names:
            return valid_names[-1]

        return ""

    def get_dob(self):

        patterns = [
            r"\d{1,2}/[A-Za-z]{3}/\d{4}",
            r"\d{1,2}-[A-Za-z]{3}-\d{2}",
            r"\d{1,2}-[A-Za-z]{3}-\d{4}"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                self.text
            )

            if match:
                return match.group()

        return ""

    def get_cover_amount(self):

        match = re.search(
            r"Cover Amount\s*:\s*Rs\.?\s*([0-9,\.]+)",
            self.text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

        return ""

    def extract(self):

        with open(
            "output/insurance_debug.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(self.text)

        return {
            "Member Policy No":
                self.get_member_policy_no(),

            "Certificate Number":
                self.get_certificate_no(),

            "DLA Name":
                self.get_dla_name(),

            "DOB":
                self.get_dob(),

            "Cover Amount":
                self.get_cover_amount()
        }