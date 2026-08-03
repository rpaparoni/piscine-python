from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator   # type: ignore
from pydantic import ValidationError  # type: ignore


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)

    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)

    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':

        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            astronaut.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for astronaut in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = 0

            for astronaut in self.crew:
                if astronaut.years_experience >= 5:
                    experienced_count += 1
            if (experienced_count / len(self.crew)) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)"
                )

        if not all(astronaut.is_active for astronaut in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation\n")

    commander = CrewMember(
        member_id="C001", name="Sarah Connor", rank=Rank.COMMANDER,
        age=45, specialization="Mission Command", years_experience=15
    )
    rookie = CrewMember(
        member_id="R002", name="John Smith", rank=Rank.LIEUTENANT,
        age=25, specialization="Navigation", years_experience=2
    )
    officer = CrewMember(
        member_id="O003", name="Alice Johnson", rank=Rank.OFFICER,
        age=30, specialization="Engineering", years_experience=6
    )

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[commander, rookie, officer],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"| {member.specialization}")
        print("\n" + "-"*40 + "\n")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    try:
        print("Expected validation error:")
        invalid_mission = SpaceMission(
            mission_id="M_FAIL_01",
            mission_name="Rookie Mistake",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=[rookie, officer],
            budget_millions=50.0
        )
        print(invalid_mission.name)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
