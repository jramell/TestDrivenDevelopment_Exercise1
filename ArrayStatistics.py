class ArrayStatistics:
    def numElems(self, stringWithCommaSeparatedNumbers):
        if(stringWithCommaSeparatedNumbers == ""):
            return 0;

        return len(stringWithCommaSeparatedNumbers.split(","));