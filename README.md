# text classification in tensorflow
Implementing multi models for Text Classification in TensorFlow.

## Contents
### Data and Preprocess
#### Data
Models are used to perform sentiment analysis on movie reviews from the [Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/), which contains 25,000 highly polar movie reviews for training, and 25,000 for testing.<br/>
In this task, given a movie review, the model attempts to predict whether it is positive or negative. This is a binary classification task.

#### Preprocess
1. Load positive and negative sentences from the raw data files.
2. Clean the text data.
3. Pad each sentence to the maximum sentence length.
4. Word vector mapping, Each sentence becomes a bag of word vectors.

### Models
#### 1. FastText
<div align=center>
<img src='imgs/fast_text_model.png' width='400' height='200'>
</div>

- text classification: [Bag of Tricks for Efficient Text Classification, 2016.07](https://arxiv.org/abs/1607.01759)

#### 2. TextCNN
<div align=center>
<img src='imgs/text_cnn_model.png' width='700' height='300'>
</div>

<div align=center>
<img src='imgs/text_cnn_model_explain.png' width='600' height='500'>
</div>

- [Convolutional Neural Networks for Sentence Classification, 2014.08](https://arxiv.org/abs/1408.5882)
- [A Sensitivity Analysis of (and Practitioners' Guide to) Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1510.03820)

#### 3. BiLSTM
<div align=center>
<img src='imgs/bilstm_model.png' width='600' height='300'>
</div>

- [Bidirectional Recurrent Neural Networks, 1997](http://ieeexplore.ieee.org/document/650093/)

#### 4. TextRCNN
![](./imgs/rcnn_model.png)
Learn more contextual information   than conventional window-based neural networks.
- [Recurrent Convolutional Neural Networks for Text Classification, 2015](https://scholar.google.com.hk/scholar?q=Recurrent+Convolutional+Neural+Networks+for+Text+Classification&hl=zh-CN&as_sdt=0&as_vis=1&oi=scholart&sa=X&ved=0ahUKEwjpx82cvqTUAhWHspQKHUbDBDYQgQMIITAA)

#### 5. Hierarchical Attention Networks
<div align=center>
<img src='imgs/han_model.png' width='500' height='500'>
</div>

- [Hierarchical Attention Networks for Document Classification, 2016](http://www.cs.cmu.edu/~./hovy/papers/16HLT-hierarchical-attention-networks.pdf)

#### 6. Seq2seq with Attention
- [Neural Machine Translation by Jointly Learning to Align and Translate, 2014.09](https://arxiv.org/abs/1409.0473)

## Performance
```
epochs = 10
batch_size = 64
max_learning_rate = 0.001
decay_rate = 0.8
decay_steps = 2000
l2_reg_lambda = 1e-3
embedding_trainable = False
```

Models   | fastText|TextCNN |BiLSTM    | TextRCNN | HierAtteNet|Seq2seqAttn|EntityNet|DynamicMemory|Transformer
---      | ---     | ---    |---       |---       |---         |---        |---      |---          |----
Accuracy |0.834304 |0.878276| 0.884974 |0.840128  |0.889314    |           |         |             |

## References
- [Understanding Convolutional Neural Networks for NLP](http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/)
- [Implementing a CNN for Text Classification in TensorFlow](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow)
- [Github: cnn-text-classification-tf](https://github.com/cahya-wirawan/cnn-text-classification-tf)
- [基于 word2vec 和 CNN 的文本分类 ：综述 & 实践](https://zhuanlan.zhihu.com/p/29076736)
- [自然语言处理中CNN模型几种常见的Max Pooling操作](http://blog.csdn.net/malefactor/article/details/51078135)
- [LSTM Networks for Sentiment Analysis](http://deeplearning.net/tutorial/lstm.html)
- [Bag of Tricks for Efficient Text Classification](https://arxiv.org/abs/1607.01759)
- [Chatbots with Seq2Seq](http://suriyadeepan.github.io/2016-06-28-easy-seq2seq/)

## License
This project is licensed under the terms of the MIT license.
