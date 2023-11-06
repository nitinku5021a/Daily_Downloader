from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Instrument:
    instrument_token: int
    exchange_token: int
    tradingsymbol: str
    name: str
    last_price: float
    expiry: date
    strike: float
    tick_size: float
    lot_size: int
    instrument_type: str
    segment: str
    exchange: str