class InvalidSocial(Exception):
    pass


class InvalidPassword(Exception):
    pass


class Email:

    def __init__(self, email):
        try:
            a, b = email.split("@")
            c, d = b.split(".")
            self.email = email
        except ImportError:
            raise InvalidEmail

    def __str__(self):
        return self.email


class SS:

    def __init__(self, social):
        try:
            AAA, BB, CCCC = social.split("-")
            int(AAA)
            int(BB)
            int(CCCC)
        except IndexError:
            raise InvalidSocial
        except ValueError:
            raise InvalidSocial


class Hash:
    def __init__(self, passwd):
        if len(passwd) > 7:
            self.hash = self.generate_hash(passwd)
        else:
            raise InvalidPassword

    def __eq__(self, passwd):
        return self.hash == self.generate_hash(passwd)

    def generate_hash(self, passwd):
        return random.randint(1, 2)
