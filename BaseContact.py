class BaseContact:
    def __init__(self, name, private_number, email):
        self.name = name
        self.private_number = private_number
        self.email = email

        self._label_length = 0

    @property
    def label_length(self):
        self._label_length = len(self.name)
        return self._label_length

    def __repr__(self):
        return f"Base(name={self.name} private_number={self.private_number}, email={self.email}, label_length={self.label_length})"

    def contact(self):
        print(f"Dzwonie do {self.name} na numer prywatny: {self.private_number}")
