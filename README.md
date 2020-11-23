# AfricanWordNet: Implementation of WordNets for African languages

This library extends [OMW](http://compling.hss.ntu.edu.sg/omw/) implemented in [NLTK](https://www.nltk.org/) to add support for the following African languages. 

- Sepedi (nso)
- Xitsonga (tsn)
- Tshivenda (ven)
- isiZulu (zul)
- isiXhosa (xho)

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![GitHub release](https://img.shields.io/github/release/josephsefara/africanwordnet.svg?maxAge=3600)](https://github.com/josephsefara/africanwordnet/releases) [![Wheel](https://img.shields.io/pypi/wheel/africanwordnet.svg?maxAge=3600)](https://pypi.python.org/pypi/africanwordnet) [![python](https://img.shields.io/pypi/pyversions/africanwordnet.svg?maxAge=3600)](https://pypi.org/project/africanwordnet/) [![TotalDownloads](https://pepy.tech/badge/africanwordnet)]

## Requirements

* [Python 3](https://docs.python.org/3.5/)
* [NLTK](https://www.nltk.org/)
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

>>> wn.synsets('iqoqo', lang='zul')
[Synset('whole.n.02'),
 Synset('conspectus.n.01'),
 Synset('overview.n.01'),
 Synset('sketch.n.03'),
 Synset('compilation.n.01'),
 Synset('collection.n.01'),
 Synset('team.n.02'),
 Synset('set.n.01')]

>>> wn.synset('entity.n.01').lemmas('zul')
[Lemma('entity.n.01.selô'), Lemma('entity.n.01.sengwe')]

>>> wn.synset('entity.n.01').lemma_names('tsn')
['selô', 'sengwe']

>>> wn.lemmas('iqoqo', lang='zul')
[Lemma('whole.n.02.iqoqo'),
 Lemma('conspectus.n.01.iqoqo'),
 Lemma('overview.n.01.iqoqo'),
 Lemma('sketch.n.03.iqoqo'),
 Lemma('compilation.n.01.iqoqo'),
 Lemma('collection.n.01.iqoqo'),
 Lemma('team.n.02.iqoqo'),
 Lemma('set.n.01.iqoqo')]

>>> whole_lemma = wn.lemma('whole.n.02.iqoqo', lang='zul')
>>> whole_lemma.lang()
'zul'
```

```

```