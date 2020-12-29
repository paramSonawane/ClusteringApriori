
import pandas as pd

from os.path import join as ospJoin
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

from plotly.offline import plot

import plotly.graph_objs as go


def plotScatter(clusterInfo, labels):
	cluster0 = go.Scatter3d(
		z=(clusterInfo[(clusterInfo.labels == 0)][['Age']]).reset_index()['Age'].tolist(),
		y=(clusterInfo[(clusterInfo.labels == 0)][['Annual_income']]).reset_index()['Annual_income'].tolist(),
		x=(clusterInfo[(clusterInfo.labels == 0)][['Spending_score']]).reset_index()['Spending_score'].tolist(),
		name='Cluster 0',
	)
	cluster1 = go.Scatter3d(
		z=(clusterInfo[(clusterInfo.labels == 1)][['Age']]).reset_index()['Age'].tolist(),
		y=(clusterInfo[(clusterInfo.labels == 1)][['Annual_income']]).reset_index()['Annual_income'].tolist(),
		x=(clusterInfo[(clusterInfo.labels == 1)][['Spending_score']]).reset_index()['Spending_score'].tolist(),
		name='Cluster 1'
	)
	cluster2 = go.Scatter3d(
		z=(clusterInfo[(clusterInfo.labels == 2)][['Age']]).reset_index()['Age'].tolist(),
		y=(clusterInfo[(clusterInfo.labels == 2)][['Annual_income']]).reset_index()['Annual_income'].tolist(),
		x=(clusterInfo[(clusterInfo.labels == 2)][['Spending_score']]).reset_index()['Spending_score'].tolist(),
		name='Cluster 2'
	)
	cluster3 = go.Scatter3d(
		z=(clusterInfo[(clusterInfo.labels == 3)][['Age']]).reset_index()['Age'].tolist(),
		y=(clusterInfo[(clusterInfo.labels == 3)][['Annual_income']]).reset_index()['Annual_income'].tolist(),
		x=(clusterInfo[(clusterInfo.labels == 3)][['Spending_score']]).reset_index()['Spending_score'].tolist(),
		name='Cluster 3'
	)
	cluster4 = go.Scatter3d(
		z=(clusterInfo[(clusterInfo.labels == 4)][['Age']]).reset_index()['Age'].tolist(),
		y=(clusterInfo[(clusterInfo.labels == 4)][['Annual_income']]).reset_index()['Annual_income'].tolist(),
		x=(clusterInfo[(clusterInfo.labels == 4)][['Spending_score']]).reset_index()['Spending_score'].tolist(),
		name='Cluster 4'
	)
	clusterCenters = go.Scatter3d(
		z=(clusterInfo[(clusterInfo.labels == 6)][['Age']]).reset_index()['Age'].tolist(),
		y=(clusterInfo[(clusterInfo.labels == 6)][['Annual_income']]).reset_index()['Annual_income'].tolist(),
		x=(clusterInfo[(clusterInfo.labels == 6)][['Spending_score']]).reset_index()['Spending_score'].tolist(),
		name='Centers',
		mode='markers',

		marker=dict(
				color = "#eff836",
				size= 10,
				line=dict(
					color= "#eff836",
				),
				opacity = 0.9
			),
	)

	layout = go.Layout(
		autosize=False,
		width=1000,
		height=800,
		scene = dict(
				xaxis = dict(title  = 'Spending_score'),
				yaxis = dict(title  = 'Annual_income'),
				zaxis = dict(title  = 'Age')
			),
		showlegend=True,
	)

	fig = go.Figure(data=[cluster0,cluster1, cluster2 ,cluster3, cluster4, clusterCenters], layout=layout)
	plot_div = plot(fig, output_type='div', include_plotlyjs=False)
	return plot_div



def plotMaleVsFemale():
	df = pd.read_csv(ospJoin(BASE_DIR,'home/logic/CSVs/mall.csv'))

	extrDf = df['Gender'].value_counts()

	x = list(extrDf.index)
	y = list(extrDf.values)

	# Use the hovertext kw argument for hover text
	fig = go.Figure(
		data=[
			go.Bar(
				x=y,
				y=x,
				hovertext=[ ""+str(int((y[i]/extrDf.values.sum())*100))+"%" for i in range(len(y)) ],
				orientation='h',
			),
		]
	)
	# Customize aspect
	fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
					marker_line_width=1.5, opacity=0.6)
	fig.update_layout(title_text='Male vs Female Distribution')

	return plot(fig, output_type='div', include_plotlyjs=False)

def giveOnlyProds(df):

	print("started generating ops")
	onlyProducts = {}

	for i in range(1, len(df.columns)):
		for item in list(df[i]) :
			if not pd.isna(item) :
				if item in onlyProducts :
					onlyProducts[item]+=1
				else :
					onlyProducts[item] = 1

	print("Generated ops")
	return onlyProducts

def plotMaxFreq():
	df = pd.read_csv(ospJoin(BASE_DIR,'home/logic/CSVs/new_purchase.csv'), header=None)

	onlyProducts = giveOnlyProds(df)

	print("Building df from dictionary")
	oPDf = pd.DataFrame(onlyProducts, index=[0]).transpose()

	print("Sorting df")
	oPDf = oPDf.sort_values(oPDf.columns[0], ascending=False).reset_index()

	print("Generatring graph")

	fig = go.Figure(
		go.Bar(
            y=oPDf.head(10)[0],
            x=oPDf.head(10)['index'],
            # orientation='h'
		)
	)
	fig.update_layout(title_text='Top 10 Selling Items')

	return plot(fig, output_type='div', include_plotlyjs=False)

def genderVsSpendingPower():
	df = pd.read_csv(ospJoin(BASE_DIR,'home/logic/CSVs/mall.csv'))

	extrDf = df.groupby(['Gender'])['Spending Score (1-100)'].mean()

	x = list(extrDf.index)
	y = list(extrDf.values)

	# Use the hovertext kw argument for hover text
	labels = x
	values = y

	fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
	fig.update_layout(title_text='Gender wise Spendings')

	return plot(fig, output_type='div', include_plotlyjs=False)