import pandas as pd

dataset_file = "/home/dw/Downloads/Daraj_articles_v1.csv"
fname = "Daraj_articles_v1"

data = pd.read_csv(dataset_file)
data.sort_values(by=['text'], ascending=True, inplace=True)
data['id'] = range(1, len(data) + 1)
data['id'] = data['id'].apply(lambda x: f'{fname}_'+ str(x) )

data[["text", "id"]].to_csv("/home/dw/Dokumente/Codes/potato/project-hub/debiasing_news_articles_ar/data/Daraj_articles_v1.tsv", sep='\t')