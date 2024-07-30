# YAMLの新規書き込み
# YAMLの新規書き込みを行ってみます。
# 新規作成はカンタンで、辞書型のデータを作ってそれを、dump関数を使うだけです。

import yaml


with open('write_sample.yaml', 'w') as f:
    data = {
        'setting': {
            'language': 'jp'
        }
    }

    yaml.dump(data, f)
# dumpの第１引数に辞書型のデータを入れて、
# 第２引数にファイルのストリームデータを入れます。