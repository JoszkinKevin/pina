import streamlit as st
import pandas as pd

tabla = {
  "fiuk":[1,2,3,4],
  "lanyok":[input(),2,3,4]
}
bum = pd.DataFrame(tabla)

st.write(bum)
