import uvicorn
from fastapi import FastAPI
import numpy as np
from base_data import Data
import joblib
import pickle

app=FastAPI(title="ML App")
my_model=pickle.load(open("model_and_data/fixed_lgbm_model_pkl","rb"))
#columns=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","yas_araligi_genç","yas_araligi_genç-yaşlı","BMI_araligi_obez"]
@app.get("/")
def home():
    return "API is working as expected"



@app.post("/predict")
def predict(data:Data):
    data=dict(data)
    print(data)
    print("Hello")
    preg=data["Pregnancies"]
    print(preg)
    glucose=data["Glucose"]
    bp=data["BloodPressure"]
    skinTh=data["SkinThickness"]
    insülin=data["Insulin"]
    bmi=data["BMI"]
    dpf=data["DiabetesPedigreeFunction"]
    age=data["Age"]
    genc=data["yas_araligi_genç"]
    genc_yasli=data["yas_araligi_genç_yaşlı"]
    yasli=data["yas_araligi_yaşlı"]
    kilolu=data["BMI_araligi_kilolu"]
    normal=data["BMI_araligi_normal"]
    obez=data["BMI_araligi_obez"]
    zayif=data["BMI_araligi_zayıf"]
    insülin_anorm=data["INSULIN_araligi_anormal"]
    insülin_norm=data["INSULIN_araligi_normal"]





    #return my_model.predict([[preg,glucose,bp,skinTh,insülin,bmi,dpf,age,genc,genc_yasli,yasli,kilolu,normal,obez,zayif,insülin_anorm,insülin_norm]])
    print(my_model.predict([[preg,glucose,bp,skinTh,insülin,bmi,dpf,age,genc,genc_yasli,yasli,kilolu,normal,obez,zayif,insülin_anorm,insülin_norm]]))
    print("Hello")
    prediction=my_model.predict([[preg,glucose,bp,skinTh,insülin,bmi,dpf,age,genc,genc_yasli,yasli,kilolu,normal,obez,zayif,insülin_anorm,insülin_norm]])
    if(prediction[0]==1):
        prediction="Diabetes"
    else:
        prediction="Not Diabetes"
    return {
        "prediction":prediction
    }



if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)