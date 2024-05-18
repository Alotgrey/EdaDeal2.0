from db.base import Base
from sqlalchemy import JSON, Column, Integer, Sequence, String


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    name = Column(String)
    url = Column(String)
    img_urls = Column(JSON)
    category = Column(String)
