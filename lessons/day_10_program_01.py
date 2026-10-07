import numpy as np

daily_token_usage = np.array([120, 250, 180, 320, 210])

print("Token usage:", daily_token_usage)
print("With 10% increase:", daily_token_usage * 1.10)
print("Average:", daily_token_usage.mean())
print("Maximum:", daily_token_usage.max())
print("Minimum:", daily_token_usage.min())