import pandas as pd
import numpy as np
import os
import sentencepiece as spm
from fastai.text import BaseTokenizer
import sentencepiece as spm

FILE_DIR = os.path.dirname(os.path.abspath("__file__"))
MODEL_PATH = os.path.join(FILE_DIR, 'models/sentencepiece/tokenizer.model')

data_paths = {}
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        data_paths[filename] = os.path.join(dirname, filename)
        # print(os.path.join(dirname, filename))
        
class TeluguTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load(MODEL_PATH)
        
    def tokenizer(self, t:str):
        return self.sp.EncodeAsPieces(t)