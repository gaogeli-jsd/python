# with構文(with)
# 文法
# with expression [as target] [, expression [as target]]... :
#    suite...
# with を用いると、withブロックが終了した際に、
# オブジェクトの終了処理が自動的に呼ばれます。
# 例えば、
#   open() で返却される file オブジェクトは、
#   終了処理として、close() が自動的に呼び出されます。
#   下記の例で、with を用いた書き方では、withブロックが終了した際に 
#      f.close() が自動的に呼び出されます。

# withを用いない書き方
f = open("test.txt")
print(f.read())
f.close()

# withを用いた書き方1
with open("test.txt") as f:
    print(f.read())

# withを用いた書き方2
f = open("test.txt")
with f:
    print(f.read())