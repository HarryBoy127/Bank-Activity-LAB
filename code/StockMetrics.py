
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

     def average01(self):
         averages = []
        for row in self.data:
             valid_price = []
        for price in row:
            if price_str.strip()
             price = float(price_str)
            valid_prices.append(price)
             if valid_prices:
                 average = sum(valid_price) / len(valid_price)
                 average = round(average, 3)
                averages.append(average)  
        return averages

    def median02(self):
        medians = []
        for row in self.data
            row_value = []
        for value in row :
             if value_str.strip()
             numeric_value = float(value)
             row_value.append(value)
            if row_value:
            row_median = statistics.median(row_value)
             medians.append(median)
        return medians
             
    def stddev03(self):
        stddevs = []
        for row in self.data
            row_value = []
        for value in row :
             if value_str.strip()
             numeric_value = float(value)
             row_value.append(value)
        if row_value:
            row_stddev = round(statistics.stddev(row_value),3)
            stddevs.append(stddev)
        return stddevs
             
        
       
    
        ...
