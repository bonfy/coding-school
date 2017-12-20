
# threading.Thread 类方法 run

    def run(self):
        """Method representing the thread's activity.
        You may override this method in a subclass. 
        The standard run() method
        invokes the callable object passed to 
        the object's constructor as the
        target argument, if any, with sequential and 
        keyword arguments taken
        from the args and kwargs arguments, respectively.
        """
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs