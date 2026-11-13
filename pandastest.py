import pandas as pd
data = {
    "producto": ["manzana", "banana", "naranja", "pera"],
    "precio": [0.5, 0.3, 0.7, 0.4],
}
df = pd.DataFrame(data)
print(df["precio"].mean())