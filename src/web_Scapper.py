import requests

def find_the_input(input_text:str):
    url = 'https://openai-openai-detector.hf.space/'
    text_input = input_text

    response = requests.get(url, params=text_input)
    string_dict = response.text
    dict_obj = eval(string_dict)
    human = round(dict_obj['real_probability']*100,2)
    GPT = round(dict_obj['fake_probability']*100,2)
    if human < GPT:
        return 'The given content is generated by AI : '+ str(GPT) + ' %'
    else:
        return 'The given content is generated by Human : '+ str(human) + ' %'

import newspaper

def get_paragraphs(url):
    # Initialize newspaper's Article object
    article = newspaper.Article(url)
    
    # Download and parse the article
    article.download()
    article.parse()
    
    # Return the extracted article text
    return article.text