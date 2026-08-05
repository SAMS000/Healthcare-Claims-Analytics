from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class HCPCSCode(Base):
    __tablename__ = "hcpcs_codes"

    hcpcs_code: Mapped[str] = mapped_column(
        String(10),
        primary_key=True
    )

    description: Mapped[str] = mapped_column()

    drug_indicator: Mapped[bool] = mapped_column(Boolean)