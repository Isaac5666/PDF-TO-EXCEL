class FinalValidator:

    def validate(self, data):

        score = 0

        checks = []

        important_fields = [

            "Member Policy No",
            "Loan account number",
            "DLA Name",
            "Cover Amount",
            "Date Of Death",
            "Registration Number",
            "Aadhar Number 1",
            "Permanent Address",
            "Place Of Death",
            "Name"
        ]

        for field in important_fields:

            if data.get(field):

                score += 10

                checks.append(
                    f"{field} OK"
                )

        data["Accuracy %"] = (
            f"{min(score,100)}%"
        )

        data["Validation Details"] = (
            " | ".join(checks)
        )

        return data