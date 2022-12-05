import streamlit as st
from gotLibrary import GotLib
import plotly.express as px
import pandas as pd 
import matplotlib.pyplot as plt

class plot_type:
    def __init__(self,data):
        self.data = data
        self.fig=None
        self.update_layout=None

    def bar(self,x,y,color):
        self.fig=px.bar(self.data,x=x,y=y,color=color)

    def pie(self,x,y):
        self.fig = px.pie(self.data,values=x,names=y)

        
    def set_title(self,title):
        
        self.fig.update_layout(
                title=f"{title}",
                    yaxis=dict(tickmode="linear"),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white',size=18))

    def set_title_x(self,title):
        
        self.fig.update_layout(
                title=f"{title}",
                    xaxis=dict(tickmode="linear"),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white',size=18))

    def set_title_pie(self,title):
        self.fig.update_layout(title=title,
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                font=dict(color='white',size=18))
        


    def plot(self):
        st.write(self.fig)

class slide_bar:
    value=4
    def __init__(self,title,x,y):
        self.title = title
        self.x=x
        self.y=y
        self.slide_bar = None
        

    def set(self):
        self.slide_bar = st.slider(self.title,self.x,self.y)
        slide_bar.value=self.slide_bar

class select_box:
    value="tyrion"
    def __init__(self,data):
        self.data=data
        self.box=None
    def place(self,title,key):
        header(title)
        self.box = st.selectbox(str(key),self.data)
        select_box.value=self.box

def title(text,size,color):
    st.markdown(f'<h1 style="font-weight:bolder;font-size:{size}px;color:{color};text-align:center;">{text}</h1>',unsafe_allow_html=True)

def header(text):
    st.markdown(f"<p style='color:white;'>{text}</p>",unsafe_allow_html=True)




@st.cache(persist=True,suppress_st_warning=True)
def load_data():
    df = pd.read_csv('final_data.csv')
    df = df.iloc[:,1:]
    return df

#loading the data
df = load_data()

#intializing the GotLib object
got = GotLib(df)



with open("styles/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


#-------------------------------Header-----------------------

st.markdown('<h1 style="text-align:center;color:white;font-weight:bolder;font-size:100px;">GAME<br>OF<br>THRONES</h1>',unsafe_allow_html=True)
# st.markdown('<h1 style="text-align:center;color:white;background-image:url("m1.png");">An analysis..</h1>',unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;color:white;">An analysis..</h2>',unsafe_allow_html=True)
st.image('images/got1.jpg',width=700)
st.markdown('### This is an analysis based project on the tv series game of thrones')



#------------------------Module 1--------------------------
title("Top characters based on number of words spoken in a season",60,"white")

header('season')

option_1_s = st.selectbox('',[1,2,3,4,5,6,7,8])

header("number of results")
num = st.slider("",4,50)

temp_data = got.show_top_by_season(option_1_s)
number=10

bar1 = plot_type(temp_data[-num:])
bar1.bar("spoken_words","character","spoken_words")
bar1.set_title(f"Season {option_1_s}")
bar1.plot()


#-----------------------Module 2------------------------------

title("Overall top characters based on number of spoken words",60,'white')

header("number of results")

num1 = st.slider("",5,60)

temp_data1 = got.get_overall_top()

bar2 = plot_type(temp_data1[-num1:])
bar2.bar("words","character","words")
bar2.set_title("Overall Top")
bar2.plot()

#------------------------Module 3-----------------------------

title("Character's number of dialogues over the seasons",60,"white")
st.markdown('### NOTE: displaying only top 100 characters in drop downs as there are more than 500+ it would be awkward to display it all :)')

characters = got.get_data_seasons()
stb1 = select_box(characters)
stb1.place("character",0)
@st.cache(persist=True)
def sbyc(df,stb1):
    return got.show_bar_by_character_allSeason(stb1)

t_data = sbyc(df,stb1.value)

bar0 = plot_type(t_data)
bar0.bar("season","spoken_words","spoken_words")
# bar0.update_layout(title=f"{stbl.value}")
bar0.set_title_x(stb1.value)

bar0.plot()

#----------------------Module 4----------------------------------

title("Percentage distribution of a character's performance in seasons",60,"white")
st.write("what is the character's distribution of his/her/(uhh. you know the rest) dialogue percentage over the seasons")

stb2 = select_box(characters)
stb2.place("character",9)
t_data1 = got.cal_importance(df,stb2.value)

pie2 = plot_type(t_data1)
pie2.pie("imp","season")
pie2.set_title_pie(stb2.value)
pie2.plot()


#-------------------------Module 5-----------------------------

title('Most spoken words by a character',60,'white')
st.markdown('#### removing all the stop words aka common words.')



select_box1 = select_box(characters)
select_box1.place('character',1)
header("range")
num2 = slide_bar("",5,55)
num2.set()
temp_data2,size = got.get_most_spokenwords_by_character(df,select_box1.value,num2.value)


bar3 = plot_type(temp_data2)
bar3.bar("frequency","words","frequency")
bar3.set_title(f"{select_box1.value.capitalize()} total words spoken - {size}")
bar3.plot()

#--------------------------WORD_CLOUD---------------------------

title("WordCloud of a character",60,'white')
st.markdown('#### It may take a few seconds to load the result, so please hold on to your dragons.')

select_box2 = select_box(characters)
select_box2.place('character',2)

header('range')
sl = slide_bar('',50,200)
sl.set()
@st.cache(persist=True,suppress_st_warning=True)
def swc(df,v1,v2):
    return got.show_word_cloud(df,v1,v2)
wc = swc(df,sl.value,select_box2.value)
fig = plt.figure(figsize=(8,8))
plt.imshow(wc,interpolation="bilinear")
plt.axis('off')
plt.title(select_box2.value,fontsize=18)
plt.tight_layout()
st.pyplot(fig)

#--------------------------Module 4------------------------------

title("Emotional characteristics",70,"white")
st.write("The below pie chart depicts the distribution of emotions of a character.")
st.write('Note: This is purely my calculations based on the text-corpus I created and also based on the words used by a character.')

select_box3 = select_box(characters)
select_box3.place('character',3)

temp_data3 = got.cal_character(select_box3.value)
pie1 = plot_type(temp_data3['data'])
pie1.pie(temp_data3['y'],temp_data3['x'])
pie1.set_title_pie(select_box3.value)
pie1.plot()

#---------------------------Module 5--------------------------
title("Most used name by a character",50,"white")

stb = select_box(characters[:50])
stb.place("character",4)
temp_df = got.most_name(stb.value)
num_range = temp_df.shape[0]
rangesl = slide_bar("",1,num_range)
rangesl.set()

bar5 = plot_type(temp_df.iloc[-rangesl.value:,:])
bar5.bar("number","name","number")
bar5.set_title(stb.value)
bar5.plot()



#----------------------Module 6----------------------------------

title('Similar Characters',60,'white')
st.write('The chart shows characters who are similar to a character with their similarity precentage, based on their similar usage of words, this same alogrithm is also used in movie recommender systems.')
st.write('Note: This is very much experimental and purely based on the scripts. And only depends on script text and nothing else.')
ch=characters[:]
ch1 = select_box(ch)
ch1.place('character',5)
val=ch1.value


results = got.get_similar_character(val)

colors = ['rgb(0,255,42)','rgb(221, 235, 30)','rgb(224, 91, 43)']
char = list(results['character'])
score = list(results['similarity'])
i=0
for name,sc in zip(char,score):
    
    st.markdown(f"<h3 style='text-align:center;color:rgb(196, 196, 196);'><span style='font-weight:bolder;color:{colors[i]};font-size:50px;'>{name} </span> [{sc}%]</h3>",unsafe_allow_html=True)
    i+=1


#----------------------------------------------------------------------THE END---------------------------------------------------------------------

st.write(' ')

st.markdown('#### The dataset here is created from the scripts, involved a lot of data cleaning,wrangling and pre-processing!. Took a lot of time to prepare it!. And is 85% accurate.')

st.write('check the box below to peak at the dataset')
if st.checkbox('',False):
    st.subheader("Game_of_Thrones")
    st.write(df)

st.write('')
st.write('')


st.markdown('<h3 style="text-align:center;">Made By <span style="color:#4f9bce;font-weight:bolder;font-size:40px;">Mario 😎</span></h3>',unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;text-decoration:none;font-weight:bolder;"><a style="text-decoration:none;color:rgb(96, 235, 133);" href="https://github.com/Mario-Vishal">-> GitHub <-</a></h2>',unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;text-decoration:none;font-weight:bolder;"><a style="text-decoration:none;color:rgb(20, 166, 219);" href="https://www.linkedin.com/in/mario-vishal">-> Linkedin <-</a></h2>',unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;text-decoration:none;font-weight:bolder;"><a style="text-decoration:none;color:red;" href="mailto:mariovishal12@gmail.com">-> Contact Me <-</a></h2>',unsafe_allow_html=True)




