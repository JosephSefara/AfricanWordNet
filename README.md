# AfricanWordNet: Implementation of WordNets for African languages

This library extends [OMW](http://compling.hss.ntu.edu.sg/omw/) implemented in [NLTK](https://www.nltk.org/) to add support for the following African languages. 

- Sepedi (nso)
- Xitsonga (tsn)
- Tshivenda (ven)
- isiZulu (zul)
- isiXhosa (xho)

[![licence](https://img.shields.io/pypi/l/africanwordnet)](https://github.com/josephsefara/africanwordnet/blob/master/LICENSE) [![GitHub release](https://img.shields.io/github/release/josephsefara/africanwordnet.svg?maxAge=3600)](https://github.com/josephsefara/africanwordnet/releases) [![Wheel](https://img.shields.io/pypi/wheel/africanwordnet.svg?maxAge=3600)](https://pypi.python.org/pypi/africanwordnet) [![python](https://img.shields.io/pypi/pyversions/africanwordnet.svg?maxAge=3600)](https://pypi.org/project/africanwordnet/) [![TotalDownloads](https://pepy.tech/badge/africanwordnet)] 

## Requirements

* [Python 3](https://docs.python.org/3.5/)
* [NLTK](https://www.nltk.org/)
## Installation

- From Pypi
  - ```pip install africanwordnet```
- From source
  - ```pip install https://github.com/JosephSefara/AfricanWordNet.git```

## Citation Paper
```
@inproceedings{sefara2020practical,
  title={Paper Title},
  author={Sefara, Tshephisho and Mokgonyane, Tumisho and Marivate, Vukosi},
  booktitle={Proceedings of the Eleventh Global Wordnet Conference},
  paages={},
  year={2020},
}
```

## Usage

```python
>>> from nltk.corpus import wordnet as wn
>>> import africanwordnet

>>> wn.langs()
['nso', 'tsn', 'ven', 'zul', 'xho']
```
### Setswana WordNet

```python
>>> wn.synsets('phêpafatsa',lang=('tsn'))
[Synset('scavenge.v.04'),
 Synset('tidy.v.01'),
 Synset('refine.v.04'),
 Synset('refine.v.03'),
 Synset('purify.v.01'),
 Synset('purge.v.04'),
 Synset('purify.v.02'),
 Synset('clean.v.08'),
 Synset('clean.v.01'),
 Synset('houseclean.v.01')]

>>> wn.lemmas('phêpafatsa', lang='tsn')
[Lemma('scavenge.v.04.phêpafatsa'),
 Lemma('tidy.v.01.phêpafatsa'),
 Lemma('refine.v.04.phêpafatsa'),
 Lemma('refine.v.03.phêpafatsa'),
 Lemma('purify.v.01.phêpafatsa'),
 Lemma('purge.v.04.phêpafatsa'),
 Lemma('purify.v.02.phêpafatsa'),
 Lemma('clean.v.08.phêpafatsa'),
 Lemma('clean.v.01.phêpafatsa'),
 Lemma('houseclean.v.01.phêpafatsa')]

>>> wn.synset('purify.v.01').lemma_names('tsn')
['phêpafatsa']

>>> lemma = wn.lemma('purify.v.01.phêpafatsa', lang='tsn')
>>> whole_lemma.lang()
'tsn'
```

### Sepedi WordNet

```python
>>> wn.synsets('taelo',lang=('nso'))
[Synset('call.n.12'),
 Synset('mandate.n.03'),
 Synset('command.n.01'),
 Synset('order.n.01'),
 Synset('commission.n.06'),
 Synset('commandment.n.01'),
 Synset('directive.n.01'),
 Synset('injunction.n.01')]

>>> wn.lemmas('taelo', lang='nso')
[Lemma('call.n.12.taelo'),
 Lemma('mandate.n.03.taelo'),
 Lemma('command.n.01.taelo'),
 Lemma('order.n.01.taelo'),
 Lemma('commission.n.06.taelo'),
 Lemma('commandment.n.01.taelo'),
 Lemma('directive.n.01.taelo'),
 Lemma('injunction.n.01.taelo')]

>>> wn.synset('call.n.12').lemma_names('nso')
['taelo']

>>> lemma = wn.lemma('call.n.12.taelo', lang='nso')
>>> whole_lemma.lang()
'nso'
```

### isiZulu WordNet

```python
>>> wn.synsets('iqoqo', lang='zul')
[Synset('whole.n.02'),
 Synset('conspectus.n.01'),
 Synset('overview.n.01'),
 Synset('sketch.n.03'),
 Synset('compilation.n.01'),
 Synset('collection.n.01'),
 Synset('team.n.02'),
 Synset('set.n.01')]

>>> wn.lemmas('iqoqo', lang='zul')
[Lemma('whole.n.02.iqoqo'),
 Lemma('conspectus.n.01.iqoqo'),
 Lemma('overview.n.01.iqoqo'),
 Lemma('sketch.n.03.iqoqo'),
 Lemma('compilation.n.01.iqoqo'),
 Lemma('collection.n.01.iqoqo'),
 Lemma('team.n.02.iqoqo'),
 Lemma('set.n.01.iqoqo')]

>>> wn.synset('whole.n.02').lemma_names('zul')
['iqoqo']

>>> whole_lemma = wn.lemma('whole.n.02.iqoqo', lang='zul')
>>> whole_lemma.lang()
'zul'
```

### isiXhosa WordNet

```python
>>> wn.synsets('imali',lang=('xho'))
[Synset('finance.n.03'),
 Synset('wealth.n.04'),
 Synset('capital.n.01'),
 Synset('store.n.02'),
 Synset('credit.n.02'),
 Synset('money.n.01'),
 Synset('currency.n.01'),
 Synset('purse.n.02'),
 Synset('franc.n.01'),
 Synset('cent.n.01')]

>>> wn.lemmas('imali', lang='xho')
[Lemma('finance.n.03.imali'),
 Lemma('wealth.n.04.imali'),
 Lemma('capital.n.01.imali'),
 Lemma('store.n.02.imali'),
 Lemma('credit.n.02.imali'),
 Lemma('money.n.01.imali'),
 Lemma('currency.n.01.imali'),
 Lemma('purse.n.02.imali'),
 Lemma('franc.n.01.imali'),
 Lemma('cent.n.01.imali')]

>>> wn.synset('wealth.n.04').lemma_names('xho')
['imali']

>>> lemma = wn.lemma('wealth.n.04.imali', lang='xho')
>>> lemma.lang()
'xho'
```

### Tshivenda WordNet

```python
>>> wn.synsets('tshifanyiso',lang=('ven'))
[Synset('picture.n.05'), 
 Synset('word_picture.n.01'), 
 Synset('portrayal.n.01')]

>>> wn.lemmas('tshifanyiso', lang='ven')
[Lemma('picture.n.05.tshifanyiso'),
 Lemma('word_picture.n.01.tshifanyiso'),
 Lemma('portrayal.n.01.tshifanyiso')]

>>> wn.synset('picture.n.05').lemma_names('ven')
['tshifanyiso']

>>> lemma = wn.lemma('picture.n.05.tshifanyiso', lang='ven')
>>> whole_lemma.lang()
'ven'
```

## Find related words
The word **taelo** in Sepedi is related to 

- tagafalo
- molao
- tlhalošo

```python
words = set()
synsets = wn.synsets('taelo',lang=('nso'))
for synset in synsets: # synset is in english
     for hypo in synset.hyponyms():
        for lemma in hypo.lemmas("nso"):
            words.add(lemma.name())
print('taelo', '---', words)

taelo --- {'taelo', 'tagafalo', 'molao', 'tlhalošo'}
```