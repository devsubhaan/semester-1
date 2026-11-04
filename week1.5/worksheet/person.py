# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, nname, nbirth):
        """
        Initialises the class
        """
        if not isinstance(nname, str):
            raise(TypeError)
        elif nname == "":
            raise(ValueError)

        if not isinstance(nbirth, date):
            raise(TypeError)

        self.name = nname
        self.birth = nbirth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """
        Returns the initials of the person
        """
        ret = ""
        for name in self.name.split():
            ret += name[0].upper()

        return ret

    def is_birthday(self):
        """
        Returns true if the persons birthday is today
        """
        if date.today() == self.birth:
            return True
        return False


"""
test = Person("John Smith", date.fromisoformat('2025-12-04'))
print(test.initials())
print(test.is_birthday())

test2 = Person("Mundane Mann", date.fromisoformat('2026-11-04'))
print(test2.initials())
print(test2.is_birthday())

test3 = Person("Pablo Diego José Francisco de Paula Juan Nepomuceno María de los Remedios Cipriano de la Santísima Trinidad Ruiz y Picasso", date.fromisoformat('2026-11-04'))
print(test3.initials())
print(test3.is_birthday())
"""