import streamlit as st

import pandas as pd

from database.supabase import supabase

st.title("Funcionários")

menu = st.sidebar.selectbox(

    "Opções",

    [

        "Cadastrar",

        "Consultar"

    ]

)

if menu == "Cadastrar":

    matricula = st.text_input("Matrícula")

    nome = st.text_input("Nome")

    cargo = st.text_input("Cargo")

    equipe = st.selectbox(

        "Equipe",

        [

            "A",

            "B",

            "C",

            "D"

        ]

    )

    telefone = st.text_input("Telefone")

    if st.button("Salvar"):

        supabase.table("funcionarios").insert(

            {

                "matricula":matricula,

                "nome":nome,

                "cargo":cargo,

                "equipe":equipe,

                "telefone":telefone

            }

        ).execute()

        st.success("Funcionário cadastrado.")

if menu == "Consultar":

    dados = supabase.table("funcionarios").select("*").execute()

    df = pd.DataFrame(dados.data)

    st.dataframe(

        df,

        use_container_width=True

    )

    if not df.empty:

        funcionario = st.selectbox(

            "Selecione",

            df["nome"]

        )

        registro = df[df["nome"]==funcionario].iloc[0]

        st.write(registro)

        if st.button("Excluir"):

            supabase.table("funcionarios").delete().eq(

                "id",

                int(registro["id"])

            ).execute()

            st.success("Excluído.")

            st.rerun()