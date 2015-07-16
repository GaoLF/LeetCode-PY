class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        vec = []
        i = 0
        string = ''
        while i < len(path):
            if path[i] == '/':
                if string:
                    vec.append(string)
                string = ''
            else:
                string += path[i:i+1]
            i += 1
        if path[len(path)-1] != '/':
            vec.append(string)
        stack = []
        for iter in vec:
            if iter == '.':
                pass
            elif iter == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(iter)
        res = ''
        for iter in stack:
            res += '/' + iter
        if not res:
            res = '/'
        return res




A = Solution()
print A.simplifyPath("/a/./b/../../c")
print A.simplifyPath("/home/")
print A.simplifyPath("/...")
print A.simplifyPath("/home//foo/")