class section:
    def __init__(self, cast, start_message, end_message):
        self.cast = cast.copy()
        self.start_message = start_message
        self.end_message = end_message

    def __str__(self):
        output = {
            "cast": self.get_cast(),
            "start_date": self.get_start(),
            "end_date": self.get_end()
        }
        return str(output)

    def get_cast(self):
        return self.cast.copy()

    def get_start(self):
        return self.start_message

    def get_end(self):
        return self.end_message

    def update_cast(self, cast):
        self.cast = cast 
    # # checks if the section is closed
    # def is_open(self):
    #     return self.get_end() == None
    #
    # # closes the section with a stop date
    # def close(self, stop_date):
    #     if self.is_open():
    #         self.end_date = stop_date
    #     return self.end_date
