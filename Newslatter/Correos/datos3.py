import boto3
import pandas as pd
import csv

s3 = boto3.resource('s3', aws_access_key_id='AKIAW6MWQJTNASYP3KXT', aws_secret_access_key='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')
filename = "https://suscripcionesnewsletter.s3.amazonaws.com/suscripcionnew.csv"
data = pd.read_csv(filename, header=0)
correos = list(data["correo"])
print(correos)


def dardebaja():
    pass
