def describe_temperature(temperature: float) -> str:
    if temperature < 0 or temperature > 2:
        return "Invalid temperature. Use a value from 0 to 2."

    if temperature <= 0.3:
        return "Focused output"
    elif temperature <= 1.0:
        return "Balanced output"
    else:
        return "Creative output"


for value in [0, 0.2, 0.7, 1.5, 2.5]:
    print(f"{value}: {describe_temperature(value)}")