import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image

selectbox2 = st.sidebar.selectbox("Influencer Based Trends",["Trends Insight","Trends Description", "Trend of Each Influencer"])


header = st.container()  #Creates a container. So now, I have a container called 'header'.
number_of_posts = st.container()  
topic = st.container()
topic_deep_dive = st.container()
brand_mentions= st.container()  #they are created but we don't have anything in them.

topic_name = st.container()
description = st.container()
example_posts  =st.container()
influencer_name = st.container()

if selectbox2 == "Trends Insight":
	csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Documents\IBT-TDD.csv')
	df = pd.DataFrame(csv)
	#st.dataframe(df)
	
	datatype= list(df['Type of Data'].drop_duplicates())
	time= list(df['Timeframe'].drop_duplicates())
	source = list(df['Source'].drop_duplicates())
	source_choice = st.sidebar.multiselect(
         "Source", source, default=source[0])

	time_choice = st.sidebar.multiselect(
        "Timeframe", time, default=time[0])

	datatype_choice = st.sidebar.multiselect('Type of Data', datatype, default=datatype[0])
    
	df = df[df['Type of Data'].isin(datatype_choice)]
	df = df[df['Timeframe'].isin(time_choice)]
	df = df[df['Source'].isin(source_choice)]
	with header:           #to write something inside a container - with container_name
		st.title('Trend Insights')
		

	with number_of_posts:
		#st.header('Number of post analyzed')
		st.metric(label="Number of post analyzed", value="700")

	with topic:
		st.header('Topic')
		from PIL import Image
		image = Image.open(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Microsoft Teams Chat Files\topic.png')
		st.image(image)

	with topic_deep_dive:
		csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Desktop\streamlit\KBT-TDD.csv')
		df = pd.DataFrame(csv)
		st.header('Topic deep dive')		
		fig = go.Figure(data=[go.Table(header=dict(values=['Topic', 'Size', 'Top 2 Influencers'], fill_color = 'darkgrey'),
	                 cells=dict(values=[df.Topic, df.Size, df.Top_2_Influencers],fill_color = 'salmon'))
	                     ])
		fig.update_layout(margin=dict(l=2,r=2,b=2,t=2))
		st.write(fig)

if selectbox2 == "Trends Description":
	csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Documents\IBT-TDD.csv')
	df = pd.DataFrame(csv)
	#st.dataframe(df)
	
	datatype= list(df['Type of Data'].drop_duplicates())
	time= list(df['Timeframe'].drop_duplicates())
	source = list(df['Source'].drop_duplicates())
	#topic = list(df['Topic'].drop_duplicates())
	source_choice = st.sidebar.multiselect(
         "Source", source, default=source[0])

	time_choice = st.sidebar.multiselect(
        "Timeframe", time, default=time[0])

	datatype_choice = st.sidebar.multiselect('Type of Data', datatype, default=datatype[0])
	#topic_choice = st.sidebar.multiselect('Topic', topic, default=topic[0])
    
	df = df[df['Type of Data'].isin(datatype_choice)]
	df = df[df['Timeframe'].isin(time_choice)]
	df = df[df['Source'].isin(source_choice)]
	#df = df[df['Topic'].isin(topic_choice)]

	with header:           #to write something inside a container - with container_name
		st.title('Trend Description')

	with topic_name:
		Topic0, Topic1, Topic2= st.tabs(["Topic 0", "Topic 1", "Topic 2"])

		with Topic0:
		    st.header('Description')
		    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum semper feugiat metus eget sollicitudin. Vestibulum ac risus fringilla, venenatis neque ut, dapibus turpis. Aenean in metus vel ex porta facilisis ac vitae metus. Cras eu lorem nec sem vulputate laoreet sed at lacus. In hac habitasse platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer pretium augue id cursus consectetur. Fusce faucibus lorem quis sem tempor, non congue purus iaculis.')

		with Topic1:
		    st.header('Description')
		    st.write('Ah, the eternal struggle between wanting to save the planet & be ethical in every fiber of your being, and wanting to use all kinds of fun skincare (or makeup, or hair care) products. The back and forth of “is it worth it?” and “that looks so cool, but it’s also wrong.” To help you get the best of both words, we’ve created a handy dandy list with 30 different vegan skincare brands that are 100% vegan.  Every product from each of these brands is vegan. You don’t have to worry about checking the ingredients lists on each product, just because the brand claims to be “mostly” vegan. These are all the way!')


		with Topic2:
		    st.header('Description')
		    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum semper feugiat metus eget sollicitudin. Vestibulum ac risus fringilla, venenatis neque ut, dapibus turpis. Aenean in metus vel ex porta facilisis ac vitae metus. Cras eu lorem nec sem vulputate laoreet sed at lacus. In hac habitasse platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer pretium augue id cursus consectetur. Fusce faucibus lorem quis sem tempor, non congue purus iaculis.')

		#st.header('Topic 0')


	# with description:
	# 	st.subheader('Description')
	# 	st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum semper feugiat metus eget sollicitudin. Vestibulum ac risus fringilla, venenatis neque ut, dapibus turpis. Aenean in metus vel ex porta facilisis ac vitae metus. Cras eu lorem nec sem vulputate laoreet sed at lacus. In hac habitasse platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer pretium augue id cursus consectetur. Fusce faucibus lorem quis sem tempor, non congue purus iaculis.')

	with example_posts:
		st.header('Example Posts')
		csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Documents\trend_description.csv')
		df = pd.DataFrame(csv)
		fig = go.Figure(data=[go.Table(header=dict(values=['Post', 'Influencer'], fill_color = 'darkgrey'),
	                 cells=dict(values=[df.Post, df.Influencer],fill_color = 'lightblue'))
	                     ])
		fig.update_layout(margin=dict(l=2,r=2,b=5,t=5))
		st.write(fig)


if selectbox2 == "Trend of Each Influencer":
	csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Documents\trend_of_each_influencer.csv')
	df = pd.DataFrame(csv)
	#st.dataframe(df)
	
	datatype= list(df['Type of Data'].drop_duplicates())
	time= list(df['Timeframe'].drop_duplicates())
	source = list(df['Source'].drop_duplicates())
	influencer = list(df['Influencer'].drop_duplicates())
	source_choice = st.sidebar.multiselect(
         "Source", source, default=source[0])

	time_choice = st.sidebar.multiselect(
        "Timeframe", time, default=time[0])

	datatype_choice = st.sidebar.multiselect('Type of Data', datatype, default=datatype[0])

	influencer_choice = st.sidebar.multiselect('Influencer', influencer, default=influencer[0])
    
	df = df[df['Type of Data'].isin(datatype_choice)]
	df = df[df['Timeframe'].isin(time_choice)]
	df = df[df['Source'].isin(source_choice)]
	df = df[df['Influencer'].isin(influencer_choice)]
	with header:           #to write something inside a container - with container_name
		st.title('Trend of each Influencer')
		

	with number_of_posts:
		#st.header('Number of post analyzed')
		col1, col2, col3 = st.columns(3)
		col1.metric("Number of Post Analyzed", "700")
		col2.metric("Name of Influencer", "Huda Kattan")

	with topic:
		st.header('Topic')

		image = Image.open(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Microsoft Teams Chat Files\topic.png')
		st.image(image)

	#brand_mentions, topic_deep_dive = st.columns(2)
	with brand_mentions:
		st.header('Brand mentions')
		fig = go.Figure(data=[go.Table(header=dict(values=['Brand', 'Number of Mention'], fill_color = 'darkgrey'),
	                 cells=dict(values=[df.Brand, df.Number_of_Mention],fill_color = 'salmon'))
	                     ])
		fig.update_layout(margin=dict(l=2,r=2,b=5,t=5))
		st.write(fig)

	with topic_deep_dive:
		csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Desktop\streamlit\KBT-TDD.csv')
		df= pd.DataFrame(csv)
		st.header('Topic deep dive')		
		fig = go.Figure(data=[go.Table(header=dict(values=['Topic', 'Size'], fill_color = 'darkgrey'),
	                 cells=dict(values=[df.Topic, df.Size],fill_color = 'salmon'))
	                     ])
		fig.update_layout(margin=dict(l=2,r=2,b=2,t=2), width=700, height=200)
		st.write(fig)

	