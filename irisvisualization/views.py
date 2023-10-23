import seaborn as sns
from django.shortcuts import render
import pandas as pd
from io import BytesIO
import base64

# Create your views here.
def visualization(request):
    dataset_path = "/home/gachara/PycharmProjects/djangoProject7/Iris.csv"
    dataset = pd.read_csv(dataset_path)
    dataset = dataset.drop('Id',axis=1)
    pair = sns.pairplot(dataset,hue="Species")
    image = BytesIO()
    pair.savefig(image,format='png')
    image.seek(0)
    plot_url = base64.b64encode(image.getvalue()).decode()
    return render(request,'home.html',{"pairplot":plot_url})
