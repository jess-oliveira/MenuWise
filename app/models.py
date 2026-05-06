from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database import Base

class Food(Base):
    __tablename__ = 'foods'
    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    food = Column(
        String(100),
        nullable=False,
        index=True
        )
    protein = Column(Float)

    carb = Column(Float)

    fat = Column(Float)

    @property
    def kcal(self):
        return (self.protein * 4) + (self.carb * 4) + (self.fat * 9)
    
    