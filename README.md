# Lead Predictions Streamlit Web App

## Overview

The Lead Predictions Web App is designed to predict lead conversions based on user-provided data. This interactive web application allows users to make predictions either one by one or in bulk. The predictions are generated using a machine learning model, and the app provides an easy-to-use interface for lead conversion forecasting.

## Getting Started

To get started with the Lead Predictions Web App, follow these steps:

1. Ensure you have Python and the required libraries installed on your system, including Streamlit, Pandas, and Pickle.

2. Clone this repository to your local machine.

3. Prepare the dataset for predictions. The app is designed to work with a specific set of categorical and numeric features. Refer to the input format described below.

## Input Format

The app requires input data in a specific format. Ensure your dataset adheres to the following format:

- **Categorical Features**: The app expects categorical features such as 'Lead Origin', 'Lead Source', 'Do Not Email', and others. The user interface will prompt you to select values for these features one by one.

- **Numeric Features**: Numeric features like 'Total Time Spent on Website' and 'Page Views Per Visit' are also required. You can enter these values as floating-point numbers between 0 and 1.

- **Bulk Predictions**: If you prefer to make bulk predictions, you can upload a CSV file containing the required columns. A sample file format is provided for reference.

## Making Predictions

### One by One Predictions

1. Select "One by One" from the dropdown menu.

2. Enter values for each categorical and numeric feature when prompted.

3. Click the "Predict" button to generate predictions.

### Bulk Predictions

1. Select "Bulk Predictions" from the dropdown menu.

2. Review the required file format provided in the app.

3. Upload a CSV file containing the required columns.

4. Click the "Predict" button to generate predictions for the entire dataset.

## Prediction Results

The app will display the prediction results, indicating whether a lead is likely to be converted successfully or not. You will also see a table with the input data and the corresponding predictions.

## Contributing

Contributions to this project are welcome. If you have suggestions, enhancements, or bug fixes, please feel free to submit pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE.md). See the LICENSE.md file for details.

## Acknowledgments

This project was created with the support of various open-source libraries, including Streamlit, Pandas, and Pickle.
