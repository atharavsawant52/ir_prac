def metrics(retrieved, relevant):

    tp = len(retrieved & relevant)
    fp = len(retrieved - relevant)
    fn = len(relevant - retrieved)

    precision = tp/(tp+fp) if(tp+fp)>0 else 0
    recall = tp/(tp+fn) if(tp+fn)>0 else 0
    f1 = (2*precision*recall)/(precision+recall) if(precision+recall)>0 else 0

    print("True Positive:",tp)
    print("False Positive:",fp)
    print("False Negative:",fn)
    print("Precision:",precision)
    print("Recall:",recall)
    print("F-measure:",f1)

retrieved = {"doc1","doc2","doc3"}
relevant = {"doc1","doc4"}

metrics(retrieved,relevant)

print("performed by 44_Atharav Sawant")