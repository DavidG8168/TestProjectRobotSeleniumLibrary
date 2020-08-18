from collections import OrderedDict

from TestProjectSeleniumLibrary.base import LibraryComponent, keyword


class PluginWithAllArgs(LibraryComponent):

        def __init__(self, ctx, arg, *varargs, **kwargs):
            LibraryComponent.__init__(self, ctx)
            self.arg = arg
            self.varargs = varargs
            self.kwargs = kwargs

        @keyword
        def return_all_args_as_string(self):
            joined_str = 'start: arg=%s,' % self.arg
            for arg in self.varargs:
                joined_str = '%s %s,' % (joined_str, arg)
            kwargs = OrderedDict(sorted(self.kwargs.items()))
            for key in kwargs:
                joined_str = '%s %s=%s,' % (joined_str, key, kwargs[key])
            return joined_str[:-1]
