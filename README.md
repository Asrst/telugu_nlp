
## NLP for Telugu Language
[ULMFit Telugu Encodings Projections](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/Asrst/telugu_nlp/master/configs/ulmfit_encodings_projection.json)

### Features:

##### Datasets
- datasets are in parquet format: use pandas to read/transform.
- [download telugu Wikipedia Dataset (Around 90K articles)](https://www.kaggleusercontent.com/kf/26015022/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..k4nKDWsCusgnjqogRZrnzA.OU1MWX1-FIEDVuXPu8wi-UwpIgpFr0_0bM4_7yfce94ukEtyleSKlL-hmTJ_omjpGr_rDaBYXeNBOSdkiGok1VaiRNKybHRRNnCaJLMPdD58c67a3W6iGQjC43kEJEOtSTK05FijZtgOsG-xFPIDVQ.177bN782lLlwHAWiLeBvug/telugu_wikipedia_dataset.parquet)
- [download telugu Eenaadu news Dataset (Around 20K articles)](https://www.kaggleusercontent.com/kf/27437409/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..zWxRELYkTqwDopoh_TZEXg.0PldkKOu4nG-q6jQmPYrDphs4tQMB2A0MBC6HJr3vQefsWu0f5FwJyOQ42T43pjyxsNy2gpuMzRIu7MYQMzLYUtKEj0BIj3cRSOHFC2xRDn6FLGpFoyZX8veu8ffeYaGY3IVNwzO9-ycXpK8HMYEhxuzbocg_4QkCIuDxTwiJYA.R1Y0oqRGbftDrqgyF38Mww/telugu_news_dataset.parquet)

##### Tokenizers
- Sentencepiece tokenizer trained on Telugu Wikipedia data of nearly 90K articles.
- [telugu sentencepiece tokenizer](https://www.kaggleusercontent.com/kf/26479363/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..-BXoVOeJA2JGUuZyUbBY3A.zsCX_eO0zC6yPbX3of4K3RgHaHC8S4RcMRGw14Kriv6v9fAljDFXSTLzrGuAY4PHzRm5R_qZggR3qRK3oreuuzLHxJ2cs4o_riLpGZdp6JIku-UMw48zhIqysi5N4I_T4vcsDA2IKESiVJxLWkzpjqLBUy50An416GBJBZR0GbM.9trJ6REXR4h_I-S6Hrf_5g/telugu_tok.model)
- [telugu sentencepiece vocab](https://www.kaggleusercontent.com/kf/26479363/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..57bZ3zui1_YFfsEH-IC6cQ.ZGbpfef3YRrgKKZb8sM9dOQZyXgqViI5lzEqOpjTjkfdmDsmr4h16iujIKIk6gKL8FIVGeFKAzGslTEsMIwaTav5nJUFzblruvxDYZQZd6KZFWxdHNsia15F48mx60pF9e1O2_v5qaUdZBImD4jBdrwfOLjE1KIfshftA6KvLI0.TY4TDSoRa2GhdLjx3aiCGg/telugu_tok.vocab)

##### Language Models
- ULMFit trained on Telugu Wikipedia data of nearly 90K articles & its 400 dimensional word vector Encodings for 25000 most frequent vocab.json)
- [telugu language model (fastai-awdlstm)](https://www.kaggleusercontent.com/kf/27942526/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..eCTy6WnQCV5x3Kx6xOVcFw.iNiic9H0pyUGenMQJvB5ytsckd1sugreGMnsKC9jJenNlt1Uu1slFHgeMb-M4usW1UgN8MmhorxgIjTk6bQMGUUhZchRxy7FjDJoO2jmqRSnuF5kYB9uEOP5yLGhHk5gLz5ohK-kaslVgpPkI14V9Q.JUalOHl2WD0HeH_sWwo04g/export.pkl)
- for other intermediate training files, refer the kaggle kernel [telugu LM (fastai-awdlstm)](https://www.kaggle.com/asrsaiteja/telugu-language-model/output)

##### Classification
- created the Eenaadu newspaper dataset of around 20K articles constituting of 5 classes. With finetuned language model encodings, the classification accuracy is 95%.
- [classification model on eenaadu news data (5 classes)](https://www.kaggleusercontent.com/kf/27966237/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..BIRG2gkUI9-E6SNUd1TsMQ.h28q1wBvvhOHPpIZBEX-kuogFnEGMPa-o2G0h9GJWhB6EE6sjQ7uwH9JBa_aTLAqGuQIYJ9ujdO2IE8j9rqx8Hy7A6pUu5UPO1-49Z7vmTWNFxKzw8bgX-DQZIZn6DzLTdPxwF2l2uOSUMUJhDCiJhsk1wFl1wTSn42W8ZajzT4.YEABHar2HOD0yXNZh89xQQ/models/final_cls.pth)

### Requirements:

code tested on following versions, however should work with pytorch v1.0+ , fastai v1.0+ , python v3.5+

`python v3.6`
`pytorch==1.3.0`
`fastai==1.0.59`

### citations & references

- [sentencepiece](https://github.com/google/sentencepiece)
- [fastai](https://www.fast.ai/)
- [nlp-for-marathi](https://github.com/goru001/nlp-for-marathi)
