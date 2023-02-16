import pandas
import streamlit
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruits_selected = streamlit.multiselect("pick some Fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)


streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


