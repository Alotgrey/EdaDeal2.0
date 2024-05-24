from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    ...

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image_url = Column(String)
    isFinal = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey('categories.id'))
    parent = relationship('Category', remote_side=[id])

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name}, image_url={self.image_url}, isFinal={self.isFinal}, parent_id={self.parent_id})>"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image_url = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    link = Column(String)

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, image_url={self.image_url}, category_id={self.category_id}, link={self.link})>"