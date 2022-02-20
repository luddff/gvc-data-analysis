import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib


data = pd.read_csv('data/test_data.csv', delimiter = ";")
G = nx.from_pandas_edgelist(data, source='Source',
                            target='Target',
                            edge_attr = ('weight', 'color')
                            )

widths = nx.get_edge_attributes(G, 'weight')

data['color'] = pd.Categorical(data['color'])
data['color'].cat.codes

cmap = matplotlib.colors.ListedColormap(['tab:blue', '#7FFFD4',
                                         'powderblue', 'skyblue',
                                         'lightsteelblue'
                                         , 'cornflowerblue'])

# G = nx.balanced_tree(3, 5)


pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", args="")

plt.figure(figsize=(25, 25))

nx.draw_networkx_labels(G, pos, font_size=10,
                        horizontalalignment = 'center',
                        font_color='black')

nx.draw(G, pos, alpha=0.8,
        node_color=data['color'].cat.codes,
        cmap=cmap,
        edge_color='gray', node_size=13000,
        arrows=True, width=list(widths.values()),
        font_family='Times New Roman',
        font_weight='bold',
        arrowstyle='-|>'
        )



plt.axis("equal")

hfont = {'fontname':'Times New Roman'}
plt.title('Översikt av utmattningssyndrom', fontsize=20,
          **hfont)

plt.show()


