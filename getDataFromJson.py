import pandas as pd

graph_images = pd.read_json('beauty.leg.json', encoding='utf-8')['GraphImages']

edges_list = [image['edge_media_to_caption']['edges'][0]['node']['text'] for image in graph_images if
              image['edge_media_to_caption']['edges'][0]['node']['text'] != '#美腿']

# edges_list = [image for image in graph_images]

print(edges_list)

# print(graph_images[0]['edge_media_to_caption'])
