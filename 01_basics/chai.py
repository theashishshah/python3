from hello import chai
from hello import coffee

coffee("capacino")
# chai("from another file")
# if you bring any code from other file, the that file run to start to end first then the imported code


def chai_in_chai(msg):
    print(msg)
chai_in_chai("Hello from chai file")