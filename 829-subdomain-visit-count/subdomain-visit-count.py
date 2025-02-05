class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = defaultdict(int)
        for domains in cpdomains:
            key,val = domains.split(" ")
            # val = val.split(".")
            cnt = int(key)
            domains = val.split(".")
            for i in range(len(domains)):
                d = ".".join(domains[i:])
                domain[d] += cnt
                
                 
            print(domain)
        ans = []
        for key, val in domain.items():
            ans.append(f'{val} {key}') 
        return ans
                