# Open treestructure.txt and read the contents into a table, it is a csv file
# that is space delimeted and has a header row
import csv
import os
import sys
import graphviz as gv


# Open the file and read the contents into a table
def read_file(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_ALL)
        # put rows from csv into a table
        table = [row for row in reader]
    return table


# Create a graph from the table
def create_graph(table):
    # Create a new graph
    G = gv.Digraph()

    print(table)
    # Add the nodes to the graph
    for row in table[1:]:
        print(row[0])
        G.node(row[0])

    # Add the edges to the graph\
    for row in table:
        print(row[0])
        G.edge(row[0], row[2])

    return G


# Read the file, create the graph, and render the graph.


def main():
    if len(sys.argv) < 2:
        print("Usage: python graphviz_test.py <filename>")
        sys.exit(1)
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        print("File not found: " + file_name)
        sys.exit(1)
    table = read_file(file_name)
    G = create_graph(table)
    G.render(file_name, view=True)


if __name__ == "__main__":
    main()
