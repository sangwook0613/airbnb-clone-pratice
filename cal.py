import calendar  # calendar를 import해야되기에 파일 명은 calendar로 하면 안된다!


class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.day_names = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_month(self):
        return self.months[self.month - 1]
