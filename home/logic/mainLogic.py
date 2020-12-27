import pandas as pd
from numpy import append, array

from os.path import join as ospJoin
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

from sklearn.cluster import KMeans
from apyori import apriori

apdata = {}

# prepares dictionary of apr function
def apdata_prepare(fileName, labels, l_ids):
	tempAPData = {}

	labelLookup = {}

	i = 0
	for id in l_ids:
		labelLookup[id] = labels[i]
		i += 1

	df = pd.read_csv(fileName, header=None)

	n = len(df.index)

	for i in range(n):
		s = df.iloc[i]
		s = list(s.dropna())
		id = s[0]
		if labelLookup[id] in tempAPData:
			tempAPData[labelLookup[id]] += [s[1:]]
		else:
			tempAPData[labelLookup[id]] = [s[1:]]

	return tempAPData


# kmean returns cluster centers, labels of data, x,y,z list of points to plot
def kmean():
	print("started kmeans")
	global apdata

	df = pd.read_csv(ospJoin(BASE_DIR,'home/logic/CSVs/mall.csv'))
	df = df.rename(columns={'Annual Income (k$)': 'Annual_income', 'Spending Score (1-100)': 'Spending_score'})

	kmeansAttrs = df.loc[:,["Age", "Annual_income", "Spending_score"]]

	km = KMeans(n_clusters=5, random_state=0).fit(kmeansAttrs)

	apdata = apdata_prepare(ospJoin(BASE_DIR,'home/logic/CSVs/new_purchase.csv'), km.labels_, df['CustomerID'])

	labels = append(km.labels_, [(len(km.cluster_centers_)+1) for i in range(len(km.cluster_centers_))], axis=0)

	clusterInfo = kmeansAttrs.append(pd.DataFrame(km.cluster_centers_.tolist(), columns=["Age", "Annual_income","Spending_score"]), ignore_index = True)
	print("end kmeans")

	return clusterInfo, labels

# Takes input as cluster label and performs apriori mining on that cluster
def apr(clust_label):
	ar = apriori(apdata[clust_label], min_support = 0.005, min_confidence= 0.4, min_lift= 4)
	results = list(ar)
	d = {}
	i = 0
	for record in results:
		l = []
		l.append(record[1])
		l.append(list(record[2][0][0]))
		l.append(list(record[2][0][1]))
		l.append(record[2][0][2])
		l.append(record[2][0][3])
		d[i] = l
		i += 1
	return d


def extract_ids(age, id, age_min, age_max):
	s = set()
	n = len(age)
	for i in range(n):
		if (age[i] >= age_min and age[i] <= age_max):
			s.add(id[i])
	return s

def extract_transactions(df_trans, sid):
	l = []
	n = len(df_trans.index)
	for i in range(n):
		s = df_trans.iloc[i]
		s = list(s.dropna())
		if s[0] in sid:
			l.append(s[1:])
	return l


# takes age range and gives apriori results for that age range

glob_state = {}
def giveAssocOnAgeRange(age_min, age_max):
	df = pd.read_csv(ospJoin(BASE_DIR,'home/logic/CSVs/mall.csv'))
	df_trans = pd.read_csv(ospJoin(BASE_DIR,'home/logic/CSVs/new_purchase.csv'), header=None)
	sid = extract_ids(df['Age'].tolist(), df['CustomerID'].tolist(), age_min, age_max)
	list_of_transactions = extract_transactions(df_trans, sid)
	ar = apriori(list_of_transactions, min_support = 0.004, min_confidence= 0.5, min_lift= 7)
	results = list(ar)
	d = {}
	i = 0
	for record in results:
		l = []
		l.append(record[1])
		l.append(list(record[2][0][0]))
		l.append(list(record[2][0][1]))
		l.append(record[2][0][2])
		l.append(record[2][0][3])
		d[i] = l
		i += 1

	global glob_state
	glob_state = d

	df1 = pd.DataFrame(d).transpose()

	l = list(df1[1])

	print(l)
	return {'data': ",".join(["&".join(item) for item in l])}

def giveAssocRight(query):
	splitq = query.split('&')
	print(splitq)
	df = pd.DataFrame(glob_state).transpose()
	df1 = pd.DataFrame()
	n = len(df.index)
	for i in range(n):
		s = df.iloc[i]
		# print(s[1])
		for item in splitq:
			if item in s[1]:
				df1 = df1.append(s)
				break

	print(df1)
	df1 = df1.sort_values(df1.columns[3], ascending=False)
	l = list(df1[2])

	return { 'data' : ",".join(["&".join(item) for item in l])}