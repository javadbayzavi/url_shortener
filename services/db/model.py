from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass


class Url(Base):
    __tablename__ = "url"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    long_url: Mapped[str] = mapped_column(String, unique=True, index=True)
    short_url: Mapped[str] = mapped_column(String, unique=True, index=True)
