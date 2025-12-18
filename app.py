import streamlit as st
import numpy as np

st.title("Twiddle Matrix Calculator")

st.write("This app calculates the inverse of a square matrix")

n = st.number_input("Matrix size n x n", min_value=1, max_value=6, value=2, step=1)

matrix = []
for i in range(n):
    cols = st.columns(n)
    row = []
    for j in range(n):
        val = cols[j].number_input(
            f"a{i+1}{j+1}",
            value=0.0,
            key=f"{i}-{j}"
        )
        row.append(val)
    matrix.append(row)

A = np.array(matrix)

if st.button("Calculate Twiddle Matrix"):
    try:
        A_inv = np.linalg.inv(A)
        st.subheader("Twiddle Matrix Result")
        st.write(A_inv)
    except np.linalg.LinAlgError:
        st.error("Matrix is singular, inverse does not exist")
