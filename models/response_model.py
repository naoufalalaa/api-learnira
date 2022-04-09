from pydantic import BaseModel

class ResponseModel(BaseModel):
    content: str
    correct: bool

    def __init__(self, content, correct):
        self.content = content
        self.correct = correct
    
    def serial(self):
        return {
            "content": self.content,
            "correct": self.correct
        }


def responseModelSerial(response) -> dict:
    return {
        "id": str(response["_id"]),
        "content": response["content"],
        "correct": response["correct"]
    }

def responsesModelSerial(responses) -> list:
    return [responseModelSerial(response) for response in responses]