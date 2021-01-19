from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("DS")
sc = SparkContext(conf=conf)

startCharacterID = 5306
targetCharacterID = 14

hitCounter = sc.accumulator(0)


def converToBFS(line):
    fields = line.split()
    fields = line.split()
    heroID = int(fields[0])
    connections = []
    for connection in fields[1:]:
        connections.append(int(connection))

    color = "WHITE"
    distance = 9999

    if heroID == startCharacterID:
        color = "GRAY"
        distance = 0

    return heroID, (connections, distance, color)


def createStartingRdd():
    inputFile = sc.textFile("file:///marvel-graph.txt")
    return inputFile.map(converToBFS)  # iteration each line of graph -- output: list


def bfsMap(node):    # iterationRdd = createStartingRdd() # mapped = iterationRdd.flatMap(bfsMap)
    characterID = node[0]
    data = node[1]
    connections = data[0]
    distance = data[1]
    color = data[2]

    results = []

    if color == "GRAY":
        for connection in connections:
            newCharacterID = connection
            newDistance = distance + 1
            newColor = 'GRAY'
            if targetCharacterID == connection:
                hitCounter.add(1)

            newEntry = (newCharacterID, ([], newDistance, newColor))
            results.append(newEntry)

        color = 'BLACK'

    results.append((characterID, (connections, distance, color)))
    return results


def bfsReduce(data1, data2):  # characterID,(connections1,distance,color),
                              #             (connection2,distance,color)

    edges1 = data1[0]
    edges2 = data2[0]
    distance1 = data1[1]
    distance2 = data2[1]
    color1 = data1[2]
    color2 = data2[2]

    distance = 9999
    color = color1
    edges = []

    if len(edges1) > 0:
        edges.extend(edges1)
    if len(edges2) > 0:
        edges.extend(edges2)

    if distance1 < distance:  # replace the min distance
        distance = distance1
    if distance2 < distance:
        distance = distance2

    if color1 == "WHITE" and color2 == "GRAY" or "BLACK":
        color = color2









