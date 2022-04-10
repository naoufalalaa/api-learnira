from pydantic import BaseModel

class ResponseModel(BaseModel):
    content: str
    correct: bool

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