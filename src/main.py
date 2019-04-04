from DataWorker import DataWorker
worker1 = DataWorker("users.csv")
print(worker1.get_users_by_gender('123123male'))
