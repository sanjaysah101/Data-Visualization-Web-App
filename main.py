from tkinter.tix import Tree
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

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
        uploaded_file = st.file_uploader("Choose a file")
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
        if opt == "Line Chart":
            label = "Line Chart for {} is".format(filename)
            st.header(label)
            st.line_chart(df[option])
        elif opt == "Bar Chart":
            label = "Bar Chart for {} is".format(filename)
            st.header(label)
            st.bar_chart(df[option])
        elif opt == "Pie Chart":
            label = "Pie Chart for {} is".format(filename)
            st.header(label)
            # st.write(df[option][5])
            # st.write(columnList[0])
            
            selectOption = []           
            # data = []
            for i in df[columnList[0]]:
                selectOption.append(i)
            selectedData = st.multiselect(f"chose {columnList[0]} to see", selectOption)
            
            dataToVisualize = []
            for i in selectedData:
                # st.write(getIndexes(columnList[0], i))                
                index = getIndexes(columnList[0], i)
                # st.write(df[option][index])
                dataToVisualize.append(df[option][index])
            
            # st.write("choose data",chooseData)
            # st.write("labels",selectedData)
            # st.write("labels",indexs)
            # st.write(type(option))

            # st.write(dataToVisualize)
            # for i in chooseData:
            #     data.append(i)
            #     # st.write(i)
            # st.write(df.loc[df[selectedData[0]]])
            #     # st.write(df.loc[df[i]])
            #     row = df.loc[df['Country'] == i]
            #     # st.write(row)
            #     st.write(row[option])
            # st.write(df.loc[df['Country'] == i])
            #     # st.write(df.loc[df[option] == i])
                
            # # st.write(columnList[0])
            
            x = np.array(dataToVisualize, 'f')
            # st.write(x)
            fig = plt.figure()
            plt.pie(x, labels = selectedData, autopct='%0.f%%')  # %).f%% means no of digit show after decimal

            # st.balloons()
            # st.write(option)
            plt.legend(title = option)
            st.pyplot(fig)
            
        # else:
        #     st.write("Loading data")
    else:
        st.write("There is nothing to show!! please add file to see data")

if __name__ == "__main__":
    sidebar()
    mainContent()

