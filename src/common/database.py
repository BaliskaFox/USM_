from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class UserTable(Base):
    __tablename__ = 'users_accounts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True,nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    
    roles = relationship('RoleTable', secondary='user_roles', back_populates='users_accounts')
    
class RoleTable(Base):
    __tablename__ = "roles"
    
    admin: Mapped[bool] = mapped_column(default=False)
    user: Mapped[bool] = mapped_column(default=True)
    author: Mapped[bool] = mapped_column(default=False)
    
    users = relationship('UserTable', secondary='users_roles', back_populates='roles')
    
class UserRoleTable(Base):
    __tablename__ = 'users_roles'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'), primary_key=True)
    