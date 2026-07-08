import sys
from pathlib import Path

import streamlit as st
from app.historial import Historial

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


from app.predictor import Predictor


st.title("Sistema de apoyo para detección de anemia")

st.write(
    "Ingrese los parámetros hematológicos del paciente"
)


rbc = st.number_input(
    "RBC",
    min_value=0.0,
    value=4.5
)

hgb = st.number_input(
    "HGB (Hemoglobina)",
    min_value=0.0,
    value=12.0
)

hct = st.number_input(
    "HCT",
    min_value=0.0,
    value=36.0
)

mcv = st.number_input(
    "MCV",
    min_value=0.0,
    value=85.0
)

mch = st.number_input(
    "MCH",
    min_value=0.0,
    value=28.0
)

mchc = st.number_input(
    "MCHC",
    min_value=0.0,
    value=33.0
)


if st.button("Realizar predicción"):

    predictor = Predictor()

    resultado = predictor.predecir(
        rbc,
        hgb,
        hct,
        mcv,
        mch,
        mchc
    )
    historial = Historial()

    historial.guardar(
        rbc,
        hgb,
        hct,
        mcv,
        mch,
        mchc,
        resultado
    )
    


    st.subheader("Resultado")


    if resultado["prediccion"] == 1:
        st.error(resultado["resultado"])
    else:
        st.success(resultado["resultado"])


    st.write(
        f"Probabilidad anemia: "
        f"{resultado['probabilidad_anemia']}%"
    )

    st.write(
        f"Probabilidad no anemia: "
        f"{resultado['probabilidad_no_anemia']}%"
    )