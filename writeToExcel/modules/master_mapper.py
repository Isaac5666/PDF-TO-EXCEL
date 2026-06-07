from modules.schema import EXCEL_FIELDS


class MasterMapper:

    def __init__(self):

        self.data = EXCEL_FIELDS.copy()

    def add_insurance_data(self, insurance_data):

        self.data["Member Policy No"] = (
            insurance_data.get(
                "Member Policy No",
                ""
            )
        )

        self.data["DLA Name"] = (
            insurance_data.get(
                "DLA Name",
                ""
            )
        )

        self.data["Cover Amount"] = (
            insurance_data.get(
                "Cover Amount",
                ""
            )
        )

    def add_death_data(self, death_data):

        self.data["Name"] = (
            death_data.get(
                "Death Name",
                ""
            )
        )

        self.data["Gender"] = (
            death_data.get(
                "Gender",
                ""
            )
        )

        self.data["Date Of Death"] = (
            death_data.get(
                "Date Of Death",
                ""
            )
        )

    def add_aadhaar_data(self, aadhaar_data):

        self.data["Aadhar Name 1"] = (
            aadhaar_data.get(
                "Aadhar Name 1",
                ""
            )
        )

        self.data["Aadhar Number 1"] = (
            aadhaar_data.get(
                "Aadhar Number 1",
                ""
            )
        )

        self.data["Aadhar DOB 1"] = (
            aadhaar_data.get(
                "Aadhar DOB 1",
                ""
            )
        )

    def set_accuracy(self, accuracy):

        self.data["Accuracy %"] = (
            f"{accuracy}%"
        )

    def get_data(self):

        return self.data