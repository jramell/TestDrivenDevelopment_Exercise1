class ArrayStatistics:
    def numElems(self, stringWithCommaSeparatedNumbers):
        if(stringWithCommaSeparatedNumbers == ""):
            return 0;

        return len(stringWithCommaSeparatedNumbers.split(","));

    def numElemsIter2(self, stringWithCommaSeparatedNumbers):
        if(stringWithCommaSeparatedNumbers == ""):
            return [0, -1]
        else:
            numbers = stringWithCommaSeparatedNumbers.split(",")
            minimum = numbers[0]
            for number in numbers:
                minimum = min(number, minimum)

            return [len(numbers), int(minimum)]

    def numElemsIter3(self, stringWithCommaSeparatedNumbers):
        if(stringWithCommaSeparatedNumbers == ""):
            return [0, -1, -1]
        else:
            return [1, 1, 1]