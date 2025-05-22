class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        num_acc = len(accounts)
        parent = list(range(num_acc))

        hashmap = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in hashmap:
                    parent[find(idx)] = find(hashmap[email])
                else:
                    hashmap[email] = idx

        emails_under_parent_account = defaultdict(set)
        for account_index, account in enumerate(accounts):
            for email in account[1:]:
                emails_under_parent_account[find(account_index)].add(email)

        merged_accounts = []
        for parent_index, emails in emails_under_parent_account.items():
            sorted_emails = sorted(emails)
            account_name = [accounts[parent_index][0]]
            merged_account = account_name + sorted_emails
            merged_accounts.append(merged_account)
      
        return merged_accounts
        