class Hunts(object):
    
    def __init__(self, class_key, records):
        self.records = records
        self.class_key = class_key
        
    def converge(self, records=None):
        if records is None:
            records = self.records
        
        if (self.records_in_single_class(records)):
            self.make_node(records)
        else:
            partitions = self.compute_partitions(records)
            for partition in partitions:
                self.make_node(partition)
                self.converge(partition['records'])
                
    def records_in_single_class(self, records):
        """Checks whether all the class fields are of
        the same value"""
        initial_class_value = records[0][self.class_key]
        
        for record in records:
            if record[self.class_key] != initial_class_value:
                return False
                
        return True