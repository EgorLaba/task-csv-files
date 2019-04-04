import csv


class DataWorker:
    def __init__(self, filename):
        self.__filename = filename

    @property
    def file_name(self):
        return self.__filename

    @property
    def users_count(self):
        count = 0
        with open('users.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                count += 1
            return count

    @property
    def average_salary(self):
        count = 0
        users_sum = 0
        with open('users.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                count += 1
                users_sum += float(row['salary'])
            return round(users_sum / count, 1)

    @property
    def average_age(self):
        count = 0
        users_age = 0
        with open('users.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                count += 1
                users_age += float(row['age'])
            return round(users_age / count, 1)

    def get_users(self):
        ArrayList = []
        with open('users.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                usersDictionary = {}
                for key, value in row.items():
                 usersDictionary[key] = value
                ArrayList.append(usersDictionary)
            return ArrayList

    def get_users_by_gender(self, gender):
        ArrayList = []
        if (gender == "male" or gender == "female"):
            with open('users.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if gender == row['gender']:
                        dictionary = {}
                        for key, value in row.items():
                            dictionary[key] = value
                        ArrayList.append(dictionary)
                return ArrayList
        else:
            errDict = { "error": "gender must be male, or female" }
            return errDict














