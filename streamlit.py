import streamlit as st
import pandas as pd
import plotly.express as px
table = pd.DataFrame({"column1":[1,2,3,4,5,6,7], "column2":[22,45,90,78,65,78,100]})
st.title("HI STREAMLIT IS POWERFUL FOR WEB APPLICATION")
st.write(table)
st.text("streamlit is used by data science for them to create visualization app in datascience.")

## Add visualization to streamlit 
heatmap_fig = px.imshow(table.values,x=table.columns,y=table.index,color_continuous_scale="viridis")
st.plotly_chart(heatmap_fig, use_container_width=True)

## pie chart
pie_chart_fig = px.pie(table, values="column2", names="column1", title= "Pie Chart")
st.plotly_chart(pie_chart_fig, use_container_width=True)


## Bar plot
bar_plot_fig = px.bar(table, x="column1", y="column2", title="pie chart")
st.plotly_chart(bar_plot_fig, use_container_width=True)

## Treemap
treemap_data = pd.DataFrame({
  "category":["Bola", "Ahmed", "Musa", "Shola", "Adamu","Grace","Blessing"],
  "subcategory":["Biologist","Engineer", "Full Stack Developer", "Medical Doctor", "Nurse", "Data scientist", "App developer"],
  "value":[10,20,30,40,50,60,70]})

treemap_fig = px.treemap(treemap_data, path=["category","subcategory"], values="value")
st.plotly_chart(treemap_fig, use_container_width=True)

## map
choropleth_data = pd.DataFrame({
  "country":["Nigeria", "Ghana", "Togo", "Benin", "Cameroon", "Congo", "Senegal", "canada", "Russia","china"],
  "value":[10,20,30,40,50,60,70,90,86,85]})
st.title("Choropleth Map For Country")
st.write(choropleth_data)
st.text("Choropleth maps visualization geographical data.")
choropleth_fig = px.choropleth(choropleth_data, locations="country", locationmode="country names", color="value",
                               title="Choropleth Map", color_continuous_scale="deep")
st.plotly_chart(choropleth_fig, use_container_width=True)

  
