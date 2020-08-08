class section:
    def __init__(self, cast, start_date):
        self.cast = cast.copy()
        self.start_date = start_date
        self.end_date = None

    def get_cast(self):
        return self.cast.copy()

    def get_start(self):
        return self.start_date

    def get_end(self):
        return self.end_date

    def set_end(self, end_date):
        self.end_date = end_date

    # checks if the section is closed
    def is_open(self):
        return self.get_end() == None

    # closes the section with a stop date
    def close(self, stop_date):
        if self.is_open():
            self.set_end(stop_date)
