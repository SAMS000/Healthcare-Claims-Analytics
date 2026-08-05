from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Numeric,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class ProviderServiceStatistics(Base):
    __tablename__ = "provider_service_statistics"

    __table_args__ = (
        UniqueConstraint(
            "provider_npi",
            "hcpcs_code",
            "place_of_service_code",
            name="uq_provider_service",
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    provider_npi: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("providers.npi"),
    )

    hcpcs_code: Mapped[str] = mapped_column(
        ForeignKey("hcpcs_codes.hcpcs_code"),
    )

    place_of_service_code: Mapped[str] = mapped_column(
        ForeignKey("place_of_service.place_of_service_code"),
    )

    total_beneficiaries: Mapped[int] = mapped_column()

    total_services: Mapped[float] = mapped_column(Numeric(12, 2))

    total_bene_day_services: Mapped[int] = mapped_column()

    avg_submitted_charge: Mapped[float] = mapped_column(Numeric(12, 2))

    avg_allowed_amount: Mapped[float] = mapped_column(Numeric(12, 2))

    avg_payment_amount: Mapped[float] = mapped_column(Numeric(12, 2))

    avg_standardized_amount: Mapped[float] = mapped_column(Numeric(12, 2))