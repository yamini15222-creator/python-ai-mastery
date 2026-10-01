import numpy as np
import pandas as pd
import pydantic
import sklearn

numbers = np.array([10, 20, 30])

print("Python AI environment is ready.")
print(f"Average: {numbers.mean()}")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
print(f"Pydantic: {pydantic.__version__}")