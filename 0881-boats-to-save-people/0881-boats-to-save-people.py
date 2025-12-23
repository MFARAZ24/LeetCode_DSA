class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left,right = 0, len(people)-1
        people.sort()
        countBoat = 0
        while left<=right:
            sum = people[left]+people[right]

            if sum<=limit:
                countBoat +=1
                left +=1
                right -=1
            else:
                countBoat +=1
                right -= 1
        
        return countBoat

        