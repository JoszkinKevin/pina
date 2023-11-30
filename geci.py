import streamlit as st
import pandas as pd

tabla = {
  "fiuk":[1,2,3,4]
  "lanyok":[1,2,3,4,5]
}
bum = pd.DataFrame(tabla)

st.write(bum)
