class Contact:
    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
#convert object to string
    def __str__(self) -> str:
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}" 
    
    def to_dict(self) -> dict:
        return{
            "name": self.name,
            "phone": self.phone,
            "email": self.email

        }
    @staticmethod
    def from_dict(data: dict) -> "Contact":
        return Contact(data["name"], data["phone"], data["email"])
    
