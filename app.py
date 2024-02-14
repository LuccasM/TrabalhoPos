# importing Important Liberaries
import pickle
import streamlit as st
import numpy as np

# Load model
model_diabetes = pickle.load(open('models/model_diabetes.pkl', 'rb'))

# Web Title
st.title('Predição de diabetes')

# Split Columns
col1, col2 = st.columns(2)

with col1 :
  Gestacoes = st.number_input('Informe a quantidade de gestações')

with col2 :
  Glicose = st.number_input('Informe a concentração de glicose')
  
with col1 :
  Pressao = st.number_input('Informe a pressão sanguínea')

with col2 :
  EspessuraPele = st.number_input('Informe a espessura da pele (mm)')

with col1 :
  Insulina = st.number_input('Informe a concentração de insulina')

with col2 :
  IMC = st.number_input('Informe o IMC')

with col1 :
  FuncaoDiabate = st.number_input('Informe a função de pedigree do diabetes')

with col2 :
  Idade = st.number_input('Informe a idade')
  
# Prediction
diabetes_diagnostico = ''

if st.button('Predição'):
  diabetes_predicao = model_diabetes.predict([[Gestacoes,Glicose,Pressao,EspessuraPele,Insulina,IMC,FuncaoDiabate,Idade]])
  
  if(diabetes_predicao[0]==1):
    diabetes_diagnostico = 'O paciente possuí diabetes'
  else :
    diabetes_diagnostico = 'O paciente não possuí diabetes'

st.success(diabetes_diagnostico)