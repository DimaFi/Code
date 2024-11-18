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
    
    
    # Ацикличность, Обходы (первая задача 17)
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

        
    #Обходы 6 задание 2 (37)
    
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
        print("17. Выйти")
        
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
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    user_interface()
