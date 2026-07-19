from src.rag_pipeline import rag_query

question = "What is customer segmentation?"

result = rag_query(question)

print("\nAnswer\n")
print(result["answer"])

print("\nSources\n")

for source in result["sources"]:

    print(source)