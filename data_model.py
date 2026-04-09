from pydantic import BaseModel

class Water(BaseModel):
    ph : float
    hardness : float
    tds : float
    chlorine : float
    sulfate : float
    conductivity : float
    organic_carbon : float
    trihalomethanes : float
    turbidity : float
   