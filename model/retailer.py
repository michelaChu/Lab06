from dataclasses import dataclass

@dataclass
class Retailer:
    retailer_code: int
    retailer_name: str
    type: str
    country: str