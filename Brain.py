import math
import json

class Brain:

    model = []
    
    def normalizePoints(positions):

        if not positions:
            return []

        maxX = max(points[0] for points in positions)
        maxY = max(points[1] for points in positions)
        minX = min(points[0] for points in positions)
        minY = min(points[1] for points in positions)

        rangeX = maxX - minX
        rangeY = maxY - minY

        if rangeX == 0:
            rangeX = 1

        if rangeY == 0:
            rangeY = 1

        for points in positions:
            
            # Shifting the points to the origin
            points[0] -= minX
            points[1] -= minY

            # Scaling the Points
            points[0]/= rangeX
            points[1]/= rangeY

        
        return positions
    
    def genNormalMatrix(normal_positions):
        matrix = []
        res = 12

        for i in range(res):
            row = []

            for j in range(res):
                row.append("0")
            
            matrix.append(row)


        for point in normal_positions:
            x = int(point[0] * res)
            y = int(point[1] * res)

            if x >= res:
                x = res - 1
            if y >= res:
                y = res - 1
            matrix[y][x] = "1"
            #matrix[y][x] +=
        
        #print(normal_positions)
            
        #print(matrix) 

        return matrix
        
    def flattenMatrix(matrix):
        flatVector = []

        for row in matrix:
            for cell in row:
                flatVector.append(cell)

        for i in range(len(flatVector)):
            flatVector[i] = int(flatVector[i])

        return (flatVector)

    #Method to visualize the matrix in console
    def visualizeMatrix(matrix):
        visualization = ""
        for row in matrix:
            visualization += " ".join(str(cell) for cell in row) + "\n"

        print(visualization)
    
    def manhattanDistance(vector1, vector2):
        total_diff = math.inf

        for i in range(len(vector1)):
            total_diff += abs(vector1[i] - vector2[i])

        print(total_diff)
        return total_diff

    def predictObject(predict_vector):
        match = None
        current_min_dist = math.inf

        print(predict_vector)

        for label, input_vector in Brain.model:
            print(input_vector)
            
            prediction_diff = Brain.manhattanDistance(input_vector, predict_vector)
            if prediction_diff < current_min_dist:
                current_min_dist = prediction_diff
                match = label

        print(match)

    def packBrainModel(file_path):
        with open(file_path, "r") as file:
            raw_model = json.load(file)
            Brain.model = [(label, vector) for label, vector in raw_model.items()]


