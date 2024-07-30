# YAMLで読み込んだデータに追記して書き込む
# YAMLファイルを読み込んで、データを追記して書き込みます。
# 新規書き込みのセクションで作成したYAMLファイルを利用して、追記処理をしてみます。

import yaml

with open('./write_sample.yaml', 'r+') as f:
    data = yaml.safe_load(f)
    data['setting']['list'] = [1, 2, 3]
    f.seek(0)
    yaml.dump(data, f)