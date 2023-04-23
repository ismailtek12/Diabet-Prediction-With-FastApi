from pydantic import BaseModel
class Data(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int
    yas_araligi_genç:int
    yas_araligi_genç_yaşlı:int
    yas_araligi_yaşlı:int
    BMI_araligi_kilolu:int
    BMI_araligi_normal:int
    BMI_araligi_obez:int
    BMI_araligi_zayıf:int
    INSULIN_araligi_anormal:int
    INSULIN_araligi_normal:int