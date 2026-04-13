import pandas as pd
from app.model import train_model

# Fake training data
data = pd.DataFrame({
    "failed_attempts": [1,2,3,10,12,1,2,15],
    "unique_users": [1,1,2,5,6,1,2,7]
})

train_model(data)