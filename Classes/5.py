class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = int(skills)

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        else:
            return f'{self.name} does not know {language}'

    def change_language(self, new_lang, skills_needed):
        if self.skills >= skills_needed and self.language != new_lang:
            old_lang = self.language
            self.language = new_lang
            return f'{self.name} switched from {old_lang} to {new_lang}'
        elif self.skills >= skills_needed and self.language == new_lang:
            return f'{self.name} already knows {new_lang}'
        else:
            return f'{self.name} needs {skills_needed-self.skills} more skills'


