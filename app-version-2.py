import pandas as pd
import pickle
import streamlit as st



st.image("4_images/title.jpeg", width=200)
st.title("Lead Predictions Web App")

cat_features = ['Lead Origin', 'Lead Source', 'Do Not Email', 'TotalVisits',
                   'Last Activity', 'Country', 'Specialization',
                   'What is your current occupation', 'Tags', 'Lead Quality', 'City',
                   'Asymmetrique Activity Index', 'Asymmetrique Profile Index',
                   'Asymmetrique Activity Score', 'Asymmetrique Profile Score',
                   'A free copy of Mastering The Interview', 'Last Notable Activity']
num_features = ['Total Time Spent on Website', 'Page Views Per Visit']


X_train = pd.read_csv("1_dataset/xtrain.csv")
col1, col2, col3 = st.columns(3)
test = pd.DataFrame()
sample = pd.DataFrame(columns=X_train.drop('Unnamed: 0', axis=1).columns)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')


# pickle_logistic
with open('logistic_model.pkl', 'rb') as file:
    pickle_logistic = pickle.load(file)


def main():
    user_input = st.selectbox("select one:",["Bulk Predictions","One by One"],)

    if user_input=="One by One":
        st.write("Enter the below features")
        col1, col2, col3 = st.columns(3)
        with col1:
            feature_0 = st.selectbox(f"{cat_features[0]}", X_train[f"{cat_features[0]}"].unique())
        with col2:
            feature_1 = st.selectbox(f"{cat_features[1]}", X_train[f"{cat_features[1]}"].unique())
        with col3:
            feature_2 = st.selectbox(f"{cat_features[2]}", X_train[f"{cat_features[2]}"].unique())
        with col1:
            feature_3 = st.selectbox(f"{cat_features[3]}", X_train[f"{cat_features[3]}"].unique())
        with col2:
            feature_4 = st.selectbox(f"{cat_features[4]}", X_train[f"{cat_features[4]}"].unique())
        with col3:
            feature_5 = st.selectbox(f"{cat_features[5]}", X_train[f"{cat_features[5]}"].unique())
        with col1:
            feature_6 = st.selectbox(f"{cat_features[6]}", X_train[f"{cat_features[6]}"].unique())
        with col2:
            feature_7 = st.selectbox(f"{cat_features[7]}", X_train[f"{cat_features[7]}"].unique())
        with col3:
            feature_8 = st.selectbox(f"{cat_features[8]}", X_train[f"{cat_features[8]}"].unique())
        with col1:
            feature_9 = st.selectbox(f"{cat_features[9]}", X_train[f"{cat_features[9]}"].unique())
        with col2:
            feature_10 = st.selectbox(f"{cat_features[10]}", X_train[f"{cat_features[10]}"].unique())
        with col3:
            feature_11 = st.selectbox(f"{cat_features[11]}", X_train[f"{cat_features[11]}"].unique())
        with col1:
            feature_12 = st.selectbox(f"{cat_features[12]}", X_train[f"{cat_features[12]}"].unique())
        with col2:
            feature_13 = st.selectbox(f"{cat_features[13]}", X_train[f"{cat_features[13]}"].unique())
        with col3:
            feature_14 = st.selectbox(f"{cat_features[14]}", X_train[f"{cat_features[14]}"].unique())
        with col1:
            feature_15 = st.selectbox(f"{cat_features[15]}", X_train[f"{cat_features[15]}"].unique())
        with col2:
            feature_16 = st.selectbox(f"{cat_features[16]}", X_train[f"{cat_features[16]}"].unique())
        with col1:
            feature_17 = float(st.text_input(f"{num_features[0]} - between 0 and 1",0))
        with col2:
            feature_18 = float(st.text_input(f"{num_features[1]} - between 0 and 1",0))

        features = [feature_0,feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,
                    feature_7,feature_8,feature_9,feature_10,feature_11,feature_12,feature_13,
                    feature_14,feature_15,feature_16,feature_17,feature_18
                    ]

        feature_list =[]
        feature_list.extend(cat_features)
        feature_list.extend(num_features)

        if st.button("Predict"):
            test = pd.DataFrame([features], columns=X_train.drop('Unnamed: 0', axis=1).columns)
            st.write("Predicting for:")
            test = test[X_train.drop('Unnamed: 0', axis=1).columns]
            # st.write(test[X_train.drop('Unnamed: 0', axis=1).columns])
            # predicted = pickle_logistic.predict(test[X_train.drop('Unnamed: 0', axis=1).columns])
            predicted = pickle_logistic.predict(test)
            if predicted:
                st.write("This lead will be converted successfully.")
            else:
                st.write("This is a failure.")
            test['Converted'] = predicted
            st.write(test)

    if user_input == "Bulk Predictions":
        st.subheader("Welcome to Bulk predictions")

        st.write("Input file format")
        st.write(sample)
        csv = convert_df(sample)
        st.download_button(
            label="Download Sample",
            data=csv,
            file_name='sample.csv',
            mime='text/csv',
        )

        uploaded_file = st.file_uploader("Choose a file")
        dataframe = pd.DataFrame()
        if uploaded_file is not None:
            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            dataframe.set_index(dataframe.columns[0], inplace=True)

            st.write("Input Data Sample View")
            st.write(dataframe.head())

            # Validate the file format
            required_col = sample.columns.tolist()
            given_col = dataframe.columns.tolist()

            if required_col == given_col:
                st.write("Valid file found")
                if st.button("Predict"):
                    test = dataframe.copy()
                    st.write(f"Predictions for {test.shape[0]} enteries.")
                    predicted = pickle_logistic.predict(test)
                    test['Converted'] = predicted
                    st.write(test)

                    st.subheader("Congratulations! Mission Successful")
                    st.write("Prediction complete")
                    csv = convert_df(test)
                    st.download_button(
                        label="Click to download",
                        data=csv,
                        file_name='predicticed_leads.csv',
                        mime='text/csv',
                    )

            else:
                st.write("Invlaid File Format")

        else:
            st.write("No File Uploaded")


if __name__ == '__main__':
    main()
