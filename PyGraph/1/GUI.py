import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx
from graph_1 import Graph

class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph GUI")
        self.graph = None
        self.graphs = []

        self.create_menu()
        self.create_buttons()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Загрузить граф из файла", command=self.load_graph)
        file_menu.add_command(label="Сохранить граф", command=self.save_graph)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.master.quit)

    def create_buttons(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=10)

        tk.Button(frame, text="Создать граф", command=self.create_graph).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Добавить вершину", command=self.add_vertex).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Добавить ребро", command=self.add_edge).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Загрузить граф", command=self.load_graph).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Выбрать граф", command=self.choose_graph).grid(row=0, column=4, padx=5)
        tk.Button(frame, text="Показать граф", command=self.visualize_graph).grid(row=0, column=5, padx=5)


    def create_graph(self):
        directed = messagebox.askyesno("Граф", "Граф ориентированный?")
        weighted = messagebox.askyesno("Граф", "Граф взвешенный?")
        graph = Graph(directed=directed, weighted=weighted)
        self.graphs.append(graph)
        self.graph = graph
        messagebox.showinfo("Успех", f"Новый граф создан! (Индекс: {len(self.graphs) - 1})")


    def add_vertex(self):
        if not self.graph:
            messagebox.showerror("Ошибка", "Сначала создайте граф!")
            return

        vertex = tk.simpledialog.askinteger("Добавить вершину", "Введите номер вершины:")
        if vertex is not None:
            self.graph.add_vertex(vertex)
            messagebox.showinfo("Успех", f"Вершина {vertex} добавлена.")

    def add_edge(self):
        if not self.graph:
            messagebox.showerror("Ошибка", "Сначала создайте граф!")
            return

        u = tk.simpledialog.askinteger("Добавить ребро", "Введите начальную вершину:")
        v = tk.simpledialog.askinteger("Добавить ребро", "Введите конечную вершину:")
        weight = 1
        if self.graph.weighted:
            weight = tk.simpledialog.askfloat("Добавить ребро", "Введите вес ребра (по умолчанию 1):", initialvalue=1)

        if u is not None and v is not None:
            self.graph.add_edge(u, v, weight)
            messagebox.showinfo("Успех", f"Ребро {u} -> {v} добавлено с весом {weight}.")

    def load_graph(self):
        file_path = filedialog.askopenfilename(title="Выберите файл с графом")
        if file_path:
            directed = messagebox.askyesno("Граф", "Граф ориентированный?")
            weighted = messagebox.askyesno("Граф", "Граф взвешенный?")
            graph = Graph.from_file(file_path, directed, weighted)
            self.graphs.append(graph)
            self.graph = graph
            messagebox.showinfo("Успех", f"Граф загружен из файла! (Индекс: {len(self.graphs) - 1})")
            
    def save_graph(self):
        if not self.graph:
            messagebox.showerror("Ошибка", "Сначала создайте или загрузите граф!")
            return

        file_path = filedialog.asksaveasfilename(title="Сохранить граф", defaultextension=".txt")
        if file_path:
            self.graph.to_file(file_path)
            messagebox.showinfo("Успех", "Граф сохранён в файл.")

    def visualize_graph(self):
        if not self.graph:
            messagebox.showerror("Ошибка", "Сначала создайте или загрузите граф!")
            return

        nx_graph = nx.DiGraph() if self.graph.directed else nx.Graph()
        for u, edges in self.graph.list_sm.items():
            for edge in edges:
                if self.graph.weighted:
                    nx_graph.add_edge(u, edge[0], weight=edge[1])
                else:
                    nx_graph.add_edge(u, edge[0])

        pos = nx.spring_layout(nx_graph)
        plt.figure(figsize=(8, 6))
        nx.draw(nx_graph, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
        if self.graph.weighted:
            labels = nx.get_edge_attributes(nx_graph, "weight")
            nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=labels)
        plt.title("Граф")
        plt.show()
        
    def choose_graph(self):
        if not hasattr(self, "graphs") or not self.graphs:
            messagebox.showerror("Ошибка", "Сначала создайте или загрузите граф!")
            return

        def set_current_graph(index):
            self.graph = self.graphs[index]
            messagebox.showinfo("Успех", f"Выбран граф с индексом {index}.")
            top.destroy()

        top = tk.Toplevel(self.master)
        top.title("Выберите граф")
        top.geometry("300x300")
    
        for i, graph in enumerate(self.graphs):
                graph_info = f"Граф {i + 1}: {'Ориентированный' if graph.directed else 'Неориентированный'}, {'Взвешенный' if graph.weighted else 'Невзвешенный'}"
                tk.Button(top, text=graph_info, command=lambda idx=i: set_current_graph(idx)).pack(fill=tk.X, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()
