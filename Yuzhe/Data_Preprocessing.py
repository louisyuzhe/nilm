import glob
import pandas as pd

def join_multiple_channels():
    path = r'../dataset/'  # Path to dataset
    allFiles = glob.glob(path + "/*.dat")  # Data file name
    i = 0  # Counter for appliances array

    # Initialize the frame with timestamp (TS) as Index column
    frame1 = pd.DataFrame()
    # frame1.set_index('TS')

    # Loop to load dataset into a single frame
    for file_ in allFiles:
        start = time.time()
        # df = pd.read_csv(file_,delimiter = ' ' ,index_col=0, squeeze=True, header="None")
        df = pd.read_csv(file_, delimiter=' ', names=['TS', file_[34:43]], header=None)  # appliances[i]])
        print("Reading", i, " passed")
        frame1 = frame1.join(df.set_index('TS'), how='outer')
        print("Joining", i, " passed")

        end = time.time()
        print("Time used: ", end - start)

        i = i + 1

    # df.set_index('TS')
    print(frame1)

def get_appliance():
    path = r'../dataset/'  # Path to dataset
    allFiles = glob.glob(path + "/*.dat")  # Data file name
    i = 0  # Counter for appliances array

    # Initialize the frame with timestamp (TS) as Index column
    frame1 = pd.DataFrame()
    # frame1.set_index('TS')

    # Loop to load dataset into a single frame
    for file_ in allFiles:
        start = time.time()
        # df = pd.read_csv(file_,delimiter = ' ' ,index_col=0, squeeze=True, header="None")
        df = pd.read_csv(file_, delimiter=' ', names=['TS', file_[34:43]], header=None)  # appliances[i]])
        print("Reading", i, " passed")
        frame1 = frame1.join(df.set_index('TS'), how='outer')
        print("Joining", i, " passed")

        end = time.time()
        print("Time used: ", end - start)

        i = i + 1

    # df.set_index('TS')
    print(frame1)