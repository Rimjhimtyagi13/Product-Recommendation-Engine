Product Recommendation System

## Overview
This is a **Product Recommendation System** built using Streamlit, Pandas, and machine learning techniques. The system suggests similar products based on user-selected items by utilizing a precomputed similarity matrix.

 Features
- **Product Selection:** Users can choose a product from a dropdown menu.
- **Recommendation Engine:** The system provides five similar products based on the selected item.
- **Product Images:** Displays images of the recommended products.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle (for model storage)

## Installation
### Prerequisites
Ensure you have Python installed (version 3.x recommended). Install the required libraries using:

pip install streamlit pandas scikit-learn




### Run the Application

streamlit run app.py


Files in the Repository
- `app.py` - Main Streamlit app
- `data.pkl` - Processed dataset
- `similarity.pkl` - Precomputed similarity matrix
- `Product_Search_Engine` - Main Code

### License
This project is licensed under the [MIT License](LICENSE).

Acknowledgments
- Dataset: Amazon Product Dataset
- Libraries: Streamlit, Pandas, Scikit-learn

Contact
For questions or suggestions, feel free to reach out or open an issue.

