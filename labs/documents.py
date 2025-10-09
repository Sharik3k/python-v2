from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Report(Document):
    def render(self) -> str:
        return "=== Звіт ===\nДані аналітики, статистика, висновки."


class Invoice(Document):
    def render(self) -> str:
        return "=== Рахунок ===\nСписок товарів, суми, підсумок до оплати."


class Contract(Document):
    def render(self) -> str:
        return "=== Контракт ===\nУмови угоди, зобов'язання сторін, підписи."

class NullDocument(Document):
    def render(self) -> str:
        return "Помилка: невідомий тип документа."


class DocumentFactory:
    @staticmethod
    def create(doc_type: str) -> Document:
        doc_type = doc_type.lower()
        match doc_type:
            case "report":
                return Report()
            case "invoice":
                return Invoice()
            case "contract":
                return Contract()
            case _:
                return NullDocument()



if __name__ == "__main__":
    for doc_type in ["report", "invoice", "contract", "unknown"]:
        document = DocumentFactory.create(doc_type)
        print(document.render())
        print("-" * 40)
