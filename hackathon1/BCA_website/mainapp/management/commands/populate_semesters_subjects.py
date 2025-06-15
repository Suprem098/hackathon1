from django.core.management.base import BaseCommand
from mainapp.models import Semester, Subject

class Command(BaseCommand):
    help = 'Populate semesters and subjects with sample data'

    def handle(self, *args, **kwargs):
        semesters_subjects = {
            'first': ['Mathematics I', 'Computer Fundamentals', 'English', 'Environmental Studies'],
            'second': ['Mathematics II', 'Data Structures', 'Digital Electronics', 'Communication Skills'],
            'third': ['Database Management', 'Operating Systems', 'Software Engineering', 'Computer Networks'],
            'fourth': ['Web Technologies', 'Theory of Computation', 'Microprocessors', 'Object Oriented Programming'],
            'fifth': ['Artificial Intelligence', 'Mobile Computing', 'Cloud Computing', 'Cyber Security'],
            'sixth': ['Machine Learning', 'Big Data Analytics', 'Internet of Things', 'Data Mining'],
            'seventh': ['Project Work', 'Seminar', 'Elective I', 'Elective II'],
            'eight': ['Project Work', 'Seminar', 'Elective III', 'Elective IV'],
        }

        for sem_name, subjects in semesters_subjects.items():
            semester, created = Semester.objects.get_or_create(name=sem_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Semester "{sem_name}" created.'))
            else:
                self.stdout.write(f'Semester "{sem_name}" already exists.')

            for subject_name in subjects:
                subject, created = Subject.objects.get_or_create(semester=semester, name=subject_name)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  Subject "{subject_name}" added to semester "{sem_name}".'))
                else:
                    self.stdout.write(f'  Subject "{subject_name}" already exists in semester "{sem_name}".')
