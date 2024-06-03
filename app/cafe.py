from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name')} You are not vaccinated"
            )
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"{visitor.get('name')} need to put on a mask"
            )
        return f"Welcome to {self.name}"
