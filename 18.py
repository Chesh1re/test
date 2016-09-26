class Solution():
    def crossRiver(self,prea,savg,boatpos,state):
        tmp={'prea':5,'savg':5,'boatpos':1}
        stack=[]
        moved=[]
        sontable={}
        stack.append(tmp)
        while stack:
            curr=stack.pop()
            state.append(curr)
            if curr in moved:
                state.pop()
                sontable[str(state[-1])]-=1
                if sontable[str(state[-1])]==0:
                    state.pop()
                continue
            else:
                moved.append(curr)
            if (curr['prea']==0 and curr['savg']==0 and curr['prea']==0):
                break
            elif (curr['prea']<curr['savg'] and curr['prea']!=0) or (5-curr['prea']<5-curr['savg'] and 5-curr['prea']!=0):
                state.pop()
                sontable[str(state[-1])]-=1
                if sontable[str(state[-1])]==0:
                        state.pop()
                continue
            else:
                count=0
                if curr['boatpos']==1:
                    if curr['savg']>=3:
                        stack.append({'prea':curr['prea'],'savg':curr['savg']-3,'boatpos':curr['boatpos']-1})
                        count+=1
                    if curr['savg']>=2:
                        stack.append({'prea':curr['prea'],'savg':curr['savg']-2,'boatpos':curr['boatpos']-1})
                        count+=1
                    if curr['savg']>=1:
                        stack.append({'prea':curr['prea'],'savg':curr['savg']-1,'boatpos':curr['boatpos']-1})
                        count+=1
                    if curr['prea']>=3:
                        stack.append({'prea':curr['prea']-3,'savg':curr['savg'],'boatpos':curr['boatpos']-1})
                        count+=1
                    if curr['prea']>=2 and curr['savg']>=1:
                        stack.append({'prea':curr['prea']-2,'savg':curr['savg']-1,'boatpos':curr['boatpos']-1})
                        count+=1
                    if curr['prea']>=2:
                        stack.append({'prea':curr['prea']-2,'savg':curr['savg'],'boatpos':curr['boatpos']-1})
                        count+=1
                    if curr['prea']>=1 and curr['prea']>=1:
                        stack.append({'prea':curr['prea']-1,'savg':curr['savg']-1,'boatpos':curr['boatpos']-1})
                        count+=1
                    if curr['prea']>=1:
                        stack.append({'prea':curr['prea']-1,'savg':curr['savg'],'boatpos':curr['boatpos']-1})
                        count+=1
                elif curr['boatpos']==0:
                    if 5-curr['savg']>=3:
                        stack.append({'prea':curr['prea'],'savg':curr['savg']+3,'boatpos':curr['boatpos']+1})
                        count+=1
                    if 5-curr['savg']>=2:
                        stack.append({'prea':curr['prea'],'savg':curr['savg']+2,'boatpos':curr['boatpos']+1})
                        count+=1
                    if 5-curr['savg']>=1:
                        stack.append({'prea':curr['prea'],'savg':curr['savg']+1,'boatpos':curr['boatpos']+1})
                        count+=1
                    if 5-curr['prea']>=3:
                        stack.append({'prea':curr['prea']+3,'savg':curr['savg'],'boatpos':curr['boatpos']+1})
                        count+=1
                    if 5-curr['prea']>=2 and 5-curr['savg']>=1:
                        stack.append({'prea':curr['prea']+2,'savg':curr['savg']+1,'boatpos':curr['boatpos']+1})
                        count+=1
                    if 5-curr['prea']>=2:
                        stack.append({'prea':curr['prea']+2,'savg':curr['savg'],'boatpos':curr['boatpos']+1})
                        count+=1
                    if 5-curr['prea']>=1 and 5-curr['prea']>=1:
                        stack.append({'prea':curr['prea']+1,'savg':curr['savg']+1,'boatpos':curr['boatpos']+1})
                        count+=1
                    if 5-curr['prea']>=1:
                        stack.append({'prea':curr['prea']+1,'savg':curr['savg'],'boatpos':curr['boatpos']+1})
                        count+=1
                sontable[str(curr)]=count
        return state

s=Solution()
res=s.crossRiver(5,5,1,[])
print res
