import pandas as pd
import pickle
import streamlit as st
import sklearn

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

# pickle_logistic
with open('logistic_model.pkl', 'rb') as file:
    st.write("importing model")
    pickle_logistic = pickle.load(file)

def main():
    st.write("Select Categorical Column")
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

    st.write("select numerical column")
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
        test = pd.DataFrame([features], columns=feature_list)
        predicted = pickle_logistic.predict(test)
        if predicted:
            st.write("This lead will be converted successfully.")
        else:
            st.write("This is a failure.")


if __name__ == '__main__':
    main()
