
## NLP for Telugu

[ULMFit Telugu Encodings Projections]( https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/Asrst/telugu_nlp/master/configs/ulmfit_encodings_projection.json )


### Features:

##### Tokenizers
- Sentencepiece tokenizer trained on Telugu Wikipedia data of nearly 90K articles

##### Language Models
- ULMFit trained on Telugu Wikipedia data of nearly 90K articles & its 400 dimensional word vector Encodings for 25000 most frequent vocab.

##### Classification
- created the eenadu newspaper dataset of around 20K articles constituting of 5 classes. With finetuned language model encodings, the classification accuracy is 95%. 

### Requirements:

code tested on following versions, however should work with pytorch v1.0+ , fastai v1.0+ , python v3.5+

`python v3.6`
`pytorch==1.3.0`
`fastai==1.0.59`

### Usage:




### citations & references

- [sentencepiece](https://github.com/google/sentencepiece)
- [fastai](https://www.fast.ai/)
- [nlp-for-marathi](https://github.com/goru001/nlp-for-marathi)
