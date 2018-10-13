class SuperClass:
    def hoge(self, id):
        print("---")
        print("SuperClass.hoge=", id)

class SubClass(SuperClass):
    def hoge(self, id):
        super().hoge(id)
        print("SubClass.hoge=", id)

# 基底クラスのhogeメソッドの実行例
rc = SuperClass()
rc.hoge(100)

# 派生クラスのhogeメソッドの実行例:
sc = SubClass()
sc.hoge(300)
