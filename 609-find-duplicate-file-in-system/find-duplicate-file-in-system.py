class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            
            for file_info in parts[1:]:
                filename, content = file_info.split('(')
                content = content[:-1]  
                
                full_path = f"{directory}/{filename}"
                content_dict[content].append(full_path)

        return [group for group in content_dict.values() if len(group) > 1]
