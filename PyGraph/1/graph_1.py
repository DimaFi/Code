from collections import deque

class Graph:
    def __init__(self, directed=False, weighted=True):
        self.list_sm = {}  # Список смежности
        self.directed = directed  # Ориентированный граф или нет
        self.weighted = weighted  # Взвешенный граф или нет
        
    # метод для вычисления полустепени захода
    def outdegree(self, vertex):
        if not self.directed:
            print("Полустепень это привилегия ориентированных)")
            return None
        
        outdegree_count = 0
        for u in self.list_sm:
            for edge in self.list_sm[u]:
                if edge[0] == vertex:  # проверка, есть ли ребро, ведущее в vertex
                    outdegree_count += 1
        return outdegree_count
    
    # метод для вычисления кол-ва одинаковых соседних ребер
    def find_common_neighbor(self, vertex1, vertex2):
        if vertex1 not in self.list_sm or vertex2 not in self.list_sm:
            print(f"Одна или обе вершины {vertex1} и {vertex2} не найдены в графе.")
            return None

        # соседи
        neighbors1 = {neighbor[0] for neighbor in self.list_sm[vertex1] if neighbor[0] != vertex1}
        neighbors2 = {neighbor[0] for neighbor in self.list_sm[vertex2] if neighbor[0] != vertex2}

        # пересечения
        common_neighbors = neighbors1.intersection(neighbors2)

        if common_neighbors:
            print(f"Общие соседи для вершин {vertex1} и {vertex2}: {', '.join(map(str, common_neighbors))}")
            return common_neighbors
        else:
            print(f"У вершин {vertex1} и {vertex2} нет общих соседей.")
            return None
    
    @classmethod
    def from_file(cls, file_name, directed=False, weighted=True):
        graph = cls(directed, weighted)
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    u, v, weight = int(parts[0]), int(parts[1]), float(parts[2])
                    graph.add_edge(u, v, weight)
                elif len(parts) == 2:
                    u, v = int(parts[0]), int(parts[1])
                    graph.add_edge(u, v)
        return graph
    

    @classmethod
    def copy(cls, other):
        graph_copy = cls(other.directed, other.weighted)
        graph_copy.list_sm = {v: neighbors.copy() for v, neighbors in other.list_sm.items()}
        return graph_copy

    def add_vertex(self, vertex):
        if vertex not in self.list_sm:
            self.list_sm[vertex] = []
        else:
            print(f"Вершина {vertex} уже существует.")

    def add_edge(self, u, v, weight=1):

        if u not in self.list_sm:
            self.add_vertex(u)
        if v not in self.list_sm:
            self.add_vertex(v)

        if self.weighted:
            edge_data = (v, weight)
        else:
            edge_data = (v,)

        # Добавляем ребро один раз для ориентированных графов или если u == v (петля)
        self.list_sm[u].append(edge_data)
        if not self.directed and u != v:
            self.list_sm[v].append((u, weight) if self.weighted else (u,))

    def remove_vertex(self, vertex):
        if vertex in self.list_sm:
            del self.list_sm[vertex]
            for neighbors in self.list_sm.values():
                for i in range(len(neighbors) - 1, -1, -1):
                    if neighbors[i][0] == vertex:
                        neighbors.pop(i)
        else:
            print(f"Вершина {vertex} не найдена.")

    def remove_edge(self, u, v):

        removed = False
        if u in self.list_sm:
            for i in range(len(self.list_sm[u]) - 1, -1, -1):
                if self.list_sm[u][i][0] == v:
                    self.list_sm[u].pop(i)
                    removed = True
                    break

        if not self.directed and v in self.list_sm:
            for i in range(len(self.list_sm[v]) - 1, -1, -1):
                if self.list_sm[v][i][0] == u:
                    self.list_sm[v].pop(i)
                    removed = True
                    break

        if removed:
            print(f"Ребро {u} -> {v} удалено.")
        else:
            print(f"Ребро {u} -> {v} не существует.")

    def to_file(self, file_name):
        with open(file_name, 'w') as file:
            for u in self.list_sm:
                if not self.list_sm[u]:
                    file.write(f"{u}\n")  # изолированная
                for v in self.list_sm[u]:
                    if self.weighted:
                        file.write(f"{u} {v[0]} {v[1]}\n")
                    else:
                        file.write(f"{u} {v[0]}\n")

    def display(self):
        for vertex, neighbors in self.list_sm.items():
            if not neighbors:
                print(f"{vertex}: (изолированная вершина)")
            else:
                if self.weighted:
                    print(f"{vertex}: {', '.join([f'{neighbor} (вес: {weight})' for neighbor, weight in neighbors])}")
                else:
                    print(f"{vertex}: {', '.join([str(neighbor) for neighbor in neighbors])}")

    def get_edge_list(self):
        edge_list = []
        for u in self.list_sm:
            for v in self.list_sm[u]:
                if self.directed or (v[0], u, v[1]) not in edge_list:
                    if self.weighted:
                        edge_list.append((u, v[0], v[1]))
                    else:
                        edge_list.append((u, v[0]))
        return edge_list

    def find_isolated_vertices(self):
        
        isolated = [v for v, neighbors in self.list_sm.items() if not neighbors]
        if isolated:
            print(f"Изолированные вершины: {', '.join(map(str, isolated))}")
        else:
            print("Изолированных вершин нет.")


    def symmetric_difference(graph1, graph2):
        if graph1.directed != graph2.directed or graph1.weighted != graph2.weighted:
            print("Графы должны быть одинакового типа")
            return None
        
        # новый граф
        result_graph = Graph(graph1.directed, graph1.weighted)
        
        # Добавляем рёбра из graph1, если их нет в graph2
        for u, edges in graph1.list_sm.items():
            for v in edges:
                edge = (v[0], v[1]) if graph1.weighted else (v[0],)
                if u not in graph2.list_sm or edge not in graph2.list_sm.get(u, []):
                    result_graph.add_edge(u, *edge)
        
        # Добавляем рёбра из graph2, если их нет в graph1
        for u, edges in graph2.list_sm.items():
            for v in edges:
                edge = (v[0], v[1]) if graph2.weighted else (v[0],)
                if u not in graph1.list_sm or edge not in graph1.list_sm.get(u, []):
                    result_graph.add_edge(u, *edge)

        return result_graph
    
    
    #region Ацикличность, Обходы (первая задача 17)
    def acyclies(self):
        if not self.directed:
            print("Этот метод работает только для ориентированных графов.")
            return None

        visited = set()
        recursion_stack = set() # мн-во текущих вершин

        def dfs(vertex):
            if vertex in recursion_stack:  # цикл есть
                return False
            if vertex in visited:
                return True
            
            visited.add(vertex)
            recursion_stack.add(vertex)

            for neighbor in self.list_sm.get(vertex, []):
                if not dfs(neighbor[0]):  # обходим соседей
                    return False
            
            recursion_stack.remove(vertex)
            return True

        for vertex in self.list_sm: # проходимся п овсем вершинам
            if vertex not in visited:
                if not dfs(vertex):  # Если цикл найден, граф не ацикличный
                    print("Граф содержит цикл.")
                    return False
        
        print("Граф ацикличен.")
        return True
    
    #endregion

    #region Обходы 6 задание 2 (37)
    
    def bfs_shortest_distances(self, start_vertex):
        distances = {v: float('inf') for v in self.list_sm}
        distances[start_vertex] = 0
        queue = deque([start_vertex])
        
        # пройдемся по всем вершинам начиная с заданной, BFS
        while queue:
            current = queue.popleft()
            for neighbor, _ in self.list_sm[current]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        return distances

    def radius_and_center(self):
        if not self.list_sm:
            print("Граф пуст.")
            return None, None

        # найдем эксцентриситеты
        eccentricities = {}
        for vertex in self.list_sm:
            distances = self.bfs_shortest_distances(vertex)
            eccentricities[vertex] = max(distances.values())

        # найдем радиус графа
        radius = min(eccentricities.values())

        # найдем центр графа
        center = [v for v, ecc in eccentricities.items() if ecc == radius]

        return radius, center
    
    #endregion
    
    #region Kruskal 7
    def kruskal_minimum_spanning_tree(self):
        if not self.weighted:
            print("Граф должен быть взвешенным для работы алгоритма Краскала.")
            return None
        
        edges = self.get_edge_list()
        # сортируем рёбра по весу
        edges.sort(key=lambda x: x[2])

        # Для хранения остовного дерева
        mst = []
        # Для проверки ацикличности используем структуру "система непересекающихся множеств" (Union-Find)
        parent = {}
        rank = {}

        # проверка Union-Find
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v]) # если V не корень, то рекурсивно поднимаемся по дереву пока не найдем корень
            return parent[v]

        def union(v1, v2):
            root1 = find(v1)
            root2 = find(v2)
            if root1 != root2:
                # Соединяем деревья с учётом ранга
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        for vertex in self.list_sm: # изначально все вершины равны и ранг 0, каждая вершина множество
            parent[vertex] = vertex
            rank[vertex] = 0

        # Основной цикл алгоритма Краскала
        for u, v, weight in edges:
            # если новое ребро не создаёт цикл, то добавляем его в остовное дерево
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))
                if len(mst) == len(self.list_sm) - 1:
                    break
        return mst
    #endregion
    
    #region 8
    # Метод для поиска кратчайших путей из одной вершины (алгоритм Дейкстры)
    def dijkstra(self, start):
        if not self.weighted:
            print("Алгоритм Дейкстры применим только для взвешенных графов.")
            return None

        distances = {v: float('inf') for v in self.list_sm} # мин расстояние до каждой вершины
        distances[start] = 0
        previous = {v: None for v in self.list_sm} # предшествующая вершина для восстановления пути
        visited = set()

        while len(visited) < len(self.list_sm):
            # надо найти вершину с минимальным расстоянием
            current = min((v for v in distances if v not in visited), key=lambda v: distances[v], default=None)
            if current is None or distances[current] == float('inf'):
                break

            visited.add(current)
            for neighbor, weight in self.list_sm.get(current, []): # проходимся по всем соседям текущей вершины
                if neighbor not in visited and distances[current] + weight < distances[neighbor]: # если можно улучшить расстояние через текущую вершину
                    distances[neighbor] = distances[current] + weight
                    previous[neighbor] = current

        return distances, previous
    #endregion
    

    #region 9
    # Метод для поиска кратчайших путей для всех пар вершин (алгоритм Флойда-Уоршелла)
    def floyd_warshall(self):
        vertices = list(self.list_sm.keys())
        n = len(vertices)
        dist = {v: {u: float('inf') for u in vertices} for v in vertices}
        next_hop = {v: {u: None for u in vertices} for v in vertices}

        for v in vertices:
            dist[v][v] = 0

        for u in self.list_sm:
            for v, weight in self.list_sm[u]:
                dist[u][v] = weight
                next_hop[u][v] = v

        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_hop[i][j] = next_hop[i][k]

        return dist, next_hop
    #endregion
    
    
    #region 10
    # Метод для поиска цикла отрицательного веса (алгоритм Беллмана-Форда)
    def find_negative_cycle(self):
        distances = {v: float('inf') for v in self.list_sm}
        previous = {v: None for v in self.list_sm}

        vertices = list(self.list_sm.keys())
        if not vertices:
            print("Граф пуст.")
            return None

        # Выбираем первую вершину для старта
        start = vertices[0]
        distances[start] = 0

        for _ in range(len(vertices) - 1):
            for u in self.list_sm:
                for v, weight in self.list_sm[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        previous[v] = u

        # Проверяем на наличие цикла отрицательного веса
        for u in self.list_sm:
            for v, weight in self.list_sm[u]:
                if distances[u] + weight < distances[v]:
                    cycle = []
                    current = v
                    for _ in range(len(vertices)):
                        current = previous[current]
                    cycle_vertex = current

                    while True:
                        cycle.append(cycle_vertex)
                        cycle_vertex = previous[cycle_vertex]
                        if cycle_vertex == current:
                            break

                    cycle.append(current)
                    cycle.reverse()
                    print("Найден цикл отрицательного веса:", cycle)
                    return cycle

        print("Циклов отрицательного веса нет.")
        return None
    #endregion


#region interf
def user_interface():
    graphs = []  # Список графов
    current_graph = None  # Индекс текущего графа
    
    while True:
        print("\nМеню работы с графами")    
        print("1. Создать новый граф")
        print("2. Загрузить граф из файла")
        print("3. Показать список смежности текущего графа")
        print("4. Построить симметрическую разность двух графов")
        print("5. Сохранить текущий граф в файл")
        print("6. Добавить вершину в текущий граф")
        print("7. Добавить ребро в текущий граф")
        print("8. Удалить вершину из текущего графа")
        print("9. Удалить ребро из текущего графа")
        print("10. Найти изолированные вершины в текущем графе")
        print("11. Вычислить полустепень захода вершины в текущем графе")
        print("12. Найти общих соседей для двух вершин в текущем графе")
        print("13. Переключиться на другой граф")
        print("14. Проверить, является ли граф ацикличным")
        print("15. Найти радиус графа и его центр")
        print("16. Расстояние до других вершин")
        print("17. Минимальный остовный каркас")
        print("18. Найти кратчайшие пути из u1 и u2 до v")
        print("19. Найти кратчайшие пути для всех пар вершин")
        print("20. Найти цикл отрицательного веса, если он есть")
        print("21. Выйти")
        
        choice = int(input("Выберите действие: "))
        
        if choice == 1:
            directed = bool(int(input("Граф ориентированный? (1 - Да, 0 - Нет): ")))
            weighted = bool(int(input("Граф взвешенный? (1 - Да, 0 - Нет): ")))
            graph = Graph(directed, weighted)
            graphs.append(graph)
            current_graph = len(graphs) - 1
            print(f"Создан новый граф с индексом {current_graph}. Текущий граф: {current_graph}")
        
        elif choice == 2:
            file_name = input("Введите имя файла: ")
            directed = bool(int(input("Граф ориентированный? (1 - Да, 0 - Нет): ")))
            weighted = bool(int(input("Граф взвешенный? (1 - Да, 0 - Нет): ")))
            graph = Graph.from_file(file_name, directed, weighted)
            graphs.append(graph)
            current_graph = len(graphs) - 1
            print(f"Граф загружен из файла {file_name} с индексом {current_graph}. Текущий граф: {current_graph}")

        elif current_graph is None:
            print("Пожалуйста, создайте или загрузите граф сначала.")
        
        elif choice == 3:
            graphs[current_graph].display()
        
        elif choice == 4:
            index1 = int(input("Введите индекс первого графа: "))
            index2 = int(input("Введите индекс второго графа: "))
            if 0 <= index1 < len(graphs) and 0 <= index2 < len(graphs):
                new_graph = Graph.symmetric_difference(graphs[index1], graphs[index2])
                if new_graph:
                    graphs.append(new_graph)
                    print(f"Симметрическая разность графов добавлена как новый граф с индексом {len(graphs) - 1}.")
            else:
                print("Неверные индексы графов.")
        
        elif choice == 5:
            file_name = input("Введите имя файла: ")
            graphs[current_graph].to_file(file_name)
            print(f"Граф с индексом {current_graph} сохранён в файл {file_name}.")

        elif choice == 6:
            vertex = int(input("Введите вершину: "))
            graphs[current_graph].add_vertex(vertex)
        
        elif choice == 7:
            u = int(input("Введите начальную вершину: "))
            v = int(input("Введите конечную вершину: "))
            if graphs[current_graph].weighted:
                weight = float(input("Введите вес ребра (по умолчанию 1): ") or 1)
                graphs[current_graph].add_edge(u, v, weight)
            else:
                graphs[current_graph].add_edge(u, v)
        
        elif choice == 8:
            vertex = int(input("Введите вершину для удаления: "))
            graphs[current_graph].remove_vertex(vertex)
        
        elif choice == 9:
            u = int(input("Введите начальную вершину: "))
            v = int(input("Введите конечную вершину: "))
            graphs[current_graph].remove_edge(u, v)
        
        elif choice == 10:
            graphs[current_graph].find_isolated_vertices()
        
        elif choice == 11:
            vertex = int(input("Введите вершину для вычисления полустепени захода: "))
            in_deg = graphs[current_graph].outdegree(vertex)
            if in_deg is not None:
                print(f"Полустепень захода вершины {vertex}: {in_deg}")
        
        elif choice == 12:
            vertex1 = int(input("Введите первую вершину: "))
            vertex2 = int(input("Введите вторую вершину: "))
            graphs[current_graph].find_common_neighbor(vertex1, vertex2)
        
        elif choice == 13:
            print("Доступные графы:")
            for i, graph in enumerate(graphs):
                print(f"{i}: Граф {'ориентированный' if graph.directed else 'неориентированный'}, {'взвешенный' if graph.weighted else 'невзвешенный'}")
            new_index = int(input("Введите индекс графа для переключения: "))
            if 0 <= new_index < len(graphs):
                current_graph = new_index
                print(f"Текущий граф переключен на индекс {current_graph}.")
            else:
                print("Неверный индекс графа.")
                
        elif choice == 14:
            graphs[current_graph].acyclies()
        
        elif choice == 15:
            radius, center = graphs[current_graph].radius_and_center()
            if radius is not None:
                print(f"Радиус графа: {radius}")
                print(f"Центр графа: {', '.join(map(str, center))}")
            else:
                print("Граф пуст или некорректен.")

            
        elif choice == 16:
            distance 
            
        elif choice == 17:
            if graphs[current_graph].weighted:
                mst = graphs[current_graph].kruskal_minimum_spanning_tree()
                if mst:
                    print("Минимальный остовный каркас:")
                    for u, v, weight in mst:
                        print(f"{u} - {v} (вес: {weight})")
            else:
                print("Для построения минимального остовного каркаса граф должен быть взвешенным.")
                
        elif choice == 18:
            u1 = int(input("Введите первую вершину (u1): "))
            u2 = int(input("Введите вторую вершину (u2): "))
            v = int(input("Введите конечную вершину (v): "))
            for u in (u1, u2):
                distances, _ = graphs[current_graph].dijkstra(u)
                print(f"Кратчайший путь из {u} до {v}: {distances.get(v, 'нет пути')}")

        elif choice == 19:
            dist, _ = graphs[current_graph].floyd_warshall()
            print("Кратчайшие расстояния между всеми парами вершин:")
            for u in dist:
                for v in dist[u]:
                    print(f"{u} -> {v}: {dist[u][v]}")

        elif choice == 20:
            graphs[current_graph].find_negative_cycle()
            
        elif choice == 21:
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":  
    user_interface()

#endregion