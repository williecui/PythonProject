#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

#Series索引在左边 值在右边。由于我们没有为数据指定索引。于是会自动创建一个0到N-1（N为长度）的整数型索引
s = pd.Series([1,3,6,np.nan,44,1])
print(s)

df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),columns=['a', 'b', 'c', 'd', 'e'])
print(df2)

df2 = pd.DataFrame({'A' : 1.,
					'B' : pd.Timestamp('20130102'),
					'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
					'D' : np.array([3] * 4,dtype='int32'),
					'E' : pd.Categorical(["test","train","test","train"]),
					'F' : 'foo'})
print(df2)