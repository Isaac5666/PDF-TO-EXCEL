class TXTFormatter:

    def save_report(
        self,
        data,
        output_file="output/formatted_report.txt"
    ):

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "=" * 50 + "\n"
            )

            file.write(
                "DOCUMENT EXTRACTION REPORT\n"
            )

            file.write(
                "=" * 50 + "\n\n"
            )

            for key, value in data.items():

                file.write(
                    f"{key}: {value}\n"
                )

        return output_file