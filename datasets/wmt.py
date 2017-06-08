# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))
from tools.config import *
from copy import deepcopy
from multi_language import MultiLanguageDataset


class WMT16_de_en(MultiLanguageDataset):
    """docstring for Dataset."""

    def __init__(self,
                 root,
                 split='train',
                 tokenization='bpe',
                 num_symbols=32000,
                 shared_vocab=True,
                 code_files=None,
                 vocab_files=None,
                 insert_start=[BOS],
                 insert_end=[EOS],
                 tokenizers=None,
                 load_data=True):

        train_prefix = "{root}/train.clean".format(root=root)
        options = dict(
            prefix=train_prefix,
            languages=['en', 'de'],
            tokenization=tokenization,
            num_symbols=num_symbols,
            shared_vocab=shared_vocab,
            code_files=code_files,
            vocab_files=vocab_files,
            insert_start=insert_start,
            insert_end=insert_end,
            tokenizers=tokenizers,
            load_data=False
        )
        train_options = deepcopy(options)

        if split == 'train':
            options = train_options
        else:
            train_data = MultiLanguageDataset(**train_options)
            options['tokenizers'] = getattr(train_data, 'tokenizers', None)
            options['code_files'] = getattr(train_data, 'code_files', None)
            options['vocab_files'] = getattr(train_data, 'vocab_files', None)
            if split == 'dev':
                prefix = "{root}/newstest2014.clean".format(root=root)
            elif split == 'test':
                prefix = "{root}/newstest2016.clean".format(root=root)

            options['prefix'] = prefix
        super(WMT16_de_en, self).__init__(**options)
        if load_data:
            self.load_data()
