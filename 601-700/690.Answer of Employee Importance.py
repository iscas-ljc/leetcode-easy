class Solution(object):
    def getImportance(self, employees, id):
    	dmap = {emp.id : emp for emp in employees}
    	def solve(id):
    		emp = dmap[id]
    		return emp.importance+ sum(solve(id) for id in emp.subordinates)
    	return solve(id)
