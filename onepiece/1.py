def longestValidParentheses(s):
	s = ')'+s
	n=len(s)
	dp=[]
	for i in range(0,n):
		dp.append(0)
	maxl=0
	for i in range(1,n):
		if s[i]==')':
			k=i-1
			k-=dp[k]
			if s[k]=='(':
				dp[i]=i-k+1
			dp[i]+=dp[i-dp[i]]
		maxl=max(maxl,dp[i])
	return maxl
print longestValidParentheses("((((((()()()")
