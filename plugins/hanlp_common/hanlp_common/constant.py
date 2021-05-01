# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-06-13 22:41
import os
import locale

PAD = '<pad>'
'''Padding token.'''
UNK = '<unk>'
'''Unknown token.'''
CLS = '[CLS]'
BOS = '<bos>'
EOS = '<eos>'
ROOT = BOS
IDX = '_idx_'
'''Key for index.'''
HANLP_URL = os.getenv('HANLP_URL', 'https://file.hankcs.com/hanlp/')
'''Resource URL.'''
HANLP_VERBOSE = os.environ.get('HANLP_VERBOSE', '1').lower() in ('1', 'true', 'yes')
'''Enable verbose or not.'''
NULL = '<null>'
PRED = 'PRED'
HF_MIRROR = os.getenv('HF_MIRROR', 'tuna' if 'zh_CN' in locale.getdefaultlocale() else None)
'''Mirror site to accelerate downloads of HuggingFace 🤗 Transformers. E.g., ``tuna`` or ``bfsu``. Defaults to 
``tuna`` on zh_CN locale machines and ``None`` on others. '''
