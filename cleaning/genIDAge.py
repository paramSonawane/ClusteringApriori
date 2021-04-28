from random import randint

a = open("./ID_Age.csv", "w+");

for id in range(1, 1000):
    d = "";
    d = d + str(id) + "," + str(randint(17, 80)) + "\n"
    a.write(d)

a.close();
