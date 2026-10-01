class AIModel:
    def __init__(self, name: str, temperature: float) -> None:
        self.name = name
        self.temperature = temperature

    def describe(self) -> str:
        return (
            f"Model: {self.name}, "
            f"temperature: {self.temperature}"
        )


model = AIModel("gpt-5", 0.7)

print(model.name)
print(model.describe())