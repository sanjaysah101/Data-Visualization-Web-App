import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import empty
import streamlit as st
import numpy as np



PAGE_CONFIG = {"page_title":"Data Visualization","page_icon":"chart_with_upwards_trend:", "layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def showGraphList():
    """This function will return all the graph available"""    
    graph = ["Line Chart", "Bar Chart", "Pie Chart"]
    # graph = {0: "Line Chart", 1:"Bar Chart"}
    # opt = ""
    opt = st.radio("Select to ",graph)
    # for i in graph:
    #     opt = st.checkbox(i)
    return opt

def sidebar():
    global df, filename, option, opt, columnList
    df = None
    allowedExtension =['csv', 'xlsx']
    # linegraph = ""
    with st.sidebar:
        uploaded_file = st.sidebar.file_uploader(label="Upload your csv or excel file (200 MB Max).", type=['csv','xlsx'])
        # uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            filename = uploaded_file.name   
            extension = filename[filename.index(".")+1:]
            filename = filename[:filename.index(".")]
            # print(filename)
            # print(extension)
            if extension in allowedExtension:
                df = pd.read_csv(uploaded_file)     # Can be used wherever a "file-like" object is accepted:
                columnList = df.columns.values.tolist()     # to get list of columns
                option = st.selectbox("Select Column", columnList)
                st.subheader("Filters ")
                opt = showGraphList()
            else:
                st.write("File Formate is not supported")
def getIndexes(columnName, value):
    # st.write(df[columnName])
    # st.write(value)
    count = -1
    for i in df[columnName]:
        count += 1
        # print(i, value)
        if i == value:
            # print(count)
            # print(True, value, "index = ",  count)
            # st.write(count) 
            return count



def mainContent():
    st.header("Visualize Your Data")
    if df is not None:
        st.write(df)
        # graph = ["Line Chart", "Bar Chart"]
        label = "Chose the Column To which you want to compare"
        st.header(label)            
        columnLists = df.columns.values.tolist()     # to get list of columns
        # labelColumn = st.selectbox("Select Column", columnLists)
        
        selectOption = []           
        for i in df[columnList[0]]:
            selectOption.append(i)
        selectedData = st.multiselect(f"Choose {columnList[0]} to see", selectOption)

        dataToVisualize = []
        for i in selectedData:
            # st.write(getIndexes(columnList[0], i))                
            index = getIndexes(columnList[0], i)
            # st.write(df[option][index])
            # st.write(df[option][index])
            value = df[option][index]
            if type(value) is not str:
                dataToVisualize.append(df[option][index])
            else:
                st.warning(f"The data type of {value} is not supporte")



        if opt == "Line Chart":
            label = "Line Chart for {} is".format(filename)
            st.header(label)
            st.line_chart(dataToVisualize)

        elif opt == "Bar Chart":
            label = "Bar Chart for {} is".format(filename)
            st.header(label)
            st.bar_chart(dataToVisualize)
        elif opt == "Pie Chart":          
            label = "Pie Chart for {} is".format(filename)
            st.header(label)  
            x = np.array(dataToVisualize, 'f')
            # st.write(x)
            fig = plt.figure(figsize=(10,10))
            if len(dataToVisualize) != 0:
                plt.pie(x, labels = selectedData, autopct='%.5f%%')  # %).f%% means no of digit show after decimal

            # st.balloons()
            # st.write(option)
                plt.legend(title = option)
                st.pyplot(fig)
            else:
                st.write("There is nothing to show!!")
        # else:
        #     st.write("Loading data")
    else:
        st.write("There is nothing to show!! please add file to see data")

if __name__ == "__main__":
    sidebar()
    mainContent()

