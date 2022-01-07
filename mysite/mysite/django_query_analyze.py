from timeit import default_timer as timer
from django.db import connection, reset_queries

def django_query_analyze(func):
    """decorator to perform analysis on Django queries"""

    def wrapper(*args, **kwargs):

        avs = []
        query_counts = []
        for _ in range(20):
            reset_queries()
            start = timer()
            func(*args, **kwargs)
            end = timer()
            avs.append(end - start)
            query_counts.append(len(connection.queries))
            reset_queries()

        print(" ")
        print("ran function {name}".format(name=func.__name__))
        print("-------------------------")
        print("number of queries: {queries}".format(queries=int(sum(query_counts) / len(query_counts))))
        print("Time of execution: {execution}s".format(execution=float(format(min(avs), '.5f'))))
        print(" ")
        return func(*args, **kwargs)

    return wrapper