import numpy as np

def pagerank(graph, d=0.85, iters=10):
    n = len(graph)
    rank = np.ones(n) / n

    for _ in range(iters):
        new_rank = np.ones(n) * (1-d)/n
        
        for i in range(n):
            for j in graph[i]:
                new_rank[j] += d * rank[i] / len(graph[i])
        
        rank = new_rank

    return rank


# Example Web Graph
web_graph = [
[1,2],   # Page0 -> Page1, Page2
[0,2],   # Page1 -> Page0, Page2
[0,1],   # Page2 -> Page0, Page1
[1,2]    # Page3 -> Page1, Page2
]

result = pagerank(web_graph)

for i,r in enumerate(result):
    print(f"Page {i}: {r:.4f}")

print("performed by 44_Atharav Sawant")