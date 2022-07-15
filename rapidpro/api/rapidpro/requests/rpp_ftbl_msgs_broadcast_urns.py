import json

import pandas as pd
import numpy as np

class BroadcastUrls:
    def __init__(self, session):
        self._session = session

    def get_broadcast_urls(self, **kwargs):

        params = {**kwargs}
        request = "broadcasts.json"

        responses = self._session.get(request, params=params)

        r_n = [pd.json_normalize(response, sep="_") for response in responses]
        df = pd.concat(r_n)
        if df.shape[0]==0:
            print("No new data fetched from API")
            print("Exiting the pipeline run.")
            exit(0)
        Na = np.nan
        if df.shape[0] >0:
            df['contacts']=df['contacts'].apply(lambda x:x[0]['uuid'] if x!='' else x)
            df['text_eng'] = df['text_eng'].apply(lambda x: str(x).encode('utf-8')[0:256].decode('utf-8'))
        df["broadcast_id"], df["contacturn_id"] = Na, Na
        return df