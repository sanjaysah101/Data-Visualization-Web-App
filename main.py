import pandas as pd
import matplotlib.pyplot as plt
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
    global df, filename, option, opt
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
            print(filename)
            # print(extension)
            if extension in allowedExtension:
                df = pd.read_csv(uploaded_file)     # Can be used wherever a "file-like" object is accepted:
                columnList = df.columns.values.tolist()     # to get list of columns
                option = st.selectbox("Select Column", columnList)
                st.subheader("Filters ")
                opt = showGraphList()
            else:
                st.write("File Formate is not supported")

def mainContent():
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
            # label = "Pie Chart for {} is".format(filename)
            # st.header(label)

            st.write(df[option].head(10))
            data = []
            for i in df[option].head(10):
                data.append(float(i))
            st.write(type(data[0]))

            x = np.array([35, 25, 25, 15])
            x = np.array(data, 'f')
            # mylabels = ["Python", "JavaScript", "C++", "C"]
            # x = float(df[option])


            fig = plt.figure(figsize=(10, 4))
            plt.pie(x)

            st.balloons()
            st.pyplot(fig)
            
        # else:
        #     st.write("Loading data")
    else:
        st.write("There is nothing to show!! please add file to see data")

if __name__ == "__main__":
    sidebar()
    mainContent()