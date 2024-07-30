# from には、. や .. を用いて、パッケージを相対的に指示することができます。

# ????????????????????  要調査

from . import mymod              # このパッケージから mymodモジュールをインポートする
from .. import mymod             # ひとつ上の階層のパッケージから mymodモジュールをインポートする
from ... import mymod            # ふたつ上の階層のパッケージから mymodモジュールをインポートする
from ...mypack4 import mymod     # ふたつ上の階層のmypack4パッケージから mymodモジュールをインポートする