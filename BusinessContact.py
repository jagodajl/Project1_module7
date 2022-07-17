from BaseContact import BaseContact


class BusinessContact(BaseContact):
    def __init__(self, job, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_number = business_number

    def __repr__(self):
        return f"Business(name={self.name} private_number={self.private_number}, email={self.email},job={self.job}, company={self.company}, business_number={self.business_number}, label_length={self.label_length})"

    def contact(self):
        print(f"Dzwonie do {self.name} na numer firmowy: {self.business_number}")
