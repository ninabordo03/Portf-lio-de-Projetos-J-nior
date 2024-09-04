import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

st.header('Oi')
st.text('Salve o Tricolor Paulista')
st.subheader('Nunca fui rebaixado')
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

palm = {'mundiais': 0,
        'mundiais falsificados': ['1 (Copa Rio Internacional - 1951)'],
        'rebaixamentos': ['2 (2002, 2012)'],
        'quase rebaixamentos': ['1 (só não caiu porque o Prass segurou)']}
df = pd.DataFrame(palm)
st.write(df)
st.write('Probabilidade do Palmeiras ganhar o campeonato mundial: 0%')

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