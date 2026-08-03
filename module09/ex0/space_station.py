from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError

class SpaceStation(BaseModel):
    """
    Data model for a space station.
    Hereda de BaseModel para obtener la validación automática de Pydantic.
    """
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    # is_operational tiene un valor por defecto, así que no es obligatorio pasarlo
    is_operational: bool = Field(default=True)
    # notes es opcional, puede ser None o un string de hasta 200 caracteres
    notes: Optional[str] = Field(default=None, max_length=200)

def main() -> None:
    """
    Main function to demonstrate Pydantic validation.
    """
    print("Space Station Data Validation\n")

    # 1. Creamos una estación con datos perfectos
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: {'Operational' if valid_station.is_operational else 'Down'}\n")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    # 2. Intentamos crear una estación con datos inválidos a propósito
    try:
        print("Expected validation error:")
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Deep Space Station",
            crew_size=30,  # ¡Ojo! Esto rompe la regla de "le=20"
            power_level=100.0,
            oxygen_level=100.0,
            last_maintenance=datetime.now()
        )
        # Esta línea nunca se ejecutará porque Pydantic frena la ejecución arriba
        print(invalid_station.name)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

if __name__ == "__main__":
    main()
