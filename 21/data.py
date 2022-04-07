import aocd

SESSION_ID = "53616c7465645f5f4963b68e41ac272b6efc924bde3a50262103a70e98c003e4bada61305dd829d5cd1198b0baa7d8a05149c7ceb8ea512cf40a6565b72a7a92"
YEAR = 2021


class Data:
    session = SESSION_ID
    year = YEAR

    def __init__(self, day):
        self.day = day
        self.data = aocd.get_data(session=self.session, day=self.day, year=self.year)
        self.data_str = self.data.split()

    def get_int(self):
        return [int(entry) for entry in self.data_str]

    def get_preview(self):
        print(self.data_str)
