import pandas
import streamlit

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("pick some Fruits:", list(my_fruit_list.index),['Pear','Peach'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

