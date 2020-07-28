import numpy as np
import pandas as pd
import re
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
from nltk.corpus import stopwords
from collections import Counter
from nltk import tokenize,FreqDist
import nltk
from corpus import *



def show_word_cloud(s_d,length,character):
    from PIL import Image,ImageOps
    throne_mask = Image.open('throne1.png')
    throne_mask = ImageOps.grayscale(throne_mask)
    throne_mask = np.array(throne_mask)
    txt = get_text_of_character(s_d,character)
    
    stop_words=set(stopwords.words("english"))

    wc = WordCloud(background_color="black",mask=throne_mask,
                   max_words=length,stopwords=stop_words,
               contour_width=3,contour_color="white")
    wc.generate(txt)
    wc.to_file("m1.png")
    
    return wc

def data_sort(data):
    s_d = data.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    s_d['spoken_words']=s_d.dialogue.str.split().str.len()
    s_d=s_d.sort_values(['spoken_words'])
    s_d.reset_index(drop=True,inplace=True)
    return s_d

def show_top_by_season(df,snumber):
    try:
        df = df[df['season']==snumber].groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
        df['spoken_words'] = df.dialogue.str.split().str.len()
        df = data_sort(df)
        return df
    except:
        print("Invalid season number or record number")

def show_word_cloud_by_character_and_season(s_d,length,character,season):
    from PIL import Image,ImageOps
    throne_mask = Image.open('throne1.png')
    throne_mask = ImageOps.grayscale(throne_mask)
    throne_mask = np.array(throne_mask)
    
    data_character = get_data_by_character(s_d,character)
    data_character = get_data_by_season(data_character,season)
    txt = data_character.dialogue.values[0]
    
    stop_words=set(stopwords.words("english"))

    wc = WordCloud(background_color="black",mask=throne_mask,
                   max_words=length,stopwords=stop_words,
               contour_width=3,contour_color="white")
    wc.generate(txt)
    wc.to_file("m1.png")
    return plt.imshow(wc)

def get_data_all_seasons(df):
    df = df.groupby(['season','character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    df['spoken_words'] = df.dialogue.str.split().str.len()
    return df

def get_data_seasons(df):
    df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    df['spoken_words'] = df.dialogue.str.split().str.len()
    df = df.sort_values(by='spoken_words',ascending=False)
    l = list(df.character)
    
    return l[:100]

def get_data_by_character(df,character):
    data = df[df.character==character]
    return data

def get_data_by_season(df,season):
    df = df[df['season']==season].groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    df['spoken_words'] = df.dialogue.str.split().str.len()
    return df

def show_bar_by_character_allSeason(df,character):
    temp_data = get_data_all_seasons(df)
    temp_data = get_data_by_character(temp_data,character)
    # fig = px.bar(temp_data,x="season",y="spoken_words",color="spoken_words")
    # fig.update_layout(title=f"character {character}")
    return temp_data

def get_text_of_character(df,character):
    # temp_data = get_data_all_seasons(df)
    temp_data = get_data_by_character(df,character)
    temp_data=temp_data.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    
    txt = temp_data.dialogue[0]
    return txt

def get_most_spokenwords_by_character(df,character,number):
    
    txt=get_text_of_character(df,character)
    txt = preprocess_text(txt)
    freq = FreqDist(txt)
    freq = freq.most_common(number)
    x=[]
    y=[]
    for item in freq:
        y.append(item[0])
        x.append(item[1])
    x=x[::-1]
    y=y[::-1]
    df =pd.DataFrame({"words":y,"frequency":x})
    
    return df,len(txt)

def preprocess_text(txt):
    from nltk import RegexpTokenizer
    from nltk import PorterStemmer
    tokenizer = RegexpTokenizer(r"\w+")
    txt = re.sub("'s|'ve|'re|'t|'ll","",txt)
    new_words = tokenizer.tokenize(txt)
    stop_words_v1 = ['s','ve','ll','m','re','t','d','a','i','l']
    stop_words = set(stopwords.words("english"))
    new_words = [i.strip() for i in new_words if i.strip() not in stop_words and i.strip() not in stop_words_v1]

    return new_words

def get_character_by_season(df,season):
    df = df[df.season==season]
    df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    df = df.sort_values(by='character')
    df = df.character
    return list(df)

def get_overall_top(df):
    df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    df['words']=df.dialogue.str.split().str.len()
    df =df.sort_values(by='words')
    return df


def grouby_character(df):
    df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
    return df

def cal_character(df,character):
    score={"happy":0,"aggressive":0,"caring":0,"fear":0}
    txt = get_text_of_character(df,character)
    txt = preprocess_text(txt)
    freq = FreqDist(txt)
    words = freq.most_common(len(freq))
    for word in words:
        if word[0] in fear:
            score['fear']+=word[1]
        if word[0] in aggressive:
            score['aggressive']+=word[1]
        if word[0] in happy:
            score['happy']+=word[1]
        if word[0] in caring:
            score['caring']+=word[1]
    total = sum(score.values())
    percentage = [float(str(value/total)[:4]) for value in score.values()]
    
    data = pd.DataFrame({'emotion':['happy','aggressive','caring','fear'],
                             'percentage':percentage})

    return {'data':data,'x':'emotion','y':'percentage','color':'percentage'}

def how_similar(df,c1,c2):
    c1 = get_text_of_character(df,c1)
    c2 = get_text_of_character(df,c2)
    c1 = set(preprocess_text(c1))
    c2 = set(preprocess_text(c2))
    
    inter_val = c1.intersection(c2)
    return 100*float(len(inter_val))/(len(c1)+len(c2)-len(inter_val))

def most_name(df,ch):
    txt =get_text_of_character(df,ch)
    txt = preprocess_text(txt)
    df = get_overall_top(df).sort_values(by="words",ascending=False)
    whole_characters = list(df.character)[:50]
    dict_name={}
    for name in whole_characters:
        if name!='man':
            num = txt.count(name)
            if num!=0:
                dict_name[name]=num
    dict_name = sorted(dict_name.items(),key=lambda x:x[1],reverse=True)
    name=[]
    number=[]
    for i,j in dict_name:
        name.append(i)
        number.append(j)
    df = pd.DataFrame({"name":name,"number":number})
    return df.sort_values(by="number")

def total_words_season(df):
    temp= df.groupby(['season']).sum()
    temp.reset_index(inplace=True)
    return list(temp.total_words_spoken)

def cal_importance(df,ch):
    l=total_words_season(df)
    temp = show_bar_by_character_allSeason(df,ch).groupby(['season']).sum()
    temp.reset_index(inplace=True)
    n=len(temp.season)
    temp['total_words']=l[:n]
    temp['importance']=100*temp['spoken_words']/temp['total_words']
    total = temp['importance'].sum()
    temp['imp']=100*temp['importance']/total
    temp['season']=temp['season'].apply(lambda x: "season "+str(x))
    return temp[['season','imp']]

def load_data():
    df = pd.read_csv('final_data.csv')
    df = df.iloc[:,1:]
    return df
# df=load_data()
# print(how_similar(df,"jon","sam"))