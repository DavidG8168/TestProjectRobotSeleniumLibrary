from TestProjectSeleniumLibrary.base import keyword


class my_lib_not_inherit(object):

    def __init__(self, ctx):
        self.ctx = ctx

    @keyword
    def bar(self, arg):
        self.info(arg)
