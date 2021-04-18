import json
import urllib.request
import string
import random
import streamlit as st

st.markdown("<h1 style='text-align: center; color: White;background-color: Red'>Random Youtube Video Generator</h1>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>Just the choose the number of videos to generate</h3>",unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center; color: Black;'>Project by Cookie Clan</h4>", unsafe_allow_html=True)
st.image('you.png')
st.sidebar.header("What is this Project about?")
st.sidebar.text("It a Web app that would help the user to generate youtube urls.")
st.sidebar.header("What tools where used to make this?")
st.sidebar.text("Python and google dev API")
st.sidebar.header("I hope you like to my product!")
st.sidebar.header("Find me : @suvoo_o")

count = st.number_input("Enter the number of videos to generate",min_value = 0,max_value=100,value = 20,step = 1)

API_KEY = 'AIzaSyDdj9lRzF38phWaJSe5jCKeg-xTD_1mjnA'
random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))


st.markdown("<h2 style='text-align: center; color: White;background-color: Red'>Here is a list of videos</h2>",unsafe_allow_html=True)
i = 0
for data in results['items']:
    i+=1
    videoId = (data['id']['videoId'])
    ans = 'https://www.youtube.com/watch?v=' + videoId
    st.write(i,ans)

