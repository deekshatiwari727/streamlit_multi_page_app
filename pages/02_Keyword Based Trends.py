import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
#from bertopic import BERTopic

selectbox1 = st.sidebar.selectbox("Keywords Based Trends",["Trends Insight","Trends Description","Brand Mention","Ingredient Mention"])

header = st.container()  #Creates a container. So now, I have a container called 'header'.
number_of_posts = st.container() 
topic = st.container() 
topic_deep_dive = st.container()
bar_graph = st.container()

brand_mentions= st.container()  #they are created but we don't have anything in them.

topic_name = st.container()
description = st.container()
example_posts  =st.container()


if selectbox1 == "Trends Insight":
    csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Documents\IBT-TDD.csv')
    df = pd.DataFrame(csv)
    #st.dataframe(df)
    
    keywords = list(df['Keyword'].drop_duplicates())
    time= list(df['Timeframe'].drop_duplicates())
    source = list(df['Source'].drop_duplicates())
    source_choice = st.sidebar.multiselect(
         "Source", source, default=source[0])
    keyword_choice = st.sidebar.multiselect('Keyword', keywords, default=keywords[0])


    time_choice = st.sidebar.multiselect(
        "Timeframe", time, default=time[0])

    

    
    df = df[df['Keyword'].isin(keyword_choice)]
    df = df[df['Timeframe'].isin(time_choice)]
    df = df[df['Source'].isin(source_choice)]
    with header:           #to write something inside a container - with container_name
        st.title('Trend Insights')
        

    with number_of_posts:
        # st.header('Number of post analyzed')
        st.metric(label="Number of post analyzed", value="700")

    with topic:
        st.header('Topic')
        from PIL import Image
        image = Image.open(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Microsoft Teams Chat Files\topic.png')
        st.image(image)
        # topic_model = BERTopic.load("my_model")
        # fig = topic_model.visualize_barchart(top_n_topics=10, n_words=10, height=400)
        # st.plotly_chart(fig)

    with topic_deep_dive:
        csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Desktop\streamlit\KBT-TDD.csv')
        df = pd.DataFrame(csv)
        #st.dataframe(df7)
        st.header('Topic deep dive')        
        fig = go.Figure(data=[go.Table(header=dict(values=['Topic', 'Size', 'Top 2 Influencers'], fill_color = 'darkgrey'),
                     cells=dict(values=[df.Topic, df.Size, df.Top_2_Influencers],fill_color = 'salmon'))
                         ])
        fig.update_layout(margin=dict(l=2,r=2,b=2,t=2))
        st.write(fig)
    




if selectbox1 == "Trends Description":
    csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Documents\IBT-TDD.csv')
    df = pd.DataFrame(csv)
    #st.dataframe(df)
    
    keyword= list(df['Keyword'].drop_duplicates())
    time= list(df['Timeframe'].drop_duplicates())
    source = list(df['Source'].drop_duplicates())
    #topic = list(df['Topic'].drop_duplicates())
    source_choice = st.sidebar.multiselect(
         "Source", source, default=source[0])

    keyword_choice = st.sidebar.multiselect('Keyword', keyword, default=keyword[0])

    time_choice = st.sidebar.multiselect(
        "Timeframe", time, default=time[0])

    
    #topic_choice = st.sidebar.multiselect('Topic', topic, default=topic[0])
    
    df = df[df['Keyword'].isin(keyword_choice)]
    df = df[df['Timeframe'].isin(time_choice)]
    df = df[df['Source'].isin(source_choice)]
    #df = df[df['Topic'].isin(topic_choice)]

    with header:           #to write something inside a container - with container_name
        st.title('Trends Description')

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
    #     st.subheader('Description')
    #     st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum semper feugiat metus eget sollicitudin. Vestibulum ac risus fringilla, venenatis neque ut, dapibus turpis. Aenean in metus vel ex porta facilisis ac vitae metus. Cras eu lorem nec sem vulputate laoreet sed at lacus. In hac habitasse platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer pretium augue id cursus consectetur. Fusce faucibus lorem quis sem tempor, non congue purus iaculis.')

    with example_posts:
        st.header('Example Posts')
        csv = pd.read_csv(r'C:\Users\DeekshaTiwari\OneDrive - TheMathCompany Private Limited\Documents\trend_description.csv')
        df = pd.DataFrame(csv)
        fig = go.Figure(data=[go.Table(header=dict(values=['Post', 'Influencer'], fill_color = 'darkgrey'),
                     cells=dict(values=[df.Post, df.Influencer],fill_color = 'lightblue'))
                         ])
        fig.update_layout(margin=dict(l=2,r=2,b=5,t=5))
        st.write(fig)

if selectbox1 == "Brand Mention":
    with bar_graph:
        st.header("Engagement Score of Different Brands")
        csv = pd.read_csv(r'C:\Users\DeekshaTiwari\Downloads\screen3_product_brand_bar.csv')
        df = pd.DataFrame(csv)
        #st.dataframe(df)

        csv1 = pd.read_csv(r'C:\Users\DeekshaTiwari\Downloads\screen3_product_brand_timeseries.csv')
        df1 = pd.DataFrame(csv1)
        #st.dataframe(df1)

        import plotly.express as px

        # fig = px.bar(df, x='Category', y = 'Engagement Score')
        # fig.update_traces(width=.35)
        # st.plotly_chart(fig, use_container_width=True)

        keywords = list(df['Keyword'].drop_duplicates())
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

        

        
        df = df[df['Keyword'].isin(keyword_choice)]
        df = df[df['Category'].isin(category_choice)]
        df = df[df['Time'].isin(time_choice)]
        df = df[df['Channel'].isin(source_choice)]
        
        fig = px.bar(df, x='Brand', y = 'Engagement Score')
        fig.update_traces(width=.35)
        st.plotly_chart(fig, use_container_width=True)

        df1 = df1[df1['Keyword'].isin(keyword_choice)]
        df1 = df1[df1['Category'].isin(category_choice)]
        df1= df1[df1['Time'].isin(time_choice)]
        df1 = df1[df1['Channel'].isin(source_choice)]

        fig1 = fig = px.line(df1, x="Week", y="Engagement Score", color='Brand')
        st.plotly_chart(fig1, use_container_width=True)
    with brand_mentions:
  
        st.header('Brand mentions')
        fig = go.Figure(data=[go.Table(header=dict(values=['Brand', 'Number of Mention'], fill_color = 'darkgray'),
                     cells=dict(values=[df.Brand, [450,567,453,345,532]],fill_color = 'salmon'))
                         ])
        fig.update_layout(margin=dict(l=2,r=2,b=2,t=2))
        st.write(fig)


if selectbox1 == "Ingredient Mention":
    with bar_graph:
        st.title("Ingredient Mention")
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



    #df2 = df2[df2['Keyword'].isin(keyword_choice)]
    
    #
