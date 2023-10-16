import streamlit as st
import pandas as pd
from listapoo09B.views import View

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        dic = []
        for c in clientes:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)   

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)

    def atualizar():
        option_atualizar = st.selectbox("Atualização de clientes", (View.lista_de_clientes()))
        if option_atualizar != None:
            nome = st.text_input("Informe o novo nome", value=option_atualizar.get_nome())
            email = st.text_input("Informe o novo e-mail", value=option_atualizar.get_email())
            fone = st.text_input("Informe o novo fone", value=option_atualizar.get_fone())
        if st.button("Atualizar"):
            View.cliente_atualizar(option_atualizar.get_id(), nome, email, fone)
            st.write("Cliente Atualizado")

    def excluir():
        option_excluir = st.selectbox('Exclusão de clientes', (View.lista_de_clientes()))
        if option_excluir != None:
          if st.button("Excluir"):
            View.cliente_excluir(option_excluir)
            st.write("Cliente excluido")
