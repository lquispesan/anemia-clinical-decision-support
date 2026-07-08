from app.predictor import Predictor

predictor = Predictor()

resultado = predictor.predecir(

    rbc=3.80,
    hgb=8.7,
    hct=28.4,
    mcv=74,
    mch=22,
    mchc=30

)

print(resultado)