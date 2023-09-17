import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


DATA_URL = ('/Users/harshitshangari/Downloads/train.csv')

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL, index_col=0)
    return data

data = load_data()


# Sidebar for filtering options
st.sidebar.header("Filter Data")
select_numerical_features = st.sidebar.checkbox("Select Numerical Features", value=True)

# Option to select all numerical features
all_numerical_features = ["Elevation", "Aspect", "Slope", "Horizontal_Distance_To_Hydrology", "Vertical_Distance_To_Hydrology",
                             "Horizontal_Distance_To_Roadways", "Hillshade_9am", "Hillshade_Noon", "Hillshade_3pm", "Horizontal_Distance_To_Fire_Points"]


if select_numerical_features:
    filtered_features = all_numerical_features
else:
    filtered_features = st.sidebar.multiselect("Select Features", data.columns)



st.title("Forest Cover Type Prediction Exploratory Data Analysis")
st.write("The goal of this project is to predict the forest cover type (a categorical variable) from various geographic information. "
         "Through this streamlit app, we will be performing an exploratory data analysis of this dataset")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.write("The train set comprised of 15120 rows and 13 variable classes. There were 10 numerical ex"
"planatory features and 2 categorical ones. Numerical features included: Elevation (in meters), Aspect (in degrees "
"azimuth), Slope (in degrees), Horizontal_Distance_To_Hydrology (i.e. to nearest surface water feature), Ver"
"tical_Distance_To_Hydrology (i.e. to nearest surface water features), Horizontal_Distance_To_Roadways, "
"Hillshade_9am (0 to 255 index, summer solstice), Hillshade_Noon (0 to 255 index, summer soltice), Hill"
"shade_3pm (0 to 255 index, summer solstice) and Horizontal_Distance_To_Fire_Points (i.e. to nearest wild"
"fire ignition points). There were three categorical classes: Wilderness_Area (wilderness area designation), "
"Soil_Type (soil type designation) and the target variable, Cover_Type (forest cover type designation). Wilderness_Area was divided into 4 different columns, Soil"
"Type in 40 columns and Cover Type into 7 columns.")

# Statistical Description of Features
st.header("Statistical Description of Features")
if filtered_features:
    st.write(data[filtered_features].describe())
else:
    st.write("No features selected. Please choose one or more features for summary statistics.")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Correlation Heatmap
st.header("Correlation Heatmap")
if len(filtered_features) >= 2:
    correlation_matrix = data[filtered_features].corr()
    sns.heatmap(correlation_matrix, cmap="coolwarm", linewidths=0.5)
    st.pyplot()
else:
    st.write("No features selected. Please choose two or more features for the correlation heatmap.")

st.write("The most significant correlations are hypothesized between Hillshade at 9 am and Hillshade at 3 pm, "
"as well as Horizontal Distance to Hydrology and Vertical Distance to Hydrology. Other very strong correlations "
"include Hillshade (9 am and 3 pm) and Aspect, and Hillshade at noon with Slope.")





# Distribution Plots
st.header("Distribution Plots")
if filtered_features:
    for feature in filtered_features:
        st.subheader(f"Distribution of {feature}")
        plt.figure(figsize=(8, 6))
        sns.histplot(data[feature], kde=True)
        plt.xlabel(feature)
        plt.ylabel("Count")
        st.pyplot()

st.write("From the distribution plots, we also observe strong positive skewness of the distribution of the Horizontal,"
         " and Vertical Distance to Hydrology, Horizontal Distance to Fire Points and Roadways. Strong negative skewness"
         " was observed for Hillshade at 9 am and Hillshade at noon.")

# Scatter Plot
st.header("Scatter Plot")
x_feature = st.selectbox("X-axis feature", filtered_features)
y_feature = st.selectbox("Y-axis feature", filtered_features)
if x_feature and y_feature:
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=x_feature, y=y_feature, data=data, hue='Cover_Type', palette='viridis')
    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    st.pyplot()


# Pairplot
if select_numerical_features:
    @st.cache_data
    def create_pairplot(data):
        pairplot = sns.pairplot(data[filtered_features + ['Cover_Type']], hue='Cover_Type', palette='viridis')
        return pairplot

    st.header("Pairplot")
    pairplot = create_pairplot(data)
    st.pyplot(pairplot)

else:
    st.header("Pairplot")
    pairplot = sns.pairplot(data[filtered_features + ['Cover_Type']], hue='Cover_Type', palette='viridis')
    st.pyplot()

st.write("Relations between variables: We also plotted the relations between some features with the colours on the "
"graph representing the different cover types. For example, from the plot of  Elevation vs "
"Vertical Distance to Hydrology and Elevation vs Horizontal Distance to Hydrology, we can see that it reveals "
"a pattern that can be better captured by creating a new feature by subtracting one feature from another.")

# Violin Plot
st.header("Violin Plot")

if filtered_features:
    for feature in filtered_features:
        plt.figure(figsize=(10, 6))
        sns.violinplot(x='Cover_Type', y=feature, data=data, palette='viridis')
        plt.xlabel("Cover_Type")
        plt.ylabel(feature)
        st.pyplot()

st.write("We plot violin plot for all numerical variables, which is a hybrid of a box plot and a kernel density "
"plot, and shows peaks in the data. It was used to visualize the explanatory power of our features with regard "
"to our Cover Type target variable. Our most relevant plot was Elevation as a function of Cover Type, in which we "
"clearly see that each cover type has an associated distribution of elevation.")