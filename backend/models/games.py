from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        Float,
                        Boolean,
                        )

from .base import Base


class TypePrice(Base):
    __tablename__ = 'type_price'
    name = Column(String, unique=True)


class Game(Base):
    __tablename__ = 'game'
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    price_type = Column(Integer, ForeignKey("type_price.id"))
    quantity = Column(Integer, default=0)
    is_active = Column(Boolean, default=False)

    def deactivate_at_zero(self):
        if self.quantity == 0 or self.price == 0:
            self.is_active = False
        if self.quantity > 0 and self.price > 0:
            self.is_active = True
        return
