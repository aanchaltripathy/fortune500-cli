import pandas as pd

def write_data(rows, columns, filename, file_format):
    df = pd.DataFrame(rows, columns=[col.title() for col in columns])
    if file_format == 'excel':
        df.to_excel(filename, index=False)
    else:
        df.to_csv(filename, index=False)