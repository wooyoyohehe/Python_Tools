# Example 1
# We can see that when it comes to the error in the try block
# Then the except block will be excuted and the rest of try block will be ignored
# Also, except will catch all kinds of errors, only if you add the kind after except
try:
    print 'Error starts here'
    a = b
    print 'Error ends here'
except:
    print 'Here is the error!!'

# Example 2
print '-------------------------'
print 
print 'Example2'
try:
    print 'Error starts here'
    a = b
    print 'Error ends here'
except SyntaxError:
    print 'There is a SyntaxError!!'
except IndexError:
    print 'There is a IndexError'
except:
    print 'I have no idea what error is, but there is one'

# Example 3
print '-------------------------'
print 
print 'Example3'
try:
    
    a = 1
    
except SyntaxError:
    print 'There is a SyntaxError!!'
except IndexError:
    print 'There is a IndexError'
except:
    print 'I have no idea what error is, but there is one'
# If there is no error, execute else block
else:
    print 'Good job, no error!'
# Regardless there is error or not, fianlly block WILL BE excuted!
finally:
    print 'I know how to use try-except!'