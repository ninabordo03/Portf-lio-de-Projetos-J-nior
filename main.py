import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import time

st.set_page_config(
    page_title= 'My first Streamlit',
    layout= 'wide'
)

st.header('Oi')
st.subheader('Tudo bem?')
st.text('Com certeza!')
df = pd.read_csv('penguins_size.csv')
st.write(df)
st.dataframe(df, width=100000, height=100)
st.dataframe(df, width=10, height=20)
code = '''def func(x):
            return x**2
'''
st.code(code, language='python')
d = {'a':1, 'b':2, 'c':3}
st.write(d)


fig1, ax = plt.subplots()
ax.scatter(np.arange(5), np.arange(5)**2)
st.write(fig1)

st.write(st.error)

st.dataframe(np.random.randn(50, 20))

st.metric('TCS Stock', value='3220.70', delta='19.10', delta_color='inverse')

df = pd.DataFrame(np.random.randn(10, 2), columns=['prices', 'diff'])
st.line_chart(df, y='diff')
st.area_chart(df, x='prices')
st.bar_chart(df)
fig, ax = plt.subplots()
#ax.scatter(np.arange(10), np.arange(10) ** 2)
#st.pyplot(fig)
ax.hist(np.random.randn(100), bins=10)
st.pyplot(fig)

places = pd.DataFrame({'lat': [-41, -8.07], 'lon': [-38.05, -10]})
st.map(places)

pr = st.button('Click me')
if pr == True:
    st.write(time.time())

option = st.selectbox(
    label = 'Where do you live?',
    options= ('New York', 'Vienna', 'Montreal')
)
if option == 'New York':
    st.write('You live in NY')

option = st.radio(
    label = 'Order your food',
    options= ('Pizza', 'McDonalds', 'Burguer King'),
    index= 1 #ele marca o respectivo indice
)

ck = st.checkbox('I agree', value = True)
if ck == True:
    st.write('Done')
else:
    st.write('Not done')

txt = 'Hello'
st.download_button(
    label = 'Download the text',
    data = txt
)

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns= ['1', '2']
)
data = df.to_csv().encode(('utf-8'))
st.download_button(
    label='Download',
    data = data,
    file_name='Csv.csv',
    mime = 'text/csv'
)

num = st.slider(
    label = 'Age',
    min_value= 10,
    max_value= 100,
    value = 21,
    step= 1
)

st.write(num)

txt = st.text_input(
    label = 'Enter your email',
    max_chars= 100,
    placeholder='Your email here'
)
st.write(txt)

passw = st.text_input(
    label = 'Enter your password',
    max_chars= 50,
    placeholder= 'Your password here',
    type = 'password'
)
st.write(passw)

txt = st.text_area(
    label = 'Type something',
    height= 50,
    max_chars= 1000,
    placeholder= 'Write here'
)
st.write(txt)

dat = st.date_input('Your birthday', value=datetime.date(2003, 3, 29))
st.write(dat)

tim = st.time_input('Meal time', value=datetime.time(14, 00), step=300)
st.write(tim)

fl = st.file_uploader(
    label = 'Upload here'
)

from PIL import Image
from io import StringIO

if fl:
    st.write(fl.type)
    if 'image' in fl.type:
        img = Image.open(fl)
        st.write(np.array(img).shape)
    elif fl.type == 'text/plain':
        stringio = StringIO(fl.getvalue().decode('utf-8'))
        stringdata = stringio.read()
        st.write(stringio)

color = st.color_picker('Pick a color')
if color:
    st.write(f'You selected {color}')

choice = st.sidebar.radio(
    label = 'Choose one',
    options= ('1', '2')
)

cont = st.container()
st.write('st')
cont.write('cont')
st.write('1st')
cont.write('1cont')
'''
txt = '% completed'
mybar = st.progress(0, text = txt)
for pr in range(100):
    time.sleep(0.1)
    mybar.progress(pr + 1, text = txt)

with st.spinner('Wait...'):
    time.sleep(5)
st.write('Done!')

st.balloons()
st.snow()
'''

st.error('Something went wrong')
st.warning('Warning')
st.info('Info')
st.success('Successfully completed')
e = RuntimeError('exp')
st.exception(e)

email = st.text_input('Enter email')
if not email:
    st.warning('Enter your email please')
    st.stop()
st.success('Go ahead')

form = st.form('Basic form')
name = form.text_input('Name')
submitted = form.form_submit_button('Submit')
if submitted:
    st.write(name)

st.help(datetime.time)

df1 = pd.DataFrame(
    np.random.randn(10, 2),
    columns = ['1', '2']
)
df2 = pd.DataFrame(
    np.random.randn(10, 2),
    columns= ['1', '2']
)
mytable = st.table(df1)
mychart = st.line_chart(df1)
mychart.add_rows(df2)

for i in range(5):
    time.sleep(1)
    df3 = pd.DataFrame(
        np.random.randn(10, 2),
        columns= ['1', '2']
    )
    mychart.add_rows(df3)
'''
st.session_state
if 'key' in st.session_state:
    del st.session_state['key']

if 'key' not in st.session_state:
    st.session_state['key'] = 1
st.session_state
'''

st.session_state['k1'] = 10
st.session_state['k2'] = 20
st.session_state
for k in st.session_state.keys():
    del st.session_state[k]
st.session_state

st.session_state
st.text_input('Name', key='name')
st.session_state
'''
def form_callback():
    st.write(st.session_state['my_slider'])
    st.write(st.session_state(['my_checkbox']))
with st.form(key = 'my_form'):
    slider_input = st.slider('My_slider', 0, 15, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or no', key='my_checkbox')
    submit_button = st.form_submit_button('Submit', on_click= form_callback())
'''