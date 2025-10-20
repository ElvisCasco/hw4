
# a. Load the data
def data_loader(file_name: str) -> pd.DataFrame:
    import pandas as pd
    data = pd.read_csv(file_name)
    print(f"Data loaded successfully. Shape: {data.shape}")
    return data
