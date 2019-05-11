from google.colab import files
import pandas as pd
import numpy as np
import seaborn as sns # heatmap을 그리기 위한 모듈
import matplotlib.pyplot as plt # 그래프를 그리기 위해서 사용하는 모듈
from PIL import Image # 파이썬 이미지 형식 모듈

def FileUpload(path): # parameter = path
  if os.path.isfile(path):
    print('파일이 이미 존재합니다.')
    return 0
  df = pd.read_excel(path)
  return df
  
if __name__ == "__main__" :
  df = FileUpload(path)
  if(df == 0):
    return
  
  result = df.corr() # 상관계수
  result.to_excel("") # 저장할 파일 경로
  
  Img = sns.heatmap(result, annot=True, linewidths=.5, fmt='.1f', cmap='Blues')

  #내 구글드라이브 경로로 이미지를 저장 하는 과정
  fig = plt.gcf() # 현재 이미지 Instance를 변수에 할당한다.
  plt.show()
  fig.savefig('/content/gdrive/My Drive/capstone/heatmap.jpg') # 이 Instance로 savefig()를 불러온다.
  
