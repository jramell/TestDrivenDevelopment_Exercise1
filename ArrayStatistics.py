class ArrayStatistics:
    def numElems(self, stringWithCommaSeparatedNumbers):
        if(stringWithCommaSeparatedNumbers == ""):
            return 0;

        return len(stringWithCommaSeparatedNumbers.split(","));

    def numElemsIter2(self, stringWithCommaSeparatedNumbers):
        if(stringWithCommaSeparatedNumbers == ""):
            return [0, -1];
        else:
            return [0, 1];