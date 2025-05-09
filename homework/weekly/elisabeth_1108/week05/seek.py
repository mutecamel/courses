import inspect

import wat

module_path = inspect.getfile(wat)
print(module_path)
