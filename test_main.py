from fastapi.testclient import TestClient
from main import app
from fastapi import status
from main import predict

client=TestClient(app=app)

def test_predict_positive():
    payload = {
        "Pregnancies": 6,
        "Glucose": 148,
        "BloodPressure": 72,
        "SkinThickness": 35,
        "Insulin": 0,
        "BMI": 33.6,
        "DiabetesPedigreeFunction": 0.627,
        "Age": 50,
        "yas_araligi_genç":1,
        "yas_araligi_genç_yaşlı":0,
        "yas_araligi_yaşlı":0,
        "BMI_araligi_kilolu":0,
        "BMI_araligi_normal":0,
        "BMI_araligi_obez":1,
        "BMI_araligi_zayıf":0,
        "INSULIN_araligi_anormal":1,
        "INSULIN_araligi_normal":0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] == "Diabetes"

def test_predict_negative():
    payload = {
        "Pregnancies": 1,
        "Glucose": 85,
        "BloodPressure": 66,
        "SkinThickness": 29,
        "Insulin": 0,
        "BMI": 26.6,
        "DiabetesPedigreeFunction": 0.351,
        "Age": 31,
        "yas_araligi_genç":0,
        "yas_araligi_genç_yaşlı":1,
        "yas_araligi_yaşlı":0,
        "BMI_araligi_kilolu":0,
        "BMI_araligi_normal":1,
        "BMI_araligi_obez":0,
        "BMI_araligi_zayıf":0,
        "INSULIN_araligi_anormal":0,
        "INSULIN_araligi_normal":1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] == "Not Diabetes"

def test_predict_invalid_payload():
    payload = {
        "pregnancies": 6,
        "glucose": 148,
        "blood_pressure": 72,
        "skin_thickness": 35,
        "insulin": 0,
        "bmi": 33.6,
        "diabetes_pedigree_function": "invalid",
        "age": 50
    }
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert "detail" in response.json()


    
