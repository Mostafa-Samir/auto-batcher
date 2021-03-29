import queue
import unittest
import os
from auto_batcher.batched_queue import BatchedQueue

class BatchedQueueTest(unittest.TestCase):

    def test_get_batch(self):
        """Tests the `get_batch` method of the batched queue
        """
        bqueue = BatchedQueue()

        for i in range(5):
            bqueue.put(i)

        self.assertListEqual(bqueue.get_batch(up_to=3), [0, 1, 2])
        self.assertListEqual(bqueue.get_batch(up_to=3), [3, 4])
        with self.assertRaises(queue.Empty):
            bqueue.get_batch(up_to=3, timeout=0.05)
    
        if os.name == 'nt':
            self.fail("Failing on windows")

    def test_put_batch(self):
        """Tests the `put_batch` method of the batched queue
        """
        bqueue = BatchedQueue()

        bqueue.put_batch([0, 1, 2, 3, 4])

        for i in range(5):
            self.assertEqual(bqueue.get(), i)
