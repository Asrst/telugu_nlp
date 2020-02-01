import os
os.system('pip install inltk')
import pandas as pd
import numpy as np
import re
import sentencepiece as spm
import pickle
import pathlib
import fastai
from fastai.text import BaseTokenizer
import sentencepiece as spm
import inltk
print(fastai.__version__)

data_paths = {}
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        data_paths[filename] = os.path.join(dirname, filename)
        # print(os.path.join(dirname, filename))
        
class TeluguTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load(data_paths['telugu_tok.model'])
        
    def tokenizer(self, t:str):
        return self.sp.EncodeAsPieces(t)