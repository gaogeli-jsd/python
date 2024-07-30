# 読み込むモジュールや識別子を複数記述することもできます。

import mypack1.mypack2.mymod1, mypack1.mypack2.mymod2
from mypack1.mypack2 import mymod, mymod2
from mypack1.mypack2 import (mymod, mymod2)
from mypack1.mypack2.mymod import myfunc1, myfunc2
from mypack1.mypack2.mymod import (myfunc1, myfunc2)

mypack1.mypack2.mymod.myfunc2()