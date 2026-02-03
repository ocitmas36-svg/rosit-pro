import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Rosit Pro Finance", page_icon="💰")

if 'saldo' not in st.session_state:
    st.session_state.saldo = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 Login Rosit Pro")
    pin = st.text_input("Masukkan PIN", type="password")
    if st.button("Masuk"):
        if pin == "1234":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("PIN Salah!")
else:
    st.title("💰 Rosit Pro Finance")
    st.subheader(f"Saldo: Rp {st.session_state.saldo:,}")
    
    with st.form("input_transaksi"):
        nom = st.number_input("Nominal (Rp)", min_value=0)
        ket = st.text_input("Keterangan")
        col1, col2 = st.columns(2)
        masuk = col1.form_submit_button("UANG MASUK")
        keluar = col2.form_submit_button("UANG KELUAR")

        if masuk:
            st.session_state.saldo += nom
            st.session_state.logs.append({"Waktu": datetime.now().strftime("%d/%m/%y"), "Tipe": "MASUK", "Jumlah": nom, "Ket": ket})
            st.rerun()
        if keluar:
            st.session_state.saldo -= nom
            st.session_state.logs.append({"Waktu": datetime.now().strftime("%d/%m/%y"), "Tipe": "KELUAR", "Jumlah": nom, "Ket": ket})
            st.rerun()

    st.write("### Riwayat")
    if st.session_state.logs:
        st.table(pd.DataFrame(st.session_state.logs))
