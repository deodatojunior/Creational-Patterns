from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('Personal Section')


class AlbumSection(Section):
    def describe(self):
        print('Album Section')


class PatentSection(Section):
    def describe(self):
        print('Patent Section')


class PublicationSection(Section):
    def describe(self):
        print('Publication Section')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = list()
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return [type(s).__name__ for s in self.sections]

    def add_section(self, section):
        self.sections.append(section)


class Linkedin(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':

    linkedin = Linkedin()
    facebook = Facebook()

    print('Creating Profile...', type(linkedin).__name__)
    print('Profile has sections --', linkedin.get_sections())

    print('Creating Profile...', type(facebook).__name__)
    print('Profile has sections --', facebook.get_sections())