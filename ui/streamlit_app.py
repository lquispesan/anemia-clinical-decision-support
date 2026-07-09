import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import streamlit as st
from app.historial import Historial

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


from app.predictor import Predictor
from app.historial import Historial


st.title("Sistema de apoyo para detección de anemia")

st.write(
    "Ingrese los parámetros hematológicos del paciente"
)


rbc = st.number_input(
    "RBC (Recuento de Eritrocitos)",
    min_value=0.0,
    value=4.5
)

hgb = st.number_input(
    "HGB (Hemoglobina)",
    min_value=0.0,
    value=12.0
)

hct = st.number_input(
    "HCT (Hematocrito)",
    min_value=0.0,
    value=36.0
)

mcv = st.number_input(
    "MCV (Volumen Corpuscular medio)",
    min_value=0.0,
    value=85.0
)

mch = st.number_input(
    "MCH (Hemoglobina Corpuscular Media)",
    min_value=0.0,
    value=28.0
)

mchc = st.number_input(
    "MCHC (Concentracion de Hemoglobina Corpuscular)",
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
    st.divider()

    st.subheader("Historial de predicciones")

    historial = Historial()

    df = historial.leer()

    if not df.empty:
        st.dataframe(df)
    else:
        st.info("No existen predicciones registradas.")