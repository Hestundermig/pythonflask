class spoerg:

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

if __name__ == '__main__':

    jeg_spoerg = spoerg()
    print("Har du haft en god dag?")
    while True:
        action = input("[Y] Yep | [N] Nej - ").upper()
        if action not in "ABOS" or len(action) != 1:

            if 'Nej' == print:("Hvorfor ikke det? ")

            print("Har du været i skole idag?")

        action = input("[Y] Yep | [N] Nej - ").upper()
        if action not in "ABOS" or len(action) != 1:
            quit("Der er ikke flere spørgsmål")

# python "spørgsmål.py"