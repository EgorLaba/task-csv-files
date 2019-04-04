from DataWorker import DataWorker
import unittest

all_users_json = [{"firstName": "tom", "lastName": "tomcat", "gender": "male", "age": "25", "country": "USA", "city": "New York", "salary": "1500"}, {"firstName": "martins", "lastName": "alves", "gender": "male", "age": "52", "country": "BR", "city": "rio branco", "salary": "5200"}, {"firstName": "adeci", "lastName": "barros", "gender": "female", "age": "45", "country": "BR", "city": "araras", "salary": "4500"}, {"firstName": "joshua", "lastName": "diaz", "gender": "male", "age": "50", "country": "AU", "city": "mackay", "salary": "5000"}, {"firstName": "sky", "lastName": "mauritz", "gender": "male", "age": "23", "country": "NL", "city": "amstelveen", "salary": "2300"}, {"firstName": "aada", "lastName": "rinne", "gender": "female", "age": "67", "country": "FI", "city": "vehmaa", "salary": "6700"}, {"firstName": "matthew", "lastName": "roy", "gender": "male", "age": "67", "country": "CA", "city": "summerside", "salary": "6700"}, {"firstName": "alma", "lastName": "mercier", "gender": "female", "age": "66", "country": "CH", "city": "rickenbach (tg)", "salary": "6600"}, {"firstName": "adrian", "lastName": "pastor", "gender": "male", "age": "62", "country": "ES", "city": "albacete", "salary": "6200"}, {"firstName": "christina", "lastName": "harris", "gender": "female", "age": "39", "country": "GB", "city": "ripon", "salary": "3900"}, {"firstName": "fl\u00e1vio", "lastName": "silveira", "gender": "male", "age": "33", "country": "BR", "city": "florian\u00f3polis", "salary": "3300"}, {"firstName": "samuel", "lastName": "lambert", "gender": "male", "age": "49", "country": "AU", "city": "bendigo", "salary": "4900"}, {"firstName": "arttu", "lastName": "koskela", "gender": "male", "age": "24", "country": "FI", "city": "kumlinge", "salary": "2400"}, {"firstName": "capucine", "lastName": "vincent", "gender": "female", "age": "53", "country": "FR", "city": "limoges", "salary": "5300"}, {"firstName": "walda", "lastName": "de souza", "gender": "female", "age": "36", "country": "BR", "city": "patos de minas", "salary": "3600"}, {"firstName": "suzana", "lastName": "menard", "gender": "female", "age": "49", "country": "CH", "city": "lampenberg", "salary": "4900"}, {"firstName": "evaristo", "lastName": "oliveira", "gender": "male", "age": "40", "country": "BR", "city": "parna\u00edba", "salary": "4000"}, {"firstName": "kenneth", "lastName": "hilpert", "gender": "male", "age": "52", "country": "DE", "city": "bopfingen", "salary": "5200"}, {"firstName": "indie", "lastName": "edwards", "gender": "female", "age": "67", "country": "NZ", "city": "rotorua", "salary": "6700"}, {"firstName": "britney", "lastName": "hansen", "gender": "female", "age": "47", "country": "IE", "city": "wexford", "salary": "4700"}, {"firstName": "emilia", "lastName": "alvarez", "gender": "female", "age": "68", "country": "ES", "city": "sevilla", "salary": "6800"}, {"firstName": "phoebe", "lastName": "thomas", "gender": "female", "age": "49", "country": "NZ", "city": "auckland", "salary": "4900"}, {"firstName": "theodore", "lastName": "evans", "gender": "male", "age": "23", "country": "NZ", "city": "invercargill", "salary": "2300"}]

male_users_json = [{"firstName": "tom", "lastName": "tomcat", "gender": "male", "age": "25", "country": "USA", "city": "New York", "salary": "1500"}, {"firstName": "martins", "lastName": "alves", "gender": "male", "age": "52", "country": "BR", "city": "rio branco", "salary": "5200"}, {"firstName": "joshua", "lastName": "diaz", "gender": "male", "age": "50", "country": "AU", "city": "mackay", "salary": "5000"}, {"firstName": "sky", "lastName": "mauritz", "gender": "male", "age": "23", "country": "NL", "city": "amstelveen", "salary": "2300"}, {"firstName": "matthew", "lastName": "roy", "gender": "male", "age": "67", "country": "CA", "city": "summerside", "salary": "6700"}, {"firstName": "adrian", "lastName": "pastor", "gender": "male", "age": "62", "country": "ES", "city": "albacete", "salary": "6200"}, {"firstName": "fl\u00e1vio", "lastName": "silveira", "gender": "male", "age": "33", "country": "BR", "city": "florian\u00f3polis", "salary": "3300"}, {"firstName": "samuel", "lastName": "lambert", "gender": "male", "age": "49", "country": "AU", "city": "bendigo", "salary": "4900"}, {"firstName": "arttu", "lastName": "koskela", "gender": "male", "age": "24", "country": "FI", "city": "kumlinge", "salary": "2400"}, {"firstName": "evaristo", "lastName": "oliveira", "gender": "male", "age": "40", "country": "BR", "city": "parna\u00edba", "salary": "4000"}, {"firstName": "kenneth", "lastName": "hilpert", "gender": "male", "age": "52", "country": "DE", "city": "bopfingen", "salary": "5200"}, {"firstName": "theodore", "lastName": "evans", "gender": "male", "age": "23", "country": "NZ", "city": "invercargill", "salary": "2300"}]

female_users_json = [{"firstName": "adeci", "lastName": "barros", "gender": "female", "age": "45", "country": "BR", "city": "araras", "salary": "4500"}, {"firstName": "aada", "lastName": "rinne", "gender": "female", "age": "67", "country": "FI", "city": "vehmaa", "salary": "6700"}, {"firstName": "alma", "lastName": "mercier", "gender": "female", "age": "66", "country": "CH", "city": "rickenbach (tg)", "salary": "6600"}, {"firstName": "christina", "lastName": "harris", "gender": "female", "age": "39", "country": "GB", "city": "ripon", "salary": "3900"}, {"firstName": "capucine", "lastName": "vincent", "gender": "female", "age": "53", "country": "FR", "city": "limoges", "salary": "5300"}, {"firstName": "walda", "lastName": "de souza", "gender": "female", "age": "36", "country": "BR", "city": "patos de minas", "salary": "3600"}, {"firstName": "suzana", "lastName": "menard", "gender": "female", "age": "49", "country": "CH", "city": "lampenberg", "salary": "4900"}, {"firstName": "indie", "lastName": "edwards", "gender": "female", "age": "67", "country": "NZ", "city": "rotorua", "salary": "6700"}, {"firstName": "britney", "lastName": "hansen", "gender": "female", "age": "47", "country": "IE", "city": "wexford", "salary": "4700"}, {"firstName": "emilia", "lastName": "alvarez", "gender": "female", "age": "68", "country": "ES", "city": "sevilla", "salary": "6800"}, {"firstName": "phoebe", "lastName": "thomas", "gender": "female", "age": "49", "country": "NZ", "city": "auckland", "salary": "4900"}]

error = {
    "error": "gender must be male, or female"
}

worker = DataWorker("users.csv")


class TestWorker(unittest.TestCase):
    def test_file_name_1(self):
        self.assertEqual(worker.file_name, "users.csv")

    def test_file_name_2(self):
        self.assertEqual(DataWorker("data.csv").file_name, "data.csv")
    
    def test_users_count(self):
        self.assertEqual(worker.users_count, 23)
    
    def test_average_salary(self):
        self.assertEqual(worker.average_salary, 4678.3)
    
    def test_average_age(self):
        self.assertEqual(worker.average_age, 47.2)

    def test_get_users(self):
        self.assertListEqual(worker.get_users(), all_users_json)
    
    def test_get_users_by_gender_male(self):
        self.assertListEqual(worker.get_users_by_gender("male"), male_users_json)
    
    def test_get_users_by_gender_female(self):
        self.assertListEqual(worker.get_users_by_gender("female"), female_users_json)

    def test_get_users_by_gender_error_1(self):
        self.assertDictEqual(worker.get_users_by_gender(2019), error)
    
    def test_get_users_by_gender_error_2(self):
        self.assertDictEqual(worker.get_users_by_gender("mele"), error)

unittest.main()