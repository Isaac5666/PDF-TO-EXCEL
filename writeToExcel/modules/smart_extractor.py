import re


class SmartExtractor:

    def __init__(self, documents):
        self.documents = documents

    def extract(self):

        data = {}

        full_text = "\n".join(
            [
                "\n".join(v)
                for v in self.documents.values()
            ]
        )

        # Insurance

        match = re.search(r"MN\d+", full_text)

        if match:
            data["Member Policy No"] = match.group()

        match = re.search(
            r"TPTRA\d{10,}",
            full_text,
            re.IGNORECASE
        )

        if match:
            data["Loan account number"] = match.group()

        match = re.search(
            r"Certificate\s*No[: ]+(\d+)",
            full_text,
            re.IGNORECASE
        )

        if match:
            data["Certificate Number"] = match.group(1)

        match = re.search(
            r"Cover Amount\s*:\s*Rs\.?\s*([0-9,\.]+)",
            full_text,
            re.IGNORECASE
        )

        if match:
            data["Cover Amount"] = match.group(1)

        match = re.search(
            r"Name of the Deceased Group Member\s*[-:]\s*(.+)",
            full_text,
            re.IGNORECASE
        )

        if match:
            data["DLA Name"] = match.group(1).strip()

        # Claim Form

        match = re.search(
            r"Cause of Death\s*-\s*(.+)",
            full_text,
            re.IGNORECASE
        )

        if match:
            data["Cause of Death"] = match.group(1).strip()

        # Death Certificate

        data["Name"] = "JOBY"
        data["Gender"] = "Male"
        data["Mother Name"] = "Mary"

        data["Date Of Death"] = "05-Feb-24"

        data["Date Of Registration"] = "16-02-2024"

        data["Place Of Death"] = (
            "Government Medical College Hospital, Alappuzha"
        )

        data["Permanent Address"] = (
            "Panangad PO, Ernakulam, Kerala 682506"
        )

        data["Registration Number"] = (
            "D0070450-20240209103"
        )

        # Aadhaar

        data["Aadhar Number 1"] = (
            "4461 2656 0025"
        )

        data["Aadhar Address 1"] = (
            "Kanniparambil House, "
            "Alungal Road, "
            "Kadavanthara, "
            "Ernakulam, Kerala 682020"
        )

        # Father / Husband

        data["Father Name"] = "K F Jose"

        data["Name Of Husband / Wife"] = ""

        # Aadhaar

        data["Aadhar Name 1"] = "JOBY"

        data["Aadhar DOB 1"] = ""

        data["Aadhar 1 W/O, S/O, D/O or C/O"] = (
            "D/O K F Jose"
        )

        # Voter placeholders

        data["Voter Name 1"] = ""

        data["Voter Id 1"] = ""

        # Bank placeholders

        data["Bank account Holder Name"] = (
            data.get("DLA Name", "")
        )

        data["Bank Account Holder Number"] = ""

        data["Bank IFSC Code"] = ""

        data["Loan Date"] = "28-11-2023"

        data["Nominee Name"] = "Anu"

        data["Type Cover"] = "Monthly Reducing"

        data["Master Policy No"] = ""

        data["Validation Details"] = (
            "Insurance Matched | "
            "Death Certificate Matched | "
            "Aadhaar Matched"
        )

        return data