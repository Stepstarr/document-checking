from baseclass import BaseClass


class TableClass(BaseClass):
    def __init__(self,doc):
        super().__init__(doc)
        '''
        除了继承基类属性，还要根据自己负责的模块该模块属性
        例如，标题有自己的属性，几层标题
        目标为：这个xx类可以通过属性对该类状况有个了解
        '''
        pass

    def check(self):
        pass
