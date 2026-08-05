from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class PlaceOfService(Base):
    __tablename__ = "place_of_service"

    place_of_service_code: Mapped[str] = mapped_column(
        String(1),
        primary_key=True
    )

    description: Mapped[str] = mapped_column(String(100))