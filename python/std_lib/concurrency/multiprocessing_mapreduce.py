#! /usr/bin/env python3 

import collections
import itertools
import multiprocessing

class SimpleMapReduce:

    def __init__(self, map_func, reduce_func, num_workers=None):
        """ 
        map_func: method -> 
                function for mapping input data on intermediate data 
                input 1 arg output tuple into key nad value for reduce
                
        reduce_func: method -> 
                function for reducing itermediate data. as a arg get key 
                from map_func and collection value for this key.
                
        num_workers: param -> 
                number of creating workers in pool of processes. 
                default is number cpu in this host.
        """

        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        """ 
        Managing mapping of key.
        Return sorted sequence of tuples with key and collections 
        of value
        """

        partition_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partition_data[key].append(value)
        return partition_data.items()

    def __call__(self, inputs, chunksize=1):
        """ 
        Working input data from functions for reducing and mapping
        
        inputs: parameter -> iteration object input data
        
        chunksize: parameter -> part of data for sending every worker
        used for settings production for mapreduce.
        """

        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        partitioned_data = self.partition(
            itertools.chain(*map_responses)
        )

        reduced_values = self.pool.map(
            self.reduce_func, 
            partitioned_data,
        )
        return reduced_values

    