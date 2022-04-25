from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []


def person_is_seller(person):
    return person[0] == "p"


def search_seller(graph, root):
    searched = []
    search_queue = deque()
    search_queue += graph[root]
    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                return person
            else:
                search_queue += graph[person]
                searched.append(person)


assert search_seller(graph, "you") == "peggy"
