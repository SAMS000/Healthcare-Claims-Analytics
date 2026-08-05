from sqlalchemy import Boolean, BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Provider(Base):
    __tablename__ = "providers"

    npi: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    last_org_name: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str | None] = mapped_column(String(100))
    middle_initial: Mapped[str | None] = mapped_column(String(1))
    credentials: Mapped[str | None] = mapped_column(String(50))

    entity_code: Mapped[str] = mapped_column(String(1))

    address_line1: Mapped[str] = mapped_column(String(255))
    address_line2: Mapped[str | None] = mapped_column(String(255))

    city: Mapped[str] = mapped_column(String(100))
    state: Mapped[str] = mapped_column(String(2))
    zip_code: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(50))

    provider_type: Mapped[str] = mapped_column(String(150))

    medicare_participating: Mapped[bool] = mapped_column(Boolean)