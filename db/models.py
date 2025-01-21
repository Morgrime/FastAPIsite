from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class UserBase(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    surname: Mapped[str] = mapped_column(String(40))
    login: Mapped[str] = mapped_column(String(40))
    password: Mapped[str] = mapped_column(String(40)) # изменить на хэшированный пароль


class IdeaBase(Base):
    __tablename__ = 'ideas'

    id: Mapped[int] = mapped_column(primary_key=True)
    idea: Mapped[str] = mapped_column(String(200))) # не больше 200 символов
    description: Mapped[str] = mapped_column(String(400)) # не больше 400 символов
    # likes dislikes?

