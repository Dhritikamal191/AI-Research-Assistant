from src.compare_docs import compare_documents

docs = {

    "Paper1.pdf": """

Customer segmentation using
KMeans clustering.

""",

    "Paper2.pdf": """

Customer segmentation using
DBSCAN clustering.

"""

}

print(compare_documents(docs))