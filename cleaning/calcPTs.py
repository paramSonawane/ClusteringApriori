import pandas as pd;
# from random import randint
# ageDF = pd.read_csv("ID_Age.csv");
itemsDF = pd.read_csv("new.csv",header=None);

n = len(itemsDF.index);

pt = []

for i in range(300) :
    pts = 0

    for j in range(20) :
        if not pd.isnull(itemsDF.values[i,j]) :
            pts += len(itemsDF.values[i,j])

    pt.append(pts)

print(pt);

# a = open("st_data.csv", "r");
# b = open("newWithPts", "w+")

# for i in range(0, 7501):
#     line = a.readline();
#     line2 = line + "," + str(len(line)-20) + "," + str(randint(1, 1000)) + "\n";
#     b.write(line2);

# print("Done")