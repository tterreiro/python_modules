#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    """Enumeration of authorized space crew ranks."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Pydantic model representing vital statistics of a crew member."""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Pydantic model representing vital statistics of a space mission."""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    duration_days: int = Field(ge=1, le=3650)
    launch_date: datetime
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation_rules(self) -> "SpaceMission":
        experienced = 0
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with 'M'.")
        if not any(member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
                   for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain.")
        for mate in self.crew:
            if mate.years_experience >= 5:
                experienced += 1
            if not mate.is_active:
                raise ValueError("All crew members must be active.")
        if self.duration_days > 365 and experienced < (len(self.crew) / 2):
            raise ValueError(
                "Long missions (> 365 days)"
                "need 50% experienced crew (5+ years).")
        return self


def main() -> None:
    """Execute validation demonstration for space mission crew management."""
    print("Space Mission Crew Validation")
    print("========================================")

    try:
        member1 = CrewMember(
            member_id="C001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=15
        )
        member2 = CrewMember(
            member_id="C002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=8
        )
        member3 = CrewMember(
            member_id="C003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=4
        )

        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[member1, member2, member3],
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
        for m in valid_mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Unexpected error validating proper data: {e}")

    print("\n========================================")
    print("Expected validation error:")

    try:
        invalid_member = CrewMember(
            member_id="C004",
            name="Bob Cadet",
            rank=Rank.CADET,
            age=20,
            specialization="Training",
            years_experience=0
        )

        SpaceMission(
            mission_id="M2026_TEST",
            mission_name="Unled Training Flight",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=[invalid_member],
            budget_millions=50.0
        )
    except ValidationError as e:
        for error in e.errors():
            msg = error.get('msg', '')
            if msg.startswith("Value error, "):
                print(msg[13:])
            else:
                print(msg)


if __name__ == "__main__":
    main()
