import pandas as pd
import numpy
import re

email_condition = "^[a-z 0-9]*[/.]?[a-z]*[@][a-z 0-9]*[/.][a-z]*[/.]?[a-z]*$"
# defining function for data wrangling 
def wrangle(file):
    df = pd.read_csv(file)
    df["EMAIL_ADDR"] = df["EMAIL_ADDR"].str.lower()
    valid_email = []
    
    #iterate through data and matching with email pattern 
    for string_data in df["EMAIL_ADDR"]:
        if re.match(email_condition, string_data):
            valid_email.append(string_data)
    
    df_final =  df[df["EMAIL_ADDR"].isin(valid_email)]
    return df_final

df = wrangle("email_dataset.csv")
df.to_csv("clean_email_dataset.csv")