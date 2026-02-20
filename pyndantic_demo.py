from pydantic import BaseModel, Field,EmailStr,AnyUrl
from typing import Annotated, Optional

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="the name of the patient", description="give the name of the patient", example="John Doe")]
    age: Annotated[int, Field(ge=0, le=120, title="the age of the patient", description="give the age of the person")]
    e_mail :EmailStr
    linked_in: AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(description="is the patient married?")]
    allergies: Annotated[Optional[list[str]], Field(description="list of allergies the patient has", example=["pollen", "dust"])]
    contact_details: dict[str, str]

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.e_mail)
    print(patient.linked_in)
    print(patient.married)
    print("upated")

patient_info={'name': "John Doe", 'age': 30, 'e_mail': "abc@gmail.com", 'linked_in': "https://www.linkedin.com/in/johndoe", 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'address': '123 Main St'}}
patient1=Patient(**patient_info)
update_patient_data(patient1)
