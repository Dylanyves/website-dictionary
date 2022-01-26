from pyparsing import Word
import streamlit as st
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

st.set_page_config(
    page_title='Dictionary',
    page_icon='book'
)

class Content:
    def head():
        st.title('Dictionary')

    def body():
        with st.form(key='dict_form'):
            word = st.text_input(label='Input Word')
            search_btn = st.form_submit_button('Search')

        if search_btn:
            try:
                st.subheader(f'Define - {word}')
                syns = wordnet.synsets(word)

                # Check if input is valid
                syns[0]
                st.write('---')

                for syn in syns:
                    if syn.examples():

                        # Definition
                        definition = syn.definition()
                        st.write(f'**{definition.capitalize().replace(";", "")}**')

                        # Syntax
                        syntax = {
                            'n':'Noun',
                            'v':'Verb',
                            'a':'Adjective',
                            'r':'Adverb',
                            's':'Adjective Satellite'
                        }
                        try:
                            st.write(f'_{syntax[syn.pos()]}_')
                        except:
                            pass

                        # Examples
                        for index, example in zip(range(1, 4) ,syn.examples()):
                            st.write(index, example)       
                        st.write('')         

                        # Synonyms and Antonyms
                        synonyms = list()
                        antonyms = list()

                        for l in syn.lemmas():
                            synonyms.append(l.name())

                            if l.antonyms():
                                for a in l.antonyms():
                                    antonyms.append(a.name())

                        try:
                            synonyms.remove(word)
                        except:
                            pass
                            
                        if synonyms:
                            output_syn = ', '.join(synonyms)
                            st.write(f'_**Synonyms**: {output_syn.replace("_", " ")}_')
                        if antonyms:
                            output_ant = ', '.join(antonyms)
                            st.write(f'_**Antonyms**: {output_ant.replace("_", " ")}_')


                        st.write('---')

            except Exception as e:
                st.warning(e)



c = Content
c.head()
c.body()