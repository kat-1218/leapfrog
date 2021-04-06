## This code lets you input a network of your choice then 
## work out if you can get from one node to another in a given
## number of leaps. There is also the option of displaying
## a labelled graph of the network 

import networkx as nx
import matplotlib.pyplot as plt

## Create functions

def create_graph(stops_list, edges_list):
     G=nx.Graph()
     G.add_nodes_from(stops_list)
     G.add_edges_from(edges_list)
     return G

def destination_within_n_leaps(G, leaps, start_node, end_node):
    shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
    n_nodes = len(shortest_path)
    n_edges = n_nodes -1
    if n_edges <= leaps:
        print("Journey can be completed in your lunch break!")
    else:
        print("That journey is too far")
    return shortest_path

def plot_graph(G, shortest_path, boolean):
    if boolean == True:
        sp = []
        for i in range(0,len(shortest_path)-1):
            sp.append((shortest_path[i],shortest_path[i+1]))
        nx.draw(G, with_labels=True)
        plt.show()
    elif boolean == False:
        pass
      
## Run code to work out leaps

if __name__ == "__main__":


    ## Create node/stops list and the edge list for your desired network
    stops_list = ["Home","Oliver's Perfect Cakes","Doris's Handmade Stir Fry","Isla's Favorite Snack Bar", 
                "Dorothy's Inspired Doughnuts","Florence's Glorious Diner", "William's Nutritious Pizzeria",
                "Matthew's Sublime Pies","James's Tantalizing Bakery","Charlotte's Rad Soups"]

    edges_list =[("Oliver's Perfect Cakes", "Doris's Handmade Stir Fry"),
                ("Isla's Favorite Snack Bar", "Oliver's Perfect Cakes"),
                ("Isla's Favorite Snack Bar", "Dorothy's Inspired Doughnuts"),
                ("Florence's Glorious Diner", "William's Nutritious Pizzeria"),
                ("Matthew's Sublime Pies", "James's Tantalizing Bakery"),
                ("William's Nutritious Pizzeria", "Isla's Favorite Snack Bar"),
                ("Home", "Matthew's Sublime Pies"),
                ("James's Tantalizing Bakery", "Home"),
                ("William's Nutritious Pizzeria", "Home"),
                ("Doris's Handmade Stir Fry", "Dorothy's Inspired Doughnuts"),
                ("Doris's Handmade Stir Fry", "Oliver's Perfect Cakes"),
                ("Charlotte's Rad Soups", "Florence's Glorious Diner"),
                ("Dorothy's Inspired Doughnuts", "Charlotte's Rad Soups")]
    

    ## Populate the empty graph with the nodes and edges between them
    G = create_graph(stops_list, edges_list)

    ## Run route checker, with number of leaps, start node and end node as parameters
    shortest_path = destination_within_n_leaps(G, 3, "Home", "Doris's Handmade Stir Fry")

    ## Optional: plot graph, True plots graph, False means it is not plotted
    plot_graph(G, shortest_path, True)     