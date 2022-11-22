import matplotlib.pyplot as plt 
import base64
from io import BytesIO
import csv, sys, re, random, os, time
import numpy as np


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y):
    #put your code here
    plt.switch_backend('AGG')
    # plt.figure(figsize=(10,5))
    plt.title('Number of units sold per brand')
    plt.bar(x,y, width=0.4, color='red',edgecolor='black',label='Units Sold')
    plt.xlabel('Brand Name')
    plt.ylabel('Units Sold(In Thousands)')
    plt.legend(loc=0)
    plt.tight_layout()
    graph=get_graph()
    return graph
