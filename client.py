
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
API_KEY = '79b79993b58f4f75baeda249c92811b4'
ENDPOINT = 'https://jash-text-analysis1.cognitiveservices.azure.com/'

def conn():
   try:
        client = TextAnalyticsClient(
            endpoint=ENDPOINT,
            credential=AzureKeyCredential(API_KEY)
        )
        return client
   except Exception as e:
        print(e)
        return






