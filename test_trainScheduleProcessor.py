import unittest
from trainScheduleProcessor  import TrainScheduleProcessor
from datetime import datetime

class TestTrainScheduleProcessor(unittest.TestCase):

    def setUp(self):
        self.actualCsv = 'actual.csv'
        self.plannedCsv = 'test_planned.csv'

    
    def testDelay(self):
        processor = TrainScheduleProcessor(self.actualCsv,self.plannedCsv)
        currentTimestamp = datetime.fromisoformat('2023-12-15 12:30:00')
        plannedTimestamp = datetime.fromisoformat('2023-12-15 12:00:00')
        result = processor.calculateDelay(currentTimestamp,plannedTimestamp)
        expected = 1800 #secondi
        self.assertEqual(result,expected)

    def testNegativeDelay(self):
        processor = TrainScheduleProcessor(self.actualCsv,self.plannedCsv)
        currentTimestamp = datetime.fromisoformat('2023-12-15 02:34:51')
        plannedTimestamp = datetime.fromisoformat('2023-12-15 02:35:00')
        result = processor.calculateDelay(currentTimestamp,plannedTimestamp)
        expected = -9 #secondi
        self.assertEqual(result,expected)

    def testGetTopNTrainsWithHighestDelays(self):
        processor = TrainScheduleProcessor(self.actualCsv,self.plannedCsv)
        trains = [
            ['test', 'test', 'test', 'test', -13],
            ['test', 'test', 'test', 'test', -1],
            ['test', 'test', 'test', 'test', -43],
            ['test', 'test', 'test', 'test', 20],
            ['test', 'test', 'test', 'test', 180],
            ['test', 'test', 'test', 'test', -2],
            ['test', 'test', 'test', 'test', 60],
            ['test', 'test', 'test', 'test', -6],
            ['test', 'test', 'test', 'test', -1],
            ['test', 'test', 'test', 'test', 210]
        ]
        result = processor.getTopNTrainsWithHighestDelays(5,trains)
        expected = [
            ['test', 'test', 'test', 'test', 210],
            ['test', 'test', 'test', 'test', 180],
            ['test', 'test', 'test', 'test', 60],
            ['test', 'test', 'test', 'test', 20],
            ['test', 'test', 'test', 'test', -1],

        ]
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()