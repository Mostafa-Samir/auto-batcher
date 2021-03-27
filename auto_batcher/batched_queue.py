""" An extension to multiprocessing Queue class that supports batched get and put
"""
import queue
import multiprocessing as mp
from contextlib import suppress
from typing import Any, Iterable, Union
from multiprocessing.queues import Queue


class BatchedQueue(Queue):
    """Extends the multiprocessing Queue class with `get_batch` and `put_batch` methods
    """

    def __init__(self, maxsize: int = 0) -> None:
        """initializes the batched queue object

        Parameters
        ----------
        maxsize : int, optional
            The maximum size of the queue, by default 0
        """
        super().__init__(maxsize, ctx=mp.get_context())

    def get_batch(self, up_to: int, timeout: Union[None, float] = None) -> Iterable[Any]:
        """Retreives a batch of queued elements up to a given size

        The implementation is inspired by 'Tim Peters' answer on: 
        https://stackoverflow.com/questions/41498614/multiprocessing-queue-batch-get-up-to-max-n-elements

        Parameters
        ----------
        up_to : int
            The maximum number of elements to retrieve in a batch
        timeout : Union[None, float], optional
            How many seconds of blockage on the 1st element before raising a `queue.Empty` exception, by default None

        Returns
        -------
        Iterable[Any]
            A list of queued elements
        """
        batch = [self.get(timeout=timeout)]
        with suppress(queue.Empty):
            while len(batch) < up_to:
                batch.append(self.get(block=False))

        return batch

    def put_batch(self, batch: Iterable[Any]) -> None:
        """Puts a batch of element in the queue

        Parameters
        ----------
        batch : Iterable[Any]
            The batch of elements to put in the queue
        """
        for element in batch:
            self.put(element, block=False)
