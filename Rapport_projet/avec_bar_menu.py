import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STREAMLIT

#The sidebar 
st.sidebar.title("Summary")

pages = ["The project","Analysis & cleaning the dataset","Some plots","Features Engineering","Modelisation","Conclusion"]
page = st.sidebar.radio("go through", pages)

Team_members =["Vixra KEO","Margueritte Babeth NKEN","Antoine BEDOUCH","Attoumassa SAMAKE"]

#Team members 
st.sidebar.markdown("---")
st.sidebar.title("Team members")
for member in Team_members:
    st.sidebar.markdown(member)

#Page 0 : The project descrition 
if page==pages[0]: 
     st.title("Python labs project : Books rating")
     st.write("Description of the project")
#Page 1: Analysis & cleanning 
elif page==pages[1]:
    st.header("Analysis & cleaing the dataset")
   # st.write("Our dataset looks like this")
    raw_df = pd.read_csv(
    filepath_or_buffer="data/books.csv",
    on_bad_lines="warn",
    sep=",",
    skipinitialspace=True)
    #st.write(raw_df.head())
    if st.checkbox("**Afficher un aperçu du jeu de données**"):
        st.dataframe(raw_df)

    st.write(" The dataset has  11123 rows( donc autant de livres) and 12 columns including the target variable (average_rating).")
    st.markdown("      ")

    st.write("**Variables quantitatives :**")
    st.write("- *Average_rating* : The average rating of the book received in total")
    st.write("- *num_pages*: The number of pages the book contains") 
    st.write("- *ratings_count*: The total number of ratings the book received")
    st.write("- *text_reviews_count*: The total number of written text reviews the book received")

    st.write("**Variables ... :**")   
    st.write("- *title*: The name under which the book was published.")
    st.write("- *authors*: The names of the authors of the book. Multiple authors are delimited by “/”.")   

#NETTOYAGE DU JEU DE DONNÉES 
    st.subheader("Nettoyage du jeu de données")
    #st.write("**Gestion des NaNs :**")  
    st.write("Please note that there is no NA values. But we can wonder :")
    st.write("- Is the data balanced?")
    st.write(" - Is there any outliers in our dataset ?")
    st.write("- Which features are useful and which aren't?")

#SUPPRESSION DES VALEURS ABERRANTES 
    st.write("**We will plot the distributions of the main numerical features:**") 
    st.write("- *number of pages*") 
    st.write("- *number of ratings*")
    st.write("- *number of reviews*") 
    st.write("- *average rating*") 

    if st.checkbox("**Show plots**"):
   
        st.markdown("      ")
        fig_num_pages = plt.figure(figsize=[12,5])
        df = raw_df
        plt.hist(df["num_pages"], bins=30)
        plt.yscale("log")
        plt.show()
        st.pyplot(fig_num_pages)
        st.write("We observe that most books have less than 1000 pages. Under 1000 pages the distribution is overall balanced") 

        st.markdown("      ")
        fig_num_rating = plt.figure(figsize=[12,5])
        plt.hist(df["ratings_count"], bins=50)
        plt.yscale("log")
        plt.show()
        st.pyplot(fig_num_rating)
        
        st.markdown("      ")
        fig_text = plt.figure(figsize=[12,5])
        plt.hist(df["text_reviews_count"], bins=50)
        plt.yscale("log")
        plt.show()
        st.pyplot(fig_text)
        st.write("Generally speaking, the distribution of number of ratings and reviews are skewed towards 0. This means that generally speaking, most books have fewer numbers of reviews and ratings while a few books have a lot. Such distribution resembles a [power law distribution](https://en.wikipedia.org/wiki/Power_law).")

        st.markdown("      ")
        fig_ave = plt.figure(figsize=[12,5])
        plt.hist(df["average_rating"], bins=50)
        plt.show()
        st.pyplot(fig_ave)
        st.write("We notice immediately that the target feature `average_rating` is skewed towards an average of 4. It resembles a normal distribution centered around 4. This data is inherently imbalanced (almost all ratings between 3 and 5, almost no ratings between 0 and 3).We will have to take this into consideration when creating the training and testing sets: these sets should both include books with a wide range of average ratings.")


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
