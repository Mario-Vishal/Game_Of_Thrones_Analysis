import numpy as np
import pandas as pd
import re
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image,ImageOps
from wordcloud import WordCloud,STOPWORDS
from nltk.corpus import stopwords
from collections import Counter
from nltk import tokenize,FreqDist
from nltk import RegexpTokenizer
from nltk import PorterStemmer
import nltk
from corpus import *



class gotLib:
    def __init__(self,emotions,data):
        self.data=data
        self.e = emotions
        
    def load_data(self):
        self.data = pd.read_csv('final_data.csv')
        self.data = self.data.iloc[:,1:]
        self.data['dialogue']=self.data.dialogue.str.lower()
        
    def load_data_manual(self,df):
        self.data = df

    def copy(self):
            return self.data.copy()


    def get_overall_top_sort(self):
            df=self.copy()
            df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            df['words']=df.dialogue.str.split().str.len()
            df =df.sort_values(by='words',ascending=False)
            return df

    def show_word_cloud(self,length,character):
            s_d = self.copy()
            throne_mask = Image.open('images/throne1.png')
            throne_mask = ImageOps.grayscale(throne_mask)
            throne_mask = np.array(throne_mask)
            txt = self.get_text_of_character(character)

            stop_words=set(stopwords.words("english"))

            wc = WordCloud(background_color="black",mask=throne_mask,
                           max_words=length,stopwords=stop_words,
                       contour_width=3,contour_color="white")
            wc.generate(txt)
            

            return wc

    def data_sort(self,df):
            ''' Returns the sorted data based on the spoken words'''
            
            s_d = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            s_d['spoken_words']=s_d.dialogue.str.split().str.len()
            s_d=s_d.sort_values(['spoken_words'])
            s_d.reset_index(drop=True,inplace=True)
            return s_d

    def show_top_by_season(self,snumber):
            df = self.copy()
            try:
                df = df[df['season']==snumber].groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
                df['spoken_words'] = df.dialogue.str.split().str.len()
                df = self.data_sort(df)
                return df
            except:
                print("Invalid season number or record number")


    def get_data_all_seasons(self):
            df = self.copy()
            df = df.groupby(['season','character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            df['spoken_words'] = df.dialogue.str.split().str.len()
            return df

    def get_data_seasons(self):

            ''' Returns only top 100 characters based on the number of dialogues'''

            df=self.copy()
            df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            df['spoken_words'] = df.dialogue.str.split().str.len()
            df = df.sort_values(by='spoken_words',ascending=False)
            l = list(df.character)
            return l[:100]

    def get_data_by_character(self,df,character):
#             df = self.copy()
            df = df[df.character==character]
            return df

    def get_data_by_season(self,season):
            df=self.copy()
            df = df[df['season']==season].groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            df['spoken_words'] = df.dialogue.str.split().str.len()
            return df

    def show_bar_by_character_allSeason(self,character):
            df = self.copy()
            temp_data = self.get_data_all_seasons()
            temp_data = self.get_data_by_character(temp_data,character)
            # fig = px.bar(temp_data,x="season",y="spoken_words",color="spoken_words")
            # fig.update_layout(title=f"character {character}")
            return temp_data

    def get_text_of_character(self,character):
            # temp_data = get_data_all_seasons(df)
            df = self.copy()
            temp_data = self.get_data_by_character(df,character)
            temp_data=temp_data.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            txt = temp_data.dialogue[0]
            return txt

    def get_most_spokenwords_by_character(self,character,number):
            '''
            returns a Data Frame containing words and frequency of that character,
            and the length of the entire dialogue of that character
            '''
            df = self.copy()
            txt= self.get_text_of_character(character)
            txt = self.preprocess_text(txt)
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

    def preprocess_text(self,txt):
            '''
            returns a list of words which are processed like tokenizing,removing stopwords
            '''

            tokenizer = RegexpTokenizer(r"\w+")
            txt = re.sub("'s|'ve|'re|'t|'ll","",txt)
            new_words = tokenizer.tokenize(txt)
            stop_words_v1 = ['s','ve','ll','m','re','t','d','a','i','l']
            stop_words = set(stopwords.words("english"))
            new_words = [i.strip() for i in new_words if i.strip() not in stop_words and i.strip() not in stop_words_v1]

            return new_words

    def get_character_by_season(self,season):
            '''
            returns a list of characters present in the given season
            '''
            df = self.copy()
            df = df[df.season==season]
            df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            df = df.sort_values(by='character')
            df = df.character
            return list(df)

    def get_overall_top(self):
            '''
            returns a Data Frame sorted by the number of words
            '''
            df = self.copy()
            df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            df['words']=df.dialogue.str.split().str.len()
            df =df.sort_values(by='words')
            return df


    def grouby_character(self):
            '''
            returns a Data Frame where it is grouped by character and dialogue
            '''
            df=self.copy()
            df = df.groupby(['character'])['dialogue'].apply(lambda x:' '.join(x)).reset_index()
            return df

    def cal_character(self,character):
        
            '''
            returns a dictionary containing data,x attribute,y attribute and color
            Note : this function is modified for the use of plolty
            '''
            df = self.copy()
            score={"happy":0,"aggressive":0,"caring":0,"fear":0}
            txt = self.get_text_of_character(character)
            txt = self.preprocess_text(txt)
            freq = FreqDist(txt)
            words = freq.most_common(len(freq))
            for word in words:
                if word[0] in self.e.fear():
                    score['fear']+=word[1]
                if word[0] in self.e.aggressive():
                    score['aggressive']+=word[1]
                if word[0] in self.e.happy():
                    score['happy']+=word[1]
                if word[0] in self.e.caring():
                    score['caring']+=word[1]
            total = sum(score.values())
            percentage = [float(str(value/total)[:4]) for value in score.values()]

            data = pd.DataFrame({'emotion':['happy','aggressive','caring','fear'],
                                     'percentage':percentage})

            return {'data':data,'x':'emotion','y':'percentage','color':'percentage'}

    def how_similar(self,c1,c2):
            '''
            returns a similarity score of two characters
            '''
            c1 = self.get_text_of_character(c1)
            c2 = self.get_text_of_character(c2)
            c1 = set(self.preprocess_text(c1))
            c2 = set(self.preprocess_text(c2))

            inter_val = c1.intersection(c2)
            return 100*float(len(inter_val))/(len(c1)+len(c2)-len(inter_val))

    def most_name(self,ch):
            '''
            returns a Data Frame with 2 columns name,number where number contains
            how many times they used that name in their dialogue
            '''
            df= self.copy()
            txt =self.get_text_of_character(ch)
            txt = self.preprocess_text(txt)
            df = self.get_overall_top().sort_values(by="words",ascending=False)
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

    def total_words_season(self):
        
        ''' 
        Returns a list of size 8 resembling each season where each element
        is the total number of dialogues of that whole season
        '''
        df = self.copy()
        temp= df.groupby(['season']).sum()
        temp.reset_index(inplace=True)
        return list(temp.total_words_spoken)

    def cal_importance(self,ch):
        
        '''
        Returns a Data Frame of 2 columns "season","imp" where the imp column
        contains the importance value of that character respective to that season
        
        '''
        df = self.copy()
        l=self.total_words_season()
        temp = self.show_bar_by_character_allSeason(ch).groupby(['season']).sum()
        temp.reset_index(inplace=True)
        n=len(temp.season)
        temp['total_words']=l[:n]
        temp['importance']=100*temp['spoken_words']/temp['total_words']
        total = temp['importance'].sum()
        temp['imp']=100*temp['importance']/total
        temp['season']=temp['season'].apply(lambda x: "season "+str(x))
        return temp[['season','imp']]
    