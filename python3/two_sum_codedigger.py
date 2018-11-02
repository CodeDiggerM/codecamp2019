class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = dict()
        result = None
        
        def check_elem(v, target):
            theother_num = target - v
            try:
                index = num_map[target - v]
                return index
            except KeyError:
                return None
            
        def reorder(i1, i2):
            if i1 < i2:
                return [i1, i2]
            else:
                return [i2, i1]
        
        for i, v in enumerate(nums):
            num_map[v] = i
            result_index = check_elem(v, target)
            if result_index is not None and result_index != i:
                return reorder(i, result_index)
        for i,v in enumerate(nums):
            result_index = check_elem(v, target)
            if result_index is not None and result_index != i:
                return reorder(i, result_index)
        if result_index is None:
            raise("There is not correct answer!!")
            
