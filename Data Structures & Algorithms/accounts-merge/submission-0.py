from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = list(range(len(accounts)))
        size = list(range(len(accounts)))
        email_owner = {}

        def find(element):
            if parents[element]!=element:
                parents[element] = find(parents[element])
            
            return parents[element]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            
            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            parents[rootB] = rootA
            size[rootA]+=size[rootB]
            return True
        
        for index, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in email_owner:
                    email_owner[email] = index
                else:
                    previous_acc = email_owner[email]

                    union(index, previous_acc)
        
        grouped_emails = defaultdict(set)

        for owner, ema in email_owner.items():
            root = find(ema)
            grouped_emails[root].add(owner)
        
        result = []
        
        for ith, groups in grouped_emails.items():
            name = accounts[ith][0]
            all_emails = sorted(groups)
            result.append([name] + all_emails)
        return result
        

        

        
        
        

        