from pydantic import BaseModel, validator, ValidationError,model_validator
from typing import Annotated,Dict
class Patient(BaseModel):
    name:str
    age:int
    contact_details: Dict[str,str]

    @model_validator(mode="after")
    def validate_emg_contact(self):
        if self.age>60 and 'Emergency' not in self.contact_details:
            raise ValueError("the patient age is over 60 but not have emergrncy contact ")
        return self
    
def update_patient_data(patient=Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)

patient_info={'name':"Divy",'age':90 ,'contact_details':{'phone':'23828','Emergency': '9876543210'}}
ptient1=Patient(**patient_info)
update_patient_data(ptient1)