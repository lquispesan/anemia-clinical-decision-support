from pathlib import Path
import pandas as pd
from datetime import datetime


class Historial:

    def __init__(self):

        self.ruta = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "historial"
            / "predicciones.csv"
        )

        self.ruta.parent.mkdir(parents=True, exist_ok=True)

    def guardar(
        self,
        rbc,
        hgb,
        hct,
        mcv,
        mch,
        mchc,
        resultado
    ):

        fila = {

            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "RBC": rbc,
            "HGB": hgb,
            "HCT": hct,
            "MCV": mcv,
            "MCH": mch,
            "MCHC": mchc,

            "resultado": resultado["resultado"],

            "prediccion": resultado["prediccion"],

            "probabilidad_anemia":
                resultado["probabilidad_anemia"],

            "probabilidad_no_anemia":
                resultado["probabilidad_no_anemia"]

        }

        if self.ruta.exists():

            df = pd.read_csv(self.ruta)

        else:

            df = pd.DataFrame()

        df = pd.concat(
            [df, pd.DataFrame([fila])],
            ignore_index=True
        )

        df.to_csv(
            self.ruta,
            index=False
        )

    def leer(self):

        if not self.ruta.exists():

            return pd.DataFrame()

        return pd.read_csv(self.ruta)