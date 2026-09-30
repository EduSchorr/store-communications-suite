from dataclasses import dataclass

@dataclass(frozen=True)
class Recipient:
    store_code: str
    store_name: str
    email: str
    region: str = ""

@dataclass(frozen=True)
class DispatchResult:
    recipient: str
    subject: str
    status: str
    details: str = ""
