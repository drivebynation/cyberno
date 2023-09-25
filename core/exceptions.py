class ExistError(Exception):
    """
    Use this Error When Entered string exists in queue
    """
    pass


class ArrivedTurn(Exception):
    """
    Use this error when an arrived turn item asked
    """
    pass

class EmptyQueueError(Exception):
    """
    Use this Error for Empty Queue
    """
    pass