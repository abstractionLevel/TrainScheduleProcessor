import os
import csv
from datetime import datetime

class TrainScheduleProcessor:

    def __init__(self,actualCsv,plannedCsv):
        self.actualCsv =  os.path.join(actualCsv)
        self.plannedCsv = os.path.join(plannedCsv)
      
    def getListFromCsv(self,file):
        csvList = []
        try:
            with open(file, newline='') as csvfile:
                csvReader = csv.reader(csvfile)
                for row in csvReader:
                    csvList.append(row)
            csvList = csvList[1:]
            return csvList
        except FileNotFoundError:
            print(f"Errore: Il file {file} non è stato trovato.")
            return None

    def writeCsv(self,file):
        with open('output.csv', 'w', newline='') as fileCsv:
            writer = csv.writer(fileCsv)
            writer.writerows(file)
            print("CSV CREATED")

    def calculateDelay(self,currentTimestamp,plannedTimestamp):
        if(currentTimestamp > plannedTimestamp):
            return (currentTimestamp-plannedTimestamp).seconds
        else:
            return  -(plannedTimestamp - currentTimestamp).seconds

    def matchTrains(self,current,planned):
        return current[0] == planned[0] and current[1] == planned[1]
    
    def getTopNTrainsWithHighestDelays(self,n,list):
        sortedList = sorted(list, key=lambda x: x[-1], reverse=True)
        return sortedList[:n]

    def numberTrainExistInList(self,numberTrain,trainSchedule):
        for row in trainSchedule:
            if(row[0]==numberTrain):
                return True
        return False

    def getDestinationOfTrains(self,listOfTrain):
        destination = []
        trainSchedule = []
        for x in listOfTrain:
            if not (self.numberTrainExistInList(x[0],trainSchedule)):
                for y in listOfTrain:
                    if(x[0]==y[0]):
                        destinationProv = y
                trainSchedule.append(destinationProv)
        return trainSchedule

    def processSchedule(self,currentTrain,plannedTrain):
        outputTrainSchedule = []
        for current in currentTrain:
            for planned in plannedTrain:
                if self.matchTrains(current,planned):
                    currentTimestamp  = datetime.fromisoformat(current[2])
                    plannedTimestamp = datetime.fromisoformat(planned[2])
                    difference = self.calculateDelay(currentTimestamp,plannedTimestamp)
                    outputTrainSchedule.append([current[0],current[1],planned[2],current[2],difference])
                    break
        return outputTrainSchedule

    def run(self):
        actualCsv = self.getListFromCsv(self.actualCsv)
        plannedCsv =  self.getListFromCsv(self.plannedCsv)
        if(actualCsv and plannedCsv):
            destinationOfTrains  = self.getDestinationOfTrains(actualCsv)
            output = self.processSchedule(destinationOfTrains,plannedCsv)
            topNTrains =self.getTopNTrainsWithHighestDelays(5,output)
            topNTrains.insert(0,['Numero treno','destinazione', 'Ora pianificata', 'Ora Effettiva','Ritardo'])
            self.writeCsv(topNTrains)

if __name__ == "__main__":
    trainScheduleProcessor = TrainScheduleProcessor("actual.csv","planned.csv")
    trainScheduleProcessor.run()
