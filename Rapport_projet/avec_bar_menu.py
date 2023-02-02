import streamlit as st 
import pandas as pd

# STREAMLIT
st.sidebar.title("Summary")

pages = ["The project","Analysis & cleaning the dataset","Some plots","Features Engineering","Modelisation","Conclusion"]
page = st.sidebar.radio("go through", pages)

Team_members =["Vixra KEO","Margueritte Babeth NKEN","Antoine BEDOUCH","Attoumassa SAMAKE"]

st.sidebar.markdown("---")
st.sidebar.title("Team members")
for member in Team_members:
    st.sidebar.markdown(member)

if page==pages[0]: 
     st.title("Python labs project : Books rating")
     st.write("Description of the project")

elif page==pages[1]:
    st.header("Analysis & cleaning the dataset")
    st.write("Let's load the dataset...")
    raw_df = pd.read_csv(
    filepath_or_buffer="data/books.csv",
    on_bad_lines="warn",
    sep=",",
    skipinitialspace=True)
    st.write(raw_df.head())
    st.write("We notice how some rows had too many fields. The on_bad_lines=WARN argument skips them for us. When we go look at those rows in the csv file, we notice that some books had comas , in their title or authors names. For example for line 3350 is as follows: 12224,Streetcar Suburbs: The Process of Growth in Boston  1870-1900,Sam Bass Warner, Jr./Sam B. Warner,3.58,0674842111,9780674842113,en-US,236,61,6,4/20/2004,Harvard University Press The author name is contains a coma Sam Bass Warner, Jr./Sam B. Warner.")
    st.markdown("      ")
    st.write(raw_df.isna().sum())
    st.write("Please note that there is no NA values. The dataset is clean")
    st.markdown("      ")
    st.write(raw_df.describe())

elif page==pages[2]:
    st.header("Some plots")
    st.write("The main project")


elif page==pages[3]:
    st.header("Features Engineering")
    st.write("The main project")


elif page==pages[4]:
    st.header("Modelisation")
    st.write("The main project")


elif page==pages[4]:
    st.header("Conclusion")
    st.write("The main project")
