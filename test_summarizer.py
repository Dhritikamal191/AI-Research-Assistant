from src.summarizer import summarize_document

text = """

Customer Segmentation is the process of
grouping customers into similar categories
using KMeans clustering.

"""

print(summarize_document(text,"Executive"))