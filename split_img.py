import numpy as np

def image_split_column(img:np.ndarray)->list:
    '''
    Function description: 
    Splite the image by column. Calculate the number of elements with a value of 255 in each column.
    When the number of 255 changes from zero to non-zero, it indicates the beginning of the digits area. Use startList to record the starting column index.
    When the number of 255 changes from non-zero to zero, it indicates the end of the digits area. Use endList to recorder the end column index.
    Use flag to represent the current state, outside or inside the digits area.
    
    parameters 
        img: input image to be splited by column.
        return: output image after splited by column. It is a list and its elements are np.ndarray.
    '''
    
    # find out the number of columns in the original image
    # create a list to record the number of elements with a value of 255 in each column
    column = img.shape[1]
    columnHist = np.zeros(column)
    
    # count the number of elements with a value of 255 in each column and record it in columnHist
    for i in range(column):
        columnHist[i] = np.sum(img[:,i]==255,dtype=np.uint8)
    
    # initialize the variables
    flag = 0
    startList = []
    endList = []
    columnHistLength = len(columnHist)
    
    # find out the start column and the end column by detect the change in rowHist
    for i in range(0,columnHistLength):
        if flag == 0 and columnHist[i]!=0:
            startList.append(i)
            flag = 1
            continue
        if flag == 1 and columnHist[i]==0:
            endList.append(i)
            flag = 0
            continue
        continue

    if len(startList)!=len(endList):
        l = min(len(startList),len(endList))
        startList = startList[0:l]
        endList = endList[0:l]
    
    # following the startList and the endList, split the digits area from the original image.
    # there maybe several areas.
    imgList = []
    for i in range(0,len(startList)):
        temp = img[:,startList[i]-8:endList[i]+8]
        imgList.append(temp)
    return imgList

def image_split_row(img:np.ndarray)->list:
    '''
    Function description: 
    Splite the image by row. Calculate the number of elements with a value of 255 in each row.
    When the number of 255 changes from zero to non-zero, it indicates the beginning of the digits area. Use startList to record the starting row index.
    When the number of 255 changes from non-zero to zero, it indicates the end of the digits area. Use endList to recorder the end row index.
    Use flag to represent the current state, outside or inside the digits area.
    
    parameters 
        img: input image to be splited by row.
        return: output image after splited by row. It is a list and its elements are np.ndarray.
    '''
    
    # find out the number of rows in the original image
    # create a list to record the number of elements with a value of 255 in each row
    row = img.shape[0]
    rowHist = np.zeros(row)
    
    # count the number of elements with a value of 255 in each row and record it in rowHist
    for i in range(row):
        rowHist[i] = np.sum(img[i,:]==255)
    
    # initialize the variables
    flag = 0
    startList = []
    endList = []
    rowHistLength = len(rowHist)
    
    # your work here
    # find out the start row and the end row by detect the change in rowHist
    # you may need a loop structure
    ##################
    # Your code here #
    for i in range(0,rowHistLength):
        if flag == 0 and rowHist[i]!=0:
            startList.append(i)
            flag = 1
            continue
        if flag == 1 and rowHist[i]==0:
            endList.append(i)
            flag = 0
            continue
        continue

    ##################

    if len(startList)!=len(endList):
        l = min(len(startList),len(endList))
        startList = startList[0:l]
        endList = endList[0:l]
    
    # following the startList and the endList, split the digits area from the original image.
    # there maybe several areas.
    imgList = []   
    for i in range(0,len(startList)):
        temp = img[startList[i]-8:endList[i]+8,:]
        imgList.append(temp)
    return imgList
