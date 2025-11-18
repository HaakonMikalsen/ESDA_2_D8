import numpy as np

def findClosestIndex(data, point):
    data = np.array(data)
    for index, value in enumerate(data[:-1]):  
        if (value <= point <= data[index+1]) or (value >= point >= data[index+1]):
            return index
    return 0  

def findValueInterpolate(data, point, selectData):
    data = np.array(data)
    selectData = np.array(selectData)
    index = findClosestIndex(data, point)
    
    
    a = (selectData[index+1] - selectData[index]) / (data[index+1] - data[index])
    
    y0 = selectData[index]
    x0 = data[index]
    
    
    return y0 + a * (point - x0)


if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [0, 2, 4, 6, 8]
    point = 2.5

    print(findValueInterpolate(x, point, y))
    if findValueInterpolate(x, point, y)==5:
        print("test passed")
    else:
        print("test failed")
