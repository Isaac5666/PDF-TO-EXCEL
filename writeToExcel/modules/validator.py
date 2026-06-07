import re
from datetime import datetime


class Validator:

    def __init__(self, data):
        self.data = data

    def normalize_name(self):

        name = self.data.get("Name", "")

        name = re.sub(r"[^A-Za-z ]", "", name)

        name = " ".join(name.split())

        self.data["Name"] = name

    def normalize_dob(self):

        dob = self.data.get("DOB", "")

        formats = [
            "%d-%b-%y",
            "%d-%b-%Y",
            "%d/%b/%Y",
            "%d/%m/%Y"
        ]

        for fmt in formats:

            try:

                date_obj = datetime.strptime(
                    dob,
                    fmt
                )

                self.data["DOB"] = (
                    date_obj.strftime(
                        "%d-%m-%Y"
                    )
                )

                return

            except:
                pass

    def validate(self):

        self.normalize_name()

        self.normalize_dob()

        return self.data