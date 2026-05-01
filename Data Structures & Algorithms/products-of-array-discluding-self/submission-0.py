class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_of_all_elements = 1
        res = []
        zero_count = 0

        for num in nums:
            if num==0:
                zero_count+=1
            else:
                product_of_all_elements *= num

        new_prod = product_of_all_elements

        for num in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1 and num!=0:
                res.append(0)
                new_prod = 0
            elif num == 0:
                res.append(product_of_all_elements)
            else:
                res.append(new_prod//num)
        return res