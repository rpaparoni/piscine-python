from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError

class ContactType(str, Enum):
    """
    Tipos de contacto alienígena permitidos.
    Al heredar de str y Enum, Pydantic entiende que son cadenas de texto.
    """
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
    """
    Modelo de datos para registrar un contacto alienígena.
    """
    # Usamos Field para las reglas básicas de cada dato individual
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        """
        Validaciones personalizadas después de revisar los tipos básicos.
        """
        # 1. El ID debe empezar por "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        
        # 2. El contacto físico debe estar verificado
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        
        # 3. El contacto telepático requiere al menos 3 testigos
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        
        # 4. Señales fuertes (>7.0) deben tener un mensaje
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (>7.0) should include received messages")
        
        # Si todo está perfecto, devolvemos el propio objeto validado
        return self

def main() -> None:
    """
    Función principal para probar nuestro modelo AlienContact.
    """
    print("Alien Contact Log Validation\n")

    # Prueba 1: Creamos un contacto válido
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=5.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'\n")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    # Prueba 2: Creamos un contacto inválido a propósito
    try:
        print("Expected validation error:")
        invalid_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.0,
            duration_minutes=10,
            # ¡Ojo aquí! Le ponemos 2 testigos a un contacto telepático
            witness_count=2,  
            message_received=None,
            is_verified=False
        )
        # Esto no se ejecutará porque Pydantic lo frena antes
        print(invalid_station.name)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

if __name__ == "__main__":
    main()
