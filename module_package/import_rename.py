# 読み込んだモジュール名や識別子に別名をつけることができます。

import mypack1.mypack2.mymod as mymod1
mymod1.myfunc()

from mypack1.mypack2 import mymod as mymod2
mymod2.myfunc()

from mypack1.mypack2.mymod import myfunc as myfunc1
myfunc1()