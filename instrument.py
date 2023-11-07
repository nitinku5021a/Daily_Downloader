from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class Price:
    open: Optional[float] = 0.0
    high: Optional[float] = 0.0
    low: Optional[float] = 0.0
    close: Optional[float] = 0.0

@dataclass
class Instrument:
    instrument_token: int    
    tradingsymbol: str
    name: str
    last_price: float
    exchange_token: Optional[int] = None
    expiry: Optional[date] = None
    strike: Optional[float] = None
    tick_size: Optional[float] = None
    lot_size: Optional[int] = None
    instrument_type: Optional[str] = None
    segment: Optional[str] = None
    exchange: Optional[str] = None
    timestamp: Optional[datetime] = None
    price: Optional[Price] = Price()
    volume: Optional[int] = 0
    oi: Optional[int] = 0

