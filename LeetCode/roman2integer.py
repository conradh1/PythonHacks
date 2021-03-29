def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i = 0
        
        while i < len(s):                        
            if s[i] == 'I':
                if ( (i + 1) < len(s)):                    
                    if (s[i+1] == 'V'):                                                                        
                        total += 4
                        i += 1                   
                    elif (s[i+1] == 'X'):                        
                        total += 9
                        i += 1
                    else:
                        total += 1
                else:
                    total +=1                      
            elif s[i] == 'V':
                total +=5                       
            elif s[i] == 'X':
                if ( i + 1 < len(s)):                    
                    if (s[i+1] == 'L'):
                        total += 40
                        i += 1
                    elif (s[i+1] == 'C'):
                        total += 90
                        i += 1
                    else:
                        total += 10
                else:
                    total +=10                    
            elif s[i] == 'L':
                total +=50                    
            elif s[i] ==  'C':
                if ( i + 1 < len(s) ):                    
                    if (s[i+1] == 'D'):
                        i += 1
                        total += 400
                    elif (s[i+1] == 'M'):
                        i += 1
                        total += 900
                    else:
                        total += 100
                else:
                    total +=100                
            elif s[i] ==  'D':                
                total +=500                    
            elif s[i] ==  'M':
                total +=1000
            i += 1

        return total

if __name__ == '__main__':
    s = str(raw_input().strip())    
    print(str(romanToInt(s)))    