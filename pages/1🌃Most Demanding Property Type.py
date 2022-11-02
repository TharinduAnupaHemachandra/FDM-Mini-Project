import streamlit as st
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
#from sklearn_extra.cluster import KMedoids
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from colours import *
#import random
import base64


st.set_page_config(layout='wide',)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('/app/wp5.jpg')









#st.set_page_config(layout="wide")

def get_colors():
    s = '''
        aliceblue, antiquewhite, aqua, aquamarine, azure,
        beige, bisque, black, blanchedalmond, blue,
        blueviolet, brown, burlywood, cadetblue,
        chartreuse, chocolate, coral, cornflowerblue,
        cornsilk, crimson, cyan, darkblue, darkcyan,
        darkgoldenrod, darkgray, darkgrey, darkgreen,
        darkkhaki, darkmagenta, darkolivegreen, darkorange,
        darkorchid, darkred, darksalmon, darkseagreen,
        darkslateblue, darkslategray, darkslategrey,
        darkturquoise, darkviolet, deeppink, deepskyblue,
        dimgray, dimgrey, dodgerblue, firebrick,
        floralwhite, forestgreen, fuchsia, gainsboro,
        ghostwhite, gold, goldenrod, gray, grey, green,
        greenyellow, honeydew, hotpink, indianred, indigo,
        ivory, khaki, lavender, lavenderblush, lawngreen,
        lemonchiffon, lightblue, lightcoral, lightcyan,
        lightgoldenrodyellow, lightgray, lightgrey,
        lightgreen, lightpink, lightsalmon, lightseagreen,
        lightskyblue, lightslategray, lightslategrey,
        lightsteelblue, lightyellow, lime, limegreen,
        linen, magenta, maroon, mediumaquamarine,
        mediumblue, mediumorchid, mediumpurple,
        mediumseagreen, mediumslateblue, mediumspringgreen,
        mediumturquoise, mediumvioletred, midnightblue,
        mintcream, mistyrose, moccasin, navajowhite, navy,
        oldlace, olive, olivedrab, orange, orangered,
        orchid, palegoldenrod, palegreen, paleturquoise,
        palevioletred, papayawhip, peachpuff, peru, pink,
        plum, powderblue, purple, red, rosybrown,
        royalblue, saddlebrown, salmon, sandybrown,
        seagreen, seashell, sienna, silver, skyblue,
        slateblue, slategray, slategrey, snow, springgreen,
        steelblue, tan, teal, thistle, tomato, turquoise,
        violet, wheat, white, whitesmoke, yellow,
        yellowgreen
        '''
    li=s.split(',')
    li=[l.replace('\n','') for l in li]
    li=[l.replace(' ','') for l in li]
    #random.shuffle(li)
    return li

@st.cache
def get_data(url):
    df = pd.read_csv(url)
    df["date"] = pd.to_datetime(df.date).dt.date
    df['date'] = pd.DatetimeIndex(df.date)

    return df

colors = get_colors()

#url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
data = pd.read_csv('/app/data/clustering/preprocessed_dataset_1.csv')
columns = ['longitude', 'latitude', 'accommodates',	'availability_30',	'bathrooms',	'bed_type',	'bedrooms',	'beds',	'calculated_host_listings_count',	'cancellation_policy',	'guests_included',	'has_availability',	'host_listings_count',	'instant_bookable',	'maximum_nights', 'price']



#locations = data.location.unique().tolist()

sidebar = st.sidebar

#mode = sidebar.radio("Mode", ["View property based on a price range", "Clustering"])
#st.markdown("<h1 style='text-align: center; color: #ff0000;'>COVID-19</h1>", unsafe_allow_html=True)
#st.title("".format(mode), unsafe_allow_html=True)

#st.title("Property based on a price range")
st.markdown("<h1 style='text-align: center; color: white;'>Property based on a price range</h1>", unsafe_allow_html=True)

features = sidebar.multiselect("Select Features", columns, default=columns[:2])

# select a clustering algorithm
#calg = sidebar.selectbox("Select a clustering algorithm", ["K-Means","K-Medoids", "Spectral Clustering", "Agglomerative Clustering"])

min_price = sidebar.text_input(label = 'Minimum price')
max_price = sidebar.text_input(label = 'Maximum price')
if min_price == '' or max_price == '':
    min_price = float(-1)
    max_price = float(-1)
else:
    min_price = float(min_price)
    max_price = float(max_price)
# select number of clusters
#ks = sidebar.slider("Select number of clusters", min_value=2, max_value=10, value=2)

# select a dataframe to apply cluster on

#data = data.sort_values("date").drop_duplicates(subset=["location"], keep= "last").dropna(subset=features)
#data = data[~data.location.isin(["Lower middle income", "North America", "World", "Asia", "Europe",
                        #"European Union", "Upper middle income",
                        #"High income", "South America"])]

# udf[features].dropna()

if len(features)==2:

    #f calg == "K-Means":
    #st.markdown("### K-Means Clustering")
    st.markdown("<h3 style='text-align: center; color: black;'>K-Means Clustering</h1>",
                unsafe_allow_html = True)
    #use_pca = sidebar.radio("Use PCA?",["Yes","No"])
    #st.markdown("### Not Using PCA")
    #inertias = []
    c = 10
    #tdf = data.copy()
    if min_price == -1 or max_price == -1:
        tdf = data.copy()
    else:
        tdf = data[data['price'].between(min_price, max_price)]
    X = tdf[features]
    # colors=['red','green','blue','magenta','black','yellow']
    sample_count = tdf.shape[0]
    if sample_count < c:
        c = 1

    model = KMeans(n_clusters=c)
    model.fit(X)
    y_kmeans = model.predict(X)
    tdf["cluster"] = y_kmeans
    #inertias.append((c,model.inertia_))

    trace0 = go.Scatter(x=tdf[features[0]], y=tdf[features[1]], mode='markers',
                                        marker=dict(
                                                color=tdf.cluster.apply(lambda x: colors[x]),
                                                colorscale='Viridis',
                                                showscale=True,
                                                size = data["price"] % 20,
                                                opacity = 0.9,
                                                reversescale = True,
                                                symbol = 'pentagon'
                                                ),
                                        )

    trace1 = go.Scatter(x=model.cluster_centers_[:, 0], y=model.cluster_centers_[:, 1],
                                        mode='markers',
                                        marker=dict(
                                            color=colors,
                                            size=20,
                                            symbol="circle",
                                            showscale=True,
                                            line = dict(
                                                width=1,
                                                color='rgba(102, 102, 102)'
                                                )

                                            ),
                                        name="Cluster Mean")

    data7 = go.Data([trace0, trace1])
    fig = go.Figure(data=data7)
    layout = go.Layout(
                                height=1000, width=1200, title=f"Cluster Size {c}",
                                xaxis=dict(
                                    title=features[0],
                                ),
                                yaxis=dict(
                                    title=features[1]
                                ) )

    fig.update_layout(layout)
    st.plotly_chart(fig, use_column_width=True)

    if 'latitude' in features and 'longitude' in features:
        st.map(tdf)

            #inertias=np.array(inertias).reshape(-1,2)
            #performance = go.Scatter(x=inertias[:,0], y=inertias[:,1])
            #layout = go.Layout(
             #       title="Cluster Number vs Inertia",
              #      xaxis=dict(
               #         title="Ks"
                #    ),
                 #   yaxis=dict(
                  #      title="Inertia"
                   # ) )
            #fig=go.Figure(data=go.Data([performance]))
            #fig.update_layout(layout)
            #st.plotly_chart(fig)
else:
    st.markdown("### Please Select 2 Features for Visualization.")
