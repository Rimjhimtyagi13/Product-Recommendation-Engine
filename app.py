'''import streamlit as st
import pickle

# Load models
items = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(product_name):
    import numpy as np
    index = items[items['name'] == product_name].index[0]
    similar_items = list(enumerate(similarity[index]))
    sorted_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:6]
    
    recommendations = []
    for i in sorted_items:
        recommendations.append(items.iloc[i[0]]['name'])
    
    return recommendations

# Streamlit UI
st.title("Product Recommendation System")
selected_product = st.selectbox("Choose a product",items['name'].values)


if st.button("Recommend"):
    results = recommend(selected_product)
    st.write("Recommended Products:")
   # st.image(product['image'], caption=product['name'], use_column_width=True)
    for product in results:
        st.write(product)
        #st.image(product['image'], caption=product['name'], use_container_width=True) 
import streamlit as st
import pandas as pd

# Load your dataset
items = pd.read_pickle('data.pkl')  # Assuming your data is stored in this file

# Function to display products with images
def display_product(product):
    st.write(f"**Product Name:** {product['name']}")
    st.image(product['image'], caption=product['name'], use_column_width=True)  # Display image
    st.write(f"**Price:** {product.get('price', 'N/A')}")
    st.write("---")

# Streamlit UI
st.title("Product Search Engine")

# Search input
query = st.text_input("Search for a product:")

# Filter products based on search query
if query:
    results = items[items['name'].str.contains(query, case=False, na=False)]
    if not results.empty:
        for _, product in results.iterrows():
            display_product(product)
    else:
        st.write("No products found.")'''
import streamlit as st
import pickle

# Load models
items = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(product_name):
    import numpy as np
    index = items[items['name'] == product_name].index[0]
    similar_items = list(enumerate(similarity[index]))
    sorted_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:6]
    
    recommendations = []
    for i in sorted_items:
        recommendations.append((items.iloc[i[0]]['name'], items.iloc[i[0]]['image']))  # Fetch image URLs
    
    return recommendations

# Streamlit UI
st.title("Product Recommendation System")

selected_product = st.selectbox("Choose a product", items['name'].values)

if st.button("Recommend"):
    results = recommend(selected_product)
    st.write("### Recommended Products:")
    
    for name, image in results:
        st.image(image, caption=name, width=150)
        st.write(f"**{name}**")  # Display product name

