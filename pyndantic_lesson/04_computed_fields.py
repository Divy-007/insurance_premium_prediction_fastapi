from pydantic import BaseModel,computed_field
from typing import Annotated, Optional,List,Dict

class patient(BaseModel):
    name:str
    age:int
    height:float
    weight:float

    @computed_field
    @property
    def bmi(self)->float:
        bmi=self.weight/(self.height/100)**2
        return round(bmi,2)
    
def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print("patient.bmi:", patient.bmi)

patient_info={'name': "John Doe", 'age': 30, 'height': 175.0, 'weight': 70.5}
patient1=patient(**patient_info)
update_patient_data(patient1)



