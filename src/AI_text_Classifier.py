import streamlit as st
from src.web_Scapper import find_the_input
from src.seperater import spliter
from src.rowgenerater import rowgen
from src.web_Scapper import get_paragraphs
from src.pdf import header_footer_cuter
from src.pdf_textretrive import pdf_text,text_retrive
import pandas as pd

def Text_Classifier():
    w1,col1,col2,w2=st.columns((1,1.5,2.5,1))
    w12,col11,col22,w22=st.columns((1,1.5,2.5,1))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    with col1:
        st.write('# ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Input Type</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_input = st.selectbox('',['Select','Text input','File format','Website URL'])

    # Text input
    if vAR_input == 'Text input':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Input Text</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_text = st.text_area('')
            vAR_text = ' '.join(vAR_text.split())
        if vAR_text !="":
            with col2:
                if st.button("Submit"):
                    if len(vAR_text)<400:
                        vAR_response = find_the_input(vAR_text)
                        with col2:
                            st.success(vAR_response)
                    else:
                        prompt=spliter(vAR_text)
                        result=[]
                        for j in prompt:
                            vAR_response = find_the_input(j)
                            result.append(vAR_response)
                        default=rowgen(result)
                        with cc1:
                            df=pd.DataFrame({"Wordcount":default,"Result":result})
                            st.dataframe(df)
    # files format
    elif vAR_input == 'File format':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Enter File format</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_file_type = st.selectbox("",['Select','Text file','PDF file'])
        
        
        # Text file
        if vAR_file_type == 'Text file':
            with col1:
                st.write('## ')
                st.write('# ')
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Upload File Here</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_file = st.file_uploader('',type='txt')
            if vAR_file is not None:
                txt_content = text_retrive(vAR_file)
                with col1:
                    st.write('# ')
                    st.write('# ')
                    st.write("## ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Preview</span></p>", unsafe_allow_html=True)
                with col2:
                    vAR_preview = st.selectbox("",['Select','Yes','No'],key='prw2')
                if vAR_preview == 'Yes':
                    st.write(txt_content)
                elif vAR_preview == 'No':
                    pass
                else:
                    pass
                txt_content = ' '.join(txt_content.split())
                with col2:
                    # try:
                        if st.button("Submit"):
                            if len(txt_content)<400:
                                vAR_response = find_the_input(txt_content)
                                with col2:
                                    st.success(vAR_response)
                            else:
                                prompt=spliter(txt_content)
                                result=[]
                                for j in prompt:
                                    vAR_response = find_the_input(j)
                                    result.append(vAR_response)
                                default=rowgen(result)
                                with cc1:
                                    df=pd.DataFrame({"Wordcount":default,"Result":result})
                                    st.dataframe(df)
                    # except Exception as e:
                        # st.error("Text cannot be extracted from Uploaded File")
        # PDF file
        elif vAR_file_type == 'PDF file':
            with col1:
                st.write('## ')
                st.write('# ')
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Upload File Here</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_file = st.file_uploader('',type='pdf')
            if vAR_file is not None:
                try:
                    header_footer_cuter(vAR_file)
                    vAR_pdf_content = pdf_text()
                    with col1:
                        st.write('# ')
                        st.write('# ')
                        st.write("## ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Preview</span></p>", unsafe_allow_html=True)

                    with col2:
                        vAR_preview = st.selectbox("",['Select','Yes','No'],key='prw1')
                        if vAR_preview == 'Yes':
                            st.write(vAR_pdf_content)
                        elif vAR_preview == 'No':
                            pass
                        else:
                            pass
                    vAR_pdf_content = ' '.join(vAR_pdf_content.split())
                    with col2:
                        if st.button("Submit"):
                            if len(vAR_pdf_content)<400:
                                vAR_response = find_the_input(vAR_pdf_content)
                                with col2:
                                    st.success(vAR_response)
                            else:
                                prompt=spliter(vAR_pdf_content)
                                result=[]
                                for j in prompt:
                                    vAR_response = find_the_input(j)
                                    result.append(vAR_response)
                                default=rowgen(result)
                                with cc1:
                                    df=pd.DataFrame({"Wordcount":default,"Result":result})
                                    st.dataframe(df)
                except Exception as e:
                    st.error("Text cannot be extracted from Uploaded File")
    # websit input
    elif vAR_input == 'Website URL':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Enter the Website link</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_link = st.text_input('')
        if vAR_link !="":
            vAR_text = get_paragraphs(vAR_link)
            with col1:
                st.write('# ')
                # st.write('# ')
                # st.write("## ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Preview</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_preview = st.selectbox("",['Select','Yes','No'],key='prw2')
                if vAR_preview == 'Yes':
                    st.write(vAR_text)
                elif vAR_preview == 'No':
                    pass
                else:
                    pass
            vAR_text = ' '.join(vAR_text.split())
            with col2:
                try:
                    if st.button("Submit"):
                        if len(vAR_text)<400:
                            vAR_response = find_the_input(txt_content)
                            with col2:
                                st.success(vAR_response)
                        else:
                            prompt=spliter(vAR_text)
                            result=[]
                            for j in prompt:
                                vAR_response = find_the_input(j)
                                result.append(vAR_response)
                            default=rowgen(result)
                            with cc1:
                                df=pd.DataFrame({"Wordcount":default,"Result":result})
                                st.dataframe(df)
                except Exception as e:
                    st.error("Text cannot be extracted from Uploaded URL")