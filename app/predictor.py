from pathlib import Path
import joblib
import pandas as pd


class Predictor:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parent.parent

        ruta_modelo = BASE_DIR / "modelo" / "modelo_basico.pkl"

        if not ruta_modelo.exists():
            raise FileNotFoundError(
                f"No se encontró el modelo: {ruta_modelo}"
            )

        self.modelo = joblib.load(ruta_modelo)

    def predecir(
        self,
        rbc,
        hgb,
        hct,
        mcv,
        mch,
        mchc
    ):

        paciente = pd.DataFrame([{

            "RBC": rbc,
            "HGB": hgb,
            "HCT": hct,
            "MCV": mcv,
            "MCH": mch,
            "MCHC": mchc

        }])

        pred = self.modelo.predict(paciente)[0]

        prob = self.modelo.predict_proba(paciente)[0]

        resultado = "ANEMIA" if pred == 1 else "NO ANEMIA"

        return {

            "resultado": resultado,

            "prediccion": int(pred),

            "probabilidad_anemia": round(float(prob[1]) * 100, 2),

            "probabilidad_no_anemia": round(float(prob[0]) * 100, 2)

        }