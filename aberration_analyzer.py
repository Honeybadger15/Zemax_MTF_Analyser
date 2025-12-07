import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("MTF_Biconvex_data",sep= "\s+",header = None,names =["frequency","saggital","tangential"])

