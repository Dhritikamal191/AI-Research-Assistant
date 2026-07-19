class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String(100),
        unique=True
    )

    email = Column(
        String(150),
        unique=True
    )

    password = Column(
        String(255)
    )