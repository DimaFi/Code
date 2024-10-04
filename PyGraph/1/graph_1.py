class Graph:
    def __init__(self, directed=False, weighted=True):
        self.list_sm = {}  # Список смежности
        self.directed = directed  # Ориентированный граф или нет
        self.weighted = weighted  # Взвешенный граф или нет

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


def user_interface():
    print("Хотите загрузить граф из файла? (1 - Да, 0 - Нет): ", end="")
    load_from_file = bool(int(input()))

    if load_from_file:
        file_name = input("Введите имя файла: ")
        directed = bool(int(input("Граф ориентированный? (1 - Да, 0 - Нет): ")))
        weighted = bool(int(input("Граф взвешенный? (1 - Да, 0 - Нет): ")))
        graph = Graph.from_file(file_name, directed, weighted)
        print(f"Граф загружен из файла {file_name}.")
    else:
        directed = bool(int(input("Граф ориентированный? (1 - Да, 0 - Нет): ")))
        weighted = bool(int(input("Граф взвешенный? (1 - Да, 0 - Нет): ")))
        graph = Graph(directed, weighted)

    while True:
        print("\n1. Добавить вершину")
        print("2. Добавить ребро")
        print("3. Удалить вершину")
        print("4. Удалить ребро")
        print("5. Показать список смежности")
        print("6. Показать изолированные вершины")
        print("7. Сохранить граф в файл")
        print("8. Выйти")
        print("Выберите действие: ", end="")
        choice = int(input())

        if choice == 1:
            vertex = int(input("Введите вершину: "))
            graph.add_vertex(vertex)
        elif choice == 2:
            u = int(input("Введите начальную вершину: "))
            v = int(input("Введите конечную вершину: "))
            if graph.weighted:
                weight = float(input("Введите вес ребра (по умолчанию 1): ") or 1)
                graph.add_edge(u, v, weight)
            else:
                graph.add_edge(u, v)
        elif choice == 3:
            vertex = int(input("Введите вершину для удаления: "))
            graph.remove_vertex(vertex)
        elif choice == 4:
            u = int(input("Введите начальную вершину: "))
            v = int(input("Введите конечную вершину: "))
            graph.remove_edge(u, v)
        elif choice == 5:
            graph.display()
        elif choice == 6:
            graph.find_isolated_vertices()
        elif choice == 7:
            file_name = input("Введите имя файла: ")
            graph.to_file(file_name)
        elif choice == 8:
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    user_interface()
