from pydantic import BaseModel, validator, ValidationError

class Patient(BaseModel):
    name:str
    age:int 
    e_mail:str
    
def update_patient_data(patient=Patient):
    print(patient.name)
    print(patient.age)
    print(patient.e_mail)

patient_info={'name': "John Doe", 'age': 30, 'e_mail': "jfn@gmail.com"}
patient1=Patient(**patient_info)
update_patient_data(patient1)