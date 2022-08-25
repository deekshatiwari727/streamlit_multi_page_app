import streamlit as st
import pandas as pd
st.title("Home Page")
bar_graph = st.container()



with bar_graph:
		st.header("Ingredient Mention")
		from PIL import Image
		image = Image.open(r'C:\Users\DeekshaTiwari\Downloads\prod_reddit_Vegan_serums.jpeg')
		st.image(image, caption='Wordcloud')

		st.header("Engagement Score of Different Ingredients")
		csv = pd.read_csv(r'C:\Users\DeekshaTiwari\screen3ingredientdata.csv')
		df = pd.DataFrame(csv)
		#st.dataframe(df)
		csv1 = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Microsoft Teams Chat Files\ingredienttimeseries.csv')
		df1 = pd.DataFrame(csv1)
		#st.dataframe(df1)

		# csv2 = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Desktop\composition_cloud_mapper.csv')
		# df2 = pd.DataFrame(csv2)
		# st.dataframe(df2)
		import plotly.express as px

		# fig = px.bar(df, x='Category', y = 'Engagement Score')
		# fig.update_traces(width=.35)
		# st.plotly_chart(fig, use_container_width=True)

		keywords = list(df['Keyword\t'].drop_duplicates())
		categories = list(df['Category'].drop_duplicates())
		time= list(df['Time'].drop_duplicates())
		source = list(df['Channel'].drop_duplicates())

		source_choice = st.sidebar.multiselect(
		     "Source", source, default=source[0])

		keyword_choice = st.sidebar.multiselect(
		    'Keyword', keywords, default=keywords[0])

		category_choice = st.sidebar.multiselect(
		     "Category", categories, default=categories[0])

		time_choice = st.sidebar.multiselect(
		    "Timeframe", time, default=time[0])




		df = df[df['Keyword\t'].isin(keyword_choice)]
		df = df[df['Category'].isin(category_choice)]
		df = df[df['Time'].isin(time_choice)]
		df = df[df['Channel'].isin(source_choice)]

		fig = px.bar(df, x='Ingredient', y = 'Engagement Score')
		fig.update_traces(width=.35)
		st.plotly_chart(fig, use_container_width=True)

		#df1 = df1[df1['Keyword'].isin(keyword_choice)]
		#df1 = df1[df1['Category'].isin(category_choice)]
		df1= df1[df1['Time'].isin(time_choice)]
		df1 = df1[df1['Channel'].isin(source_choice)]

		fig1 = fig = px.line(df1, x="Week", y="Engagement Score", color='Ingredient')
		st.plotly_chart(fig1, use_container_width=True)

