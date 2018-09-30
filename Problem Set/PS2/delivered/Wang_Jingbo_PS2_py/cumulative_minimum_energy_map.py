import numpy as np

def cumulative_minimum_energy_map(energyImage, seamDirection):
    map = np.zeros(energyImage.shape)

    # if horizontal, rotate and treat as vertical,
    if (seamDirection == "HORIZONTAL"):
        energyImage = np.rot90(energyImage, 3)
        map = np.rot90(map, 3)

    # vertical energy map
    map[0] = energyImage[0].copy()
    for i in range(1, len(map)):
        for j in range(len(map[i])):
            row = i - 1
            colLeft = j - 1
            colCenter = j
            colRight = j + 1
            if (colLeft >= 0 and colRight < len(map[i])):
                map[i][j] = min(map[row][colLeft], map[row][colCenter], map[row][colRight]) + energyImage[i][j]
            elif (colLeft < 0 and colRight < len(map[i])):
                map[i][j] = min(map[row][colCenter], map[row][colRight]) + energyImage[i][j]
            elif (colRight >= len(map[i]) and colLeft >= 0):
                map[i][j] = min(map[row][colLeft], map[row][colCenter]) + energyImage[i][j]
            else:
                map[i][j] = min(map[row][colCenter]) + energyImage[i][j]

    # if horizontal, rotate energy map back
    if (seamDirection == "HORIZONTAL"):
        map = np.rot90(map)

    return map.astype(np.double)